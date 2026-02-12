cmake_minimum_required(VERSION 3.15)
project(PVZ_Reproduction 
    VERSION 1.0.0
    LANGUAGES CXX
    DESCRIPTION "Plants vs Zombies Reproduction Edition"
)

# ==========================================
# 0. 全局配置与环境
# ==========================================

# 强制要求 C++ 17 标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 导出编译数据库供 VSCode/CLion 索引使用
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# ==========================================
# 1. 查找并配置第三方依赖
# 需保证已执行过 git submodule update --init
# ==========================================

# A. Python & pybind11
# 查找 Python 解释器和开发头文件

# 优先检测虚拟环境
if(EXISTS "${CMAKE_SOURCE_DIR}/.venv")
    # 虚拟环境存在，使用它
    if(WIN32)
        set(Python_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/Scripts/python.exe")
        set(Python3_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/Scripts/python.exe")
    else()
        set(Python_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/bin/python")
        set(Python3_EXECUTABLE "${CMAKE_SOURCE_DIR}/.venv/bin/python")
    endif()
endif()

set(Python_FIND_VIRTUALENV FIRST)
set(Python3_FIND_VIRTUALENV FIRST)

find_package(Python COMPONENTS Interpreter Development REQUIRED)
add_subdirectory(deps/pybind11)

# B. yaml-cpp (仅编译库，跳过测试)
set(YAML_CPP_BUILD_TESTS OFF CACHE BOOL "" FORCE)
add_subdirectory(deps/yaml-cpp EXCLUDE_FROM_ALL)    # 除非被依赖，否则不编译

# C. SFML (仅编译图形，窗口，音频模块)
# 如果使用 SFML，需要配置其不构建例子以节省时间
set(SFML_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(SFML_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(SFML_BUILD_AUDIO ON CACHE BOOL "" FORCE)        # 编译 SFML 的音频模块
add_subdirectory(deps/sfml EXCLUDE_FROM_ALL)

# ==========================================
# 2. 定义功能模块库
# ==========================================

# === A. 公共协议库 (Header-Only) ===
# 包含 common 目录下的 Types, Constants, Utils
add_library(pvz_common_lib INTERFACE)
# 指定头文件搜索路径
target_include_directories(pvz_common_lib INTERFACE
    ${CMAKE_SOURCE_DIR}/core/include
)

# === B. 核心引擎库 (Static Library) ===
# 负责渲染、物理、管理器的实现
file(GLOB_RECURSE ENGINE_SOURCES
    CONFIGURE_DEPENDS
    "${CMAKE_SOURCE_DIR}/core/src/entities/*.cpp"
    "${CMAKE_SOURCE_DIR}/core/src/framework/*.cpp"
)
# 调试时输出源文件列表
# 正常模式 cmake ..
# 调试模式 cmake .. --debug-output
if(CMAKE_MESSAGE_LOG_LEVEL STREQUAL "DEBUG")
    message(STATUS "Engine sources: ${ENGINE_SOURCES}")  # 调试：显示找到的文件
endif()

# 创建引擎库
add_library(pvz_engine_lib STATIC ${ENGINE_SOURCES})

# 引擎库依赖：公共协议、SFML、YAML
target_link_libraries(pvz_engine_lib PUBLIC
    pvz_common_lib
    sfml-graphics
    sfml-window 
    sfml-system
    sfml-audio
    yaml-cpp
)

# 包含头文件路径
target_include_directories(pvz_engine_lib PUBLIC 
    ${CMAKE_SOURCE_DIR}/core/include
)

# ==========================================
# 3. 生成 Python 绑定模块 (Module)
# ==========================================

# 胶水层：将 C++ 引擎导出给 Python
# 通过 pybind11 将 C++ 引擎暴露给 Python
pybind11_add_module(pvz_core binding/python_wrapper.cpp)

# 链接核心引擎库
target_link_libraries(pvz_core PRIVATE pvz_engine_lib)
target_include_directories(pvz_core PRIVATE
    ${CMAKE_SOURCE_DIR}/core/include
)

# 设置输出路径：直接生成到 build 根目录方便 Python import
set_target_properties(pvz_core PROPERTIES
    # Windows 上 .pyd 被视为 RUNTIME，不是 LIBRARY
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    # 为 Mac 或 Linux 准备
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)

# ==========================================
# 4. 环境配置 (可选)
# ==========================================

# 强制使用静态链接，防止因缺少 DLL 而崩溃
if(MINGW OR CYGWIN)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static")
    set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} -static")
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -static")
endif()

# ==========================================
# 5. 统一设置严格警告，并将其视为错误
# 仅针对自有代码，不针对第三方库
# ==========================================

# 只在自己的库上设置严格警告，并将警告视为错误
if(MSVC)
    # /WX 表示将警告视为错误
    target_compile_options(pvz_common_lib INTERFACE /W4 /WX)
    target_compile_options(pvz_engine_lib PRIVATE /W4 /WX)
    target_compile_options(pvz_core PRIVATE /W4 /WX)
else()
    # -Werror 表示将警告视为错误
    target_compile_options(pvz_common_lib INTERFACE -Wall -Wextra -Werror)
    target_compile_options(pvz_engine_lib PRIVATE -Wall -Wextra -Werror)
    target_compile_options(pvz_core PRIVATE -Wall -Wextra -Werror)
endif()
# PVZ_CPP

这是一个使用 **C++ (核心引擎)** 与 **Python (游戏逻辑)** 混合开发的《植物大战僵尸》复现项目。本项目采用数据驱动设计，通过 **YAML** 进行配置管理。

## 1. 项目架构

项目采用“分层开发”模式，以实现底层性能与高层开发效率的平衡：

* **Core (C++17)**: 处理游戏循环、窗口渲染 (SFML/SDL2)、物理碰撞检测、资源管理及 Python 绑定。
* **Script (Python 3.x)**: 处理植物/僵尸的具体 AI 逻辑、关卡波次控制及游戏数值。
* **Data (YAML)**: 存储所有实体的属性数值及关卡配置，实现无需重新编译即可调整平衡性。

## 2. 目录结构

```text
PVZ_CPP/
├── core/                   # C++ 核心源码
│   ├── include/            # 头文件 (.hpp)
│   └── src/                # 实现文件 (.cpp)
├── scripts/                # Python 逻辑脚本
│   ├── entities/           # 植物与僵尸的具体逻辑
│   ├── ui/                 # 负责游戏所有非战斗实体的交互界面。
│   └── main.py             # 游戏入口
├── binding/                # pybind11 接口定义
├── data/                   # YAML 配置文件 (植物、僵尸、关卡)
├── assets/                 # 游戏资源 (图片、音频)
├── deps/                   # 第三方依赖 (pybind11, yaml-cpp 等)
├── CMakeLists.txt          # 顶层 CMake 配置文件
└── CONTRIBUTING.md         # 开发协议与规范 (必读)
```

## 3. 环境准备

在开始协作前，请确保本地环境已安装：

* **编译器**: 支持 C++17 的 GCC (9.0+) 或 Clang，或 MSVC (VS2019+)。
* **构建工具**: CMake (3.15+)。
* **Python**: Python 3.8+ 及开发环境头文件。
* **Python 库**: `pip install PyYAML`。
* **图形库**: 根据选择安装 SFML 或 SDL2。

## 4. 快速开始

### 4.1 克隆仓库

由于项目包含第三方依赖，请务必使用递归克隆：

```bash
git clone --recursive https://github.com/114August514/pvz_cpp
cd pvz_cpp
```

如果仅执行了普通的 `git clone`，请补充拉取子模块：

```bash
git submodule update --init --recursive
```

### 4.2 编译 C++ 核心

编译产生的动态库（`.so` 或 `.pyd`）将供 Python 调用：

```bash
mkdir build && cd build
cmake ..
cmake --build . --config Release
```

### 4.3 运行游戏

确保编译产物在 Python 的搜索路径中，然后启动：

```bash
python scripts/main.py
```

## 5. 开发规范

为了保证多人协作不产生冲突，本项目严格执行以下规矩：

1. **分工守则**：修改底层算法动 `core/`，修改技能逻辑动 `scripts/`，修改数值动 `data/`。
2. **代码风格**：C++ 遵循 `PascalCase` 类名，Python 遵循 `PEP8`。
3. **注释规范**：所有公开接口必须包含 Doxygen 或 Docstring 注释。
4. **YAML 约束**：修改配置后需校验缩进，确保符合 YAML 格式。

详细规范请参阅：[CONTRIBUTING.md](./CONTRIBUTING.md)

## 6. 当前进度 (Roadmap)

* [ ] 底层场景管理与渲染系统 (C++)
* [ ] YAML 解析器与实体工厂 (C++/Python)
* [ ] 基础格位系统与种植逻辑 (Python)
* [ ] 基础僵尸行走与碰撞检测 (C++/Python)
* [ ] 关卡波次加载系统 (Python/YAML)

## 7. 成员

* **[不知道]**: 负责底层架构、渲染系统、碰撞算法。
* **[不知道]**: 负责实体 AI、关卡逻辑、数值平衡。

"""
初始化 Python 环境，处理 C++ 扩展加载的依赖问题
"""
import sys
import os
import shutil
from pathlib import Path
from typing import Optional

def _get_build_dir() -> Optional[Path]:
    """探测构建目录，支持常见的 CMake 构建模式"""
    root_dir = Path(__file__).parent.parent
    # 仅检测标准构建目录
    candidates = [
        root_dir / "build",
        root_dir / "cmake-build-debug",
    ]
    return next((p for p in candidates if p.is_dir()), None)

def setup_dll_paths() -> None:
    """
    配置动态库搜索路径（Windows/Linux/macOS）。
    注意：在 Windows + Python 3.8+ 环境下，必须显式调用 os.add_dll_directory。
    """
    build_dir = _get_build_dir()
    if not build_dir:
        return

    # 收集项目中可能存在的 DLL 路径
    project_lib_dirs: list[Path] = [
        build_dir,
        build_dir / "deps" / "sfml" / "lib",
        build_dir / "deps" / "yaml-cpp",
        build_dir / "bin"
    ]

    if sys.platform == "win32":
        # Windows: 添加 DLL 搜索路径
        # 1. 处理项目内部依赖
        for lib_dir in filter(Path.is_dir, project_lib_dirs):
            try:
                os.add_dll_directory(str(lib_dir.resolve()))
            except Exception:
                pass

        # 2. 处理工具链依赖 (MinGW)
        # 自动寻找并添加 MinGW 路径
        # 尝试通过 g++ 的位置找到 MinGW 的 bin 目录
        gxx_path = shutil.which("g++")
        if gxx_path:
            mingw_bin = Path(gxx_path).parent
            try:
                os.add_dll_directory(str(mingw_bin.resolve()))
                print(f"Added MinGW DLL path: {mingw_bin}")
            except Exception as e:
                print(f"Failed to add MinGW path: {e}")

    elif sys.platform in ("linux", "linux2", "darwin"):
        # Linux: 添加到 LD_LIBRARY_PATH
        # macOS: 添加到 DYLD_LIBRARY_PATH
        existing_paths = [str(p.resolve()) for p in project_lib_dirs if p.is_dir()]
        if not existing_paths:
            return

        # 根据平台选择环境变量名
        env_var = "LD_LIBRARY_PATH" if sys.platform.startswith("linux") else "DYLD_LIBRARY_PATH"

        # 获取原有值并拼接新路径 (新路径在前，保证优先级)
        old_val = os.environ.get(env_var, "")
        new_val = ":".join(existing_paths)
        os.environ[env_var] = f"{new_val}:{old_val}" if old_val else new_val

def setup_build_path() -> Optional[Path]:
    """将构建目录加入 sys.path 以便导入 .pyd/.so 模块"""
    build_dir = _get_build_dir()
    if build_dir:
        # 使用 resolve() 确保绝对路径，使用 insert(0) 确保最高优先级
        resolved_path = str(build_dir.resolve())
        if resolved_path not in sys.path:
            sys.path.insert(0, resolved_path)
        return build_dir

    return None

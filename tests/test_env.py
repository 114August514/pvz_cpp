import sys
from pathlib import Path

# 1. 找到项目根目录并加入 sys.path
# 这样才能找到 scripts 文件夹
ROOT_DIR = Path(__file__).parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# 2. 现在可以正常导入 scripts 里的工具了
from scripts._init_env import setup_dll_paths, setup_build_path

import pytest


def test_cpp_binding_loadable():
    """测试 C++ 核心库是否能被正确加载"""
    # 3. 初始化 DLL 加载路径
    setup_dll_paths()
    build_path = setup_build_path()

    # 4. 尝试导入（运行时会去 build 找）
    import pvz_core

    message = pvz_core.hello_world()
    assert message is not None
    assert "Hello" in message
    print(f"\n[Test] Received from C++: {message}")

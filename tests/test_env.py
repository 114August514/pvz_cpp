# 通过在根目录运行测试：
#   pytest tests/test_env.py -s

import sys
from pathlib import Path
import pytest

# 1. 导入 scripts.core
# 关键：这会触发 scripts/__init__.py，
#       进而自动执行 _env.py 里的 DLL 加载和路径配置
from scripts.core import pvz_core

def test_cpp_binding_loadable():
    """测试 C++ 核心库是否已正确编译并在 Python 中可用"""
    # 调用 C++ 胶水层暴露的测试函数
    message = pvz_core.hello_world()

    assert message is not None
    assert "Hello" in message
    print(f"\n[Environment] C++ Core is active: {message}")

def test_core_data_types():
    """验证 C++ 定义的基础数据类型是否能被 Python 正确解析"""
    # 测试结构体定义
    vec = pvz_core.Vector2(100.0, 200.0)
    assert vec.x == 100.0
    assert vec.y == 200.0

    # 测试网格坐标定义
    grid = pvz_core.GridPos()
    assert grid.row == -1
    assert grid.col == -1

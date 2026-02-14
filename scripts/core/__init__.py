# 将 core 目录声明为一个 Python 包，并对外暴露统一的入口

# 运行时，通过 _env 已配置好的 sys.path 导入真正的 C++ 扩展
# 明确保留 pvz_core 模块
# 从当前目录导入代理模块 pvz_core.py
from . import pvz_core

__all__ = ["pvz_core"]
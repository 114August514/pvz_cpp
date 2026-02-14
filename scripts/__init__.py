from . import _env

# 自动初始化环境：
# 1. 将构建生成的 .pyd 所在目录加入 sys.path
_build_dir = _env.setup_build_path()
# 2. 注入依赖的 DLL 搜索路径 (Windows 必须)
_env.setup_dll_paths()

# 导出重要模块
from . import config

__all__ = ["_env", "config"]
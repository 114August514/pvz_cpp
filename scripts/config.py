"""
统一管理路径，避免代码中的硬编码。
"""

from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).parent.parent.resolve()

# 资源与数据目录
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
LEVELS_DIR = DATA_DIR / "levels"

# 运行配置
DEBUG = True
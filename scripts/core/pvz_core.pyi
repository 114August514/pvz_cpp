from enum import Enum
from types import ModuleType

# === A. 枚举变量 ===

class Side(Enum):
    PLANT: Side
    ZOMBIE: Side
    NEUTRAL: Side

class GameState(Enum):
    MENU: GameState
    PREPARATION: GameState
    PLAYING: GameState
    PAUSED: GameState
    WIN: GameState
    LOSE: GameState

# === B. 结构体定义 ===

class Vector2:
    x: float
    y: float
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None: ...

class GridPos:
    row: int
    col: int
    def __init__(self, row: int = -1, col: int = -1) -> None: ...
    def is_valid(self) -> bool: ...
    def __eq__(self, other: GridPos) -> bool: ...

# === C. 全局常量定义 ===

# config 是一个 submodule（运行时为模块实例）
class _ConfigModule(ModuleType):
    """全局配置命名空间（submodule）"""
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int

config: _ConfigModule

# === D. 验证函数 ===

def hello_world() -> str:
    """返回欢迎信息，用于验证 C++ 绑定"""
    ...

from enum import Enum

# === A. 枚举变量 ===

class Side(Enum):
    PLANT: int
    ZOMBIE: int
    NEUTRAL: int

class GameState(Enum):
    MENU: int
    PREPARATION: int
    PLAYING: int
    PAUSED: int
    WIN: int
    LOSE: int

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

class config:
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int
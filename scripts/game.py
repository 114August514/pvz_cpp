from .config import BASE_DIR
from .core import pvz_core

def run():
    """游戏主循环入口"""
    print(f"PVZ Project root: {BASE_DIR}")
    print("Initializing PVZ Game Engine...")

    # 验证 C++ 绑定
    message = pvz_core.hello_world()
    print(f"Engine Reply: {message}")

    # 这里后续会添加真正的窗口循环，例如：
    # engine = pvz_core.Engine()
    # engine.run()

import sys
from pathlib import Path

# 获取项目根目录
ROOT_DIR = Path(__file__).parent.parent

# 将编译后的 C++ 路径（通常在 build 文件夹下）加入环境变量
# 这样无论在什么环境下执行，都能 import pvz_core
possible_build_dirs = [
    ROOT_DIR / "build",
    ROOT_DIR / "cmake-build-debug",
    ROOT_DIR / "build/Debug",
    ROOT_DIR / "cmake-build-debug/Debug",
]

for build_dir in possible_build_dirs:
    if build_dir.exists():
        sys.path.insert(0, str(build_dir))
        print(f"Added build path: {build_dir}")
        break

try:
    import pvz_core
    print("Successfully imported pvz_core")
except ImportError as e:
    print(f"Failed to import pvz_core: {e}")
    sys.exit(1)

# 验证 C++ 绑定
message = pvz_core.hello_world()
print(f"Message from C++: {message}")

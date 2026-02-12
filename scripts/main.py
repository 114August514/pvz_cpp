from _init_env import setup_dll_paths, setup_build_path

# 初始化环境
setup_dll_paths()
setup_build_path()

try:
    import pvz_core

    print("Successfully imported pvz_core")
except ImportError as e:
    print(f"Failed to import pvz_core: {e}")
    exit(1)

# 验证 C++ 绑定
message = pvz_core.hello_world()
print(f"Message from C++: {message}")

# 1. 运行时逻辑：
try:
    # 尝试导入原生 C++ 扩展 (pyd/so)
    # 我们期望它已经在 scripts/__init__.py 中通过 _env.py 被加入了 sys.path
    import pvz_core as _core
except ImportError as e:
    # 捕获导入错误并提供更有针对性的诊断建议
    error_header = "\n" + "!" * 60
    error_footer = "!" * 60 + "\n"
    diagnosis = (
        f"{error_header}\n"
        f"[加载失败] 无法导入原生 C++ 模块 'pvz_core'\n\n"
        f"诊断信息:\n"
        f"  1. 请确认 C++ 核心引擎是否已编译。 (尝试运行: cmake --build build)\n"
        f"  2. 请检查构建目录 (build/ 或 cmake-build-debug/) 下是否存在 .pyd 或 .so 文件。\n"
        f"  3. 原始错误信息: {e}\n"
        f"{error_footer}"
    )

    # 抛出更有意义的错误，方便开发者定位
    raise ImportError(diagnosis) from e

# 将原生模块的内容合并到当前命名空间
# 这让外部调用者通过 scripts.core.pvz_core 访问时，就像访问原生模块一样
globals().update({k: v for k, v in _core.__dict__.items() if not k.startswith('__')})

# 这个文件不需要写任何逻辑，它的存在就是为了满足 IDE 对“源码文件”的搜索需求
# 所有的代码提示都会由同目录下的 pvz_core.pyi 提供

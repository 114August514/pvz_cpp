import sys

# 1. 运行时逻辑：
# 我们在 scripts/__init__.py 中已经通过 _env.py 把 build 目录加入了 sys.path
# 所以这里可以直接 import 最外层的原生 pvz_core (pyd/so)
import pvz_core as _core
    
# 将原生模块的内容合并到当前命名空间
# 这让外部调用者通过 scripts.core.pvz_core 访问时，就像访问原生模块一样
globals().update({k: v for k, v in _core.__dict__.items() if not k.startswith('__')})

# 这个文件不需要写任何逻辑，它的存在就是为了满足 IDE 对“源码文件”的搜索需求
# 所有的代码提示都会由同目录下的 pvz_core.pyi 提供
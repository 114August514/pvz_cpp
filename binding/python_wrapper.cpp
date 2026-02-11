//
// Created by Admin on 26-2-10.
// 作为 Python 与 C++ 交互的桥梁。
//

#include <pybind11/pybind11.h>
#include "common/Constants.hpp"
#include "common/Types.hpp"

// 为命名空间命名别名。
namespace py = pybind11;
using namespace pvz;

/**
 * @brief PVZ Core Engine 的 Python 绑定模块
 * @param pvz_core Python 模块名 (在 Python 中用 import pvz_core 导入)
 * @param m pybind11 模块对象
 *
 * 该模块将 PVZ 游戏引擎的核心类型导出到 Python,包括:
 *  - Side: 阵营枚举(植物/僵尸)
 *  - Vector2: 二维向量结构体
 *  - GridPos: 网格坐标结构体
 */
PYBIND11_MODULE(pvz_core, m) {
    // 模块文档字符串
    m.doc() = "PVZ Core Engine SDK";

    // 导出 Side 枚举类型
    // 允许 Python 代码使用 Side.PLANT 和 Side.ZOMBIE
    py::enum_<Side>(m, "Side")
        .value("PLANT", Side::PLANT)            // 植物阵营
        .value("ZOMBIE", Side::ZOMBIE)          // 僵尸阵营
        .export_values();                       // 允许不带前缀访问 (如 PLANT)

    // 导出 Vector2 二维向量结构体
    // 用于表示浮点坐标或速度向量
    py::class_<Vector2>(m, "Vector2")
        .def(py::init<float, float>())          // 构造函数 Vector2(x, y)
        .def_readwrite("x", &Vector2::x)        // x 坐标，可读写
        .def_readwrite("y", &Vector2::y);       // y 坐标，可读写

    // 导出 GridPos 网格坐标结构体
    // 用于表示游戏中的格子坐标 (行,列)
    py::class_<GridPos>(m, "GridPos")
        .def(py::init<int, int>())              // 构造函数 GridPos(row, col)
        .def_readwrite("row", &GridPos::row)    // 行索引，可读写
        .def_readwrite("col", &GridPos::col)    // 列索引，可读写
        .def("is_valid", &GridPos::is_valid)    // 验证位置是否在有效范围内
        .def(py::self == py::self);             // 重载 == 运算符
}
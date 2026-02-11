//
// Created by Admin on 26-2-10.
// 类型定义。
//

#ifndef TYPES_H
#define TYPES_H

#include "common/Constants.hpp"

namespace pvz {

// 游戏状态枚举
enum class GameState {
    MENU,           // 主菜单
    PREPARATION,    // 选卡界面
    PLAYING,        // 战斗中
    PAUSED,         // 暂停
    WIN,            // 胜利
    LOSE            // 失败
};

// 阵营划分
enum class Side {
    PLANT,          // 植物
    ZOMBIE,         // 僵尸
    NEUTRAL         // 中立
};

// 物理坐标定义（二维向量）
struct Vector2 {
    float x;
    float y;

    Vector2(float x = 0.0f, float y = 0.0f) : x(x), y(y) {}
};

// 网格坐标
struct GridPos {
    int row;
    int col;

    GridPos(int row = -1, int col = -1) : row(row), col(col) {}

    bool is_valid() const {
        return row >= 0 && row < config::GRID_ROWS && col >= 0 && col < config::GRID_COLS;
    }

    // 重载 判等，方便查找
    bool operator==(const GridPos& other) const {
        return row == other.row && col == other.col;
    }
};

} // namespace pvz

#endif //TYPES_H

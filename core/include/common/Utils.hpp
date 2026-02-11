//
// Created by Admin on 26-2-10.
// 静态工具函数。
//

#ifndef UTILS_H
#define UTILS_H

#include "common/Constants.hpp"
#include "common/Types.hpp"

namespace pvz
{

class Utils {
public:
    /**
     * @brief 将网格坐标 (row, col) 转换为屏幕像素位置 [格子中心点坐标 (x, y)]
     */
    static Vector2 grid_to_screen(GridPos pos) {
        float x = config::GRID_OFFSET_X + pos.col * config::CELL_WIDTH + (config::CELL_WIDTH / 2.0f);
        float y = config::GRID_OFFSET_Y + pos.row * config::CELL_HEIGHT + (config::CELL_HEIGHT / 2.0f);

        return Vector2(x, y);
    }

    /**
     * @brief 将鼠标点击的屏幕坐标转换为对应的网格坐标
     * @return 如果点击在草坪外，可以返回 -1 的坐标进行判断
     */
    static GridPos screen_to_grid(Vector2 pixel) {
        int col = static_cast<int> ((pixel.x - config::GRID_OFFSET_X) / config::CELL_WIDTH);
        int row = static_cast<int> ((pixel.y - config::GRID_OFFSET_Y) / config::CELL_HEIGHT);

        GridPos pos(row, col);
        return pos.is_valid() ? pos : GridPos(-1, -1);
    }

    /**
     * @brief 用以限制数值范围。
     * 
     */
    template<typename T>
    static T clamp(T val, T min, T max) {
        if (val < min) return min;
        if (val > max) return max;
        return val;
    }
};

} // namespace pvz


#endif //UTILS_H

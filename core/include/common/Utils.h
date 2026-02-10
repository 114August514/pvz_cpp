//
// Created by Admin on 26-2-10.
// 静态工具函数。
//

#ifndef UTILS_H
#define UTILS_H

# include "common/Constants.h"
# include "common/Types.h"

namespace pvz
{

class Utils {
public:
    /**
     * @brief 将网格坐标 (row, col) 转换为屏幕像素中心点坐标 (x, y)
     */
    static Vector2 grid_to_screen(int row, int col) {
        float x = config::GRID_OFFSET_X + col * config::CELL_WIDTH + (config::CELL_WIDTH / 2.0f);
        float y = config::GRID_OFFSET_Y + row * config::CELL_HEIGHT + (config::CELL_HEIGHT / 2.0f);

        return {x, y};
    }

    /**
     * @brief 将鼠标点击的屏幕坐标转换为对应的网格坐标
     * @return 如果点击在草坪外，可以返回 -1 的坐标进行判断
     */
    static GridPos screen_to_grid(float x, float y) {
        int col = static_cast<int> ((x - config::GRID_OFFSET_X) / config::CELL_WIDTH);
        int row = static_cast<int> ((y - config::GRID_OFFSET_Y) / config::CELL_HEIGHT);

        // 边境检查
        if (row < 0 || row >= config::GRID_ROWS || col < 0 || col >= config::GRID_COLS)
            return {-1, -1};
        return {row, col};
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

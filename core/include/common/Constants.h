//
// Created by Admin on 26-2-10.
// 全局物理常量
//

#ifndef CONSTANTS_H
#define CONSTANTS_H

namespace pvz {
    namespace config {
        // 窗口与渲染设置 (包括窗口尺寸和帧率)
        inline constexpr int SCREEN_WIDTH = 1024;
        inline constexpr int SCREEN_HEIGHT = 768;
        inline constexpr int FRAME_RATE = 60;

        // 草坪网格设置 (pvz 标准 5 x 9)
        inline constexpr int GRID_ROWS = 5;
        inline constexpr int GRID_COLS = 9;

        // 单个格子的像素尺寸
        inline constexpr float CELL_WIDTH = 80.0f;
        inline constexpr float CELL_HEIGHT = 100.0f;

        // 草坪左上角在屏幕上的偏移坐标 (用于画面对齐)
        inline constexpr float GRID_OFFSET_X = 150.0f;
        inline constexpr float GRID_OFFSET_Y = 100.0f;

        // 初始游戏数值
        inline constexpr int INITIAL_SUN = 50;
        inline constexpr int MAX_PLANT_HEALTH = 300;
        inline constexpr int ZOMBIE_BASIC_HP = 200;
    } // namespace config
} // namespace pvz

#endif //CONSTANTS_H

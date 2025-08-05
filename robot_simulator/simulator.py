# robot_simulator/simulator.py

import tkinter as tk
from .robot import Robot

CELL_SIZE = 60

class RobotSimulator:
    def __init__(self, map_data):
        self.map_data = map_data
        self.robot = Robot(map_data)
        self.root = tk.Tk()
        self.root.title("机器人模拟器")

        self.canvas = tk.Canvas(self.root, width=self.robot.cols * CELL_SIZE, height=self.robot.rows * CELL_SIZE)
        self.canvas.pack()

        self.status_label = tk.Label(self.root, text="状态：RUNNING")
        self.status_label.pack()

        self.create_buttons()
        self.bind_keys()
        self.draw()

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="左转", command=self.turn_left).grid(row=0, column=0)
        tk.Button(frame, text="前进", command=self.move_forward).grid(row=0, column=1)
        tk.Button(frame, text="右转", command=self.turn_right).grid(row=0, column=2)

    def bind_keys(self):
        self.root.bind("<Left>", lambda e: self.turn_left())
        self.root.bind("<Up>", lambda e: self.move_forward())
        self.root.bind("<Right>", lambda e: self.turn_right())

    def turn_left(self):
        self.robot.turn_left()
        self.update()

    def turn_right(self):
        self.robot.turn_right()
        self.update()

    def move_forward(self):
        self.robot.move_forward()
        self.update()

    def update(self):
        self.draw()
        self.status_label.config(text=f"状态：{self.robot.status}，方向：{self.robot.direction}")

    def draw(self):
        self.canvas.delete("all")
        for i in range(self.robot.rows):
            for j in range(self.robot.cols):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                cell = self.map_data[i][j]
                if cell == '#':
                    color = 'black'
                elif cell == 'S':
                    color = 'lightgreen'
                elif cell == 'E':
                    color = 'orange'
                else:
                    color = 'white'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='gray')

        rx, ry = self.robot.x, self.robot.y
        cx1 = ry * CELL_SIZE + 10
        cy1 = rx * CELL_SIZE + 10
        cx2 = cx1 + CELL_SIZE - 20
        cy2 = cy1 + CELL_SIZE - 20
        self.canvas.create_oval(cx1, cy1, cx2, cy2, fill='blue')

        midx = ry * CELL_SIZE + CELL_SIZE // 2
        midy = rx * CELL_SIZE + CELL_SIZE // 2
        offset = 20
        dx, dy = Robot.MOVES[self.robot.direction]
        self.canvas.create_line(midx, midy, midx + dy * offset, midy + dx * offset, fill='red', width=3)

    # def run(self):
    #     self.root.mainloop()


    def run(self):
        # 使用定时器持续更新画面，允许外部调用修改 robot
        self._schedule_update()
        self.root.mainloop()

    def _schedule_update(self):
        self.update()
        self.root.after(100, self._schedule_update)  # 每100ms刷新一次

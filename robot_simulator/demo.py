# robot_simulator/demo.py

from robot_simulator import RobotSimulator

# 示例地图
map_data = [
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '.', '.'],
    ['S', '.', '.', '.', 'E'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.']
]

sim = RobotSimulator(map_data)
sim.run()

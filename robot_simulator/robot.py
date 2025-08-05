# robot_simulator/robot.py
class Robot:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVES = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.x, self.y = self.find_start()
        self.direction = 'N'
        self.status = 'RUNNING'

    def find_start(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'S':
                    return i, j
        raise ValueError("地图中没有起点 S")

    def turn_left(self):
        idx = Robot.DIRECTIONS.index(self.direction)
        self.direction = Robot.DIRECTIONS[(idx - 1) % 4]
        return self.status

    def turn_right(self):
        idx = Robot.DIRECTIONS.index(self.direction)
        self.direction = Robot.DIRECTIONS[(idx + 1) % 4]
        return self.status

    def move_forward(self):
        dx, dy = Robot.MOVES[self.direction]
        nx, ny = self.x + dx, self.y + dy
        if not (0 <= nx < self.rows and 0 <= ny < self.cols):
            self.status = "FAILED_OUT_OF_BOUNDS"
        elif self.grid[nx][ny] == '#':
            self.status = "FAILED_HIT_OBSTACLE"
        else:
            self.x, self.y = nx, ny
            if self.grid[nx][ny] == 'E':
                self.status = "SUCCESS"
        return self.status

import queue

class RobotController:
    def __init__(self, simulator):
        self.simulator = simulator
        self.command_queue = queue.Queue()
        self._running = False

    def turn_left(self):
        self.command_queue.put(self.simulator.robot.turn_left)

    def turn_right(self):
        self.command_queue.put(self.simulator.robot.turn_right)

    def move_forward(self):
        self.command_queue.put(self.simulator.robot.move_forward)

    def start(self):
        self._running = True
        self._process_commands()

    def stop(self):
        self._running = False

    def _process_commands(self):
        if not self._running:
            return
        try:
            command_func = self.command_queue.get_nowait()
        except queue.Empty:
            command_func = None

        if command_func:
            command_func()
            self.simulator.update()

        self.simulator.root.after(1000, self._process_commands)

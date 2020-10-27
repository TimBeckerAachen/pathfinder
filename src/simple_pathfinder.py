class SimplePathfinder:
    def __init__(self, maze):
        # TODO: change order x, y??
        self.maze = maze
        self. possible_steps = []
        self.tried_positions = []
        assert len(set([len(row) for row in self.maze])) == 1
        self.dim = [len(self.maze), len(self.maze[0])]
        self.start = self.get_start()
        self.end = self.get_end()

    def ispath(self):
        y, x = self.start
        while not (y == self.end[0] and x == self.end[1]):
            self.tried_positions.append((y, x))

            current_possible_steps = self.check_directions(y, x)
            current_possible_steps = [step for step in current_possible_steps if step not in self.tried_positions]
            self.possible_steps.extend(current_possible_steps)

            if not self.possible_steps:
                return False

            y, x = self.possible_steps.pop()

        return True

    def check_directions(self, y, x):
        steps = []
        for step in [-1, 1]:
            if 0 <= x + step < self.dim[1]:
                field = self.maze[y][x + step]
                if field != 'w':
                    steps.append((y, x + step))

            if 0 <= y + step < self.dim[0]:
                field = self.maze[y + step][x]
                if field != 'w':
                    steps.append((y + step, x))
        return steps

    def get_start(self):
        return self._get_pos('s')

    def get_end(self):
        return self._get_pos('e')

    def _get_pos(self, pos_type):
        for y in range(self.dim[0]):
            for x in range(self.dim[1]):
                if self.maze[y][x] == pos_type:
                    return y, x
        print(f'{pos_type} not found')




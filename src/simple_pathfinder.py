class SimplePathfinder:
    def __init__(self, maze):
        self.maze = maze
        self. possible_steps = []
        self.tried_positions = []
        assert len(set([len(row) for row in self.maze])) == 1, 'all rows of the maze need to have the same length'
        self.dim = [len(self.maze), len(self.maze[0])]
        self.start = self.get_start()
        self.end = self.get_end()

    def ispath(self):
        n_row, n_col = self.start
        while not (n_row == self.end[0] and n_col == self.end[1]):
            self.tried_positions.append((n_row, n_col))

            current_possible_steps = self.check_directions(n_row, n_col)
            current_possible_steps = [step for step in current_possible_steps if step not in self.tried_positions]
            self.possible_steps.extend(current_possible_steps)

            if not self.possible_steps:
                return False

            n_row, n_col = self.possible_steps.pop()

        return True

    def check_directions(self, n_row, n_col):
        steps = []
        for step in [-1, 1]:
            if 0 <= n_col + step < self.dim[1]:
                field = self.maze[n_row][n_col + step]
                if field != 'w':
                    steps.append((n_row, n_col + step))

            if 0 <= n_row + step < self.dim[0]:
                field = self.maze[n_row + step][n_col]
                if field != 'w':
                    steps.append((n_row + step, n_col))
        return steps

    def get_start(self):
        return self._get_pos('s')

    def get_end(self):
        return self._get_pos('e')

    def _get_pos(self, pos_type):
        for n_row in range(self.dim[0]):
            for n_col in range(self.dim[1]):
                if self.maze[n_row][n_col] == pos_type:
                    return n_row, n_col
        print(f'{pos_type} not found')




from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.properties import StringProperty

from src.simple_pathfinder import SimplePathfinder


class GridCell(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.color = (0, 0, 0, 1)
        self.font_size = 40
        self.background_color = (1, 1, 1, 1)
        self.text = ''

    def on_press(self):
        self.text = self.parent.parent.set_state

    def on_text(self, *args):
        if self.text == 'start':
            self.background_color = (1, 0, 1, 1)
        elif self.text == 'end':
            self.background_color = (1, 0, 0, 1)
        elif self.text == 'wall':
            self.background_color = (0, 1, 0, 1)
        else:
            self.background_color = (1, 1, 1, 1)


class Grid(GridLayout):
    grid = ListProperty([0, 1, 1, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 10
        self.cols = 10
        self.cells = []

        for i in range(self.rows*self.cols):
            cell = GridCell()
            cell.id = str(i)
            cell.bind(on_press=self.change_all_cells)
            self.add_widget(cell)
            self.cells.append(cell)

    def change_all_cells(self, *args):
        if self.parent.set_state == 'start' or self.parent.set_state == 'end':
            for cell in self.cells:
                if cell.text == self.parent.set_state:
                    cell.text = ''

    def get_maze(self):
        maze = []
        translate = {'start': 's',
                     'end': 'e',
                     'wall': 'w',
                     '': '.'}
        for row in range(0, self.rows*self.rows, self.rows):
            tmp_row = []
            for col in range(self.cols):
                spot = translate[self.cells[row+col].text]
                tmp_row.append(spot)
            maze.append(''.join(tmp_row))
        return maze

    def visualize_tried_pos(self, finder):
        for idx, pos in enumerate(finder.tried_positions):
            row = pos[0] * finder.dim[0]
            col = pos[1]
            self.cells[row+col].text = str(idx)


class Buttons(BoxLayout):
    pass


class Board(GridLayout):
    set_state = StringProperty('start')

    def set_start(self):
        self.set_state = 'start'
        self.ids.start_button.background_color = (1, 0, 0, 1)
        self.ids.end_button.background_color = (0, 0, 1, 1)
        self.ids.wall_button.background_color = (0, 0, 1, 1)

    def set_end(self):
        self.set_state = 'end'
        self.ids.start_button.background_color = (0, 0, 1, 1)
        self.ids.end_button.background_color = (1, 0, 0, 1)
        self.ids.wall_button.background_color = (0, 0, 1, 1)

    def set_wall(self):
        self.set_state = 'wall'
        self.ids.start_button.background_color = (0, 0, 1, 1)
        self.ids.end_button.background_color = (0, 0, 1, 1)
        self.ids.wall_button.background_color = (1, 0, 0, 1)

    def clear(self):
        self.ids.start_button.background_color = (0, 0, 1, 1)
        self.ids.end_button.background_color = (0, 0, 1, 1)
        self.ids.wall_button.background_color = (0, 0, 1, 1)
        for cell in self.ids.grid.cells:
            cell.text = ''

    def solve(self):
        # TODO: error if no start or no end
        maze = self.ids.grid.get_maze()
        # TODO: visualization
        finder = SimplePathfinder(maze)
        # TODO: popup
        print(finder.ispath())
        self.ids.grid.visualize_tried_pos(finder)


class PathFinderApp(App):
    def build(self):
        return Board()




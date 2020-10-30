from src.simple_pathfinder import SimplePathfinder

test_maze_1 = ['s..',
               '...',
               '..e']

test_maze_2 = ['...',
               '.s.',
               '...',
               'e..']

test_maze_3 = ['...',
               '.s.',
               'www',
               'e..']


def test_get_start():
    finder = SimplePathfinder(test_maze_1)
    y, x = finder.get_start()
    assert (y, x) == (0, 0)

    finder = SimplePathfinder(test_maze_2)
    y, x = finder.get_start()
    assert (y, x) == (1, 1)


def test_get_end():
    finder = SimplePathfinder(test_maze_1)
    y, x = finder.get_end()
    assert (y, x) == (2, 2)

    finder = SimplePathfinder(test_maze_2)
    y, x = finder.get_end()
    assert (y, x) == (3, 0)


def test_check_directions():
    finder = SimplePathfinder(test_maze_1)
    steps = finder.check_directions(0, 0)
    possible_steps = [(1, 0), (0, 1)]
    assert len(possible_steps) == len(steps) and set(steps) == set(possible_steps)

    steps = finder.check_directions(1, 1)
    possible_steps = [(1, 0), (0, 1), (1, 2), (2, 1)]
    assert len(possible_steps) == len(steps) and set(steps) == set(possible_steps)


def test_ispath():
    finder = SimplePathfinder(test_maze_1)
    assert finder.ispath()

    finder = SimplePathfinder(test_maze_2)
    assert finder.ispath()

    finder = SimplePathfinder(test_maze_3)
    assert not finder.ispath()
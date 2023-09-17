import project

def test_create_board():
    assert (project.create_board(3) == [[0, 0, 0], [0, 0, 0],[0, 0, 0]]).all()

def test_populate_board():
    board1 = project.create_board(3)
    assert (project.populate_board(board1, 3, 5) == [[0, 1, 1], [0, 1, 1],[0, 1, 0]]).all()
    board2 = project.create_board(3)
    assert (project.populate_board(board2, 3, 3) == [[0, 0, 0], [0, 1, 1],[0, 1, 0]]).all()

def test_find_path():
    board = project.create_board(3)
    assert project.find_path(board, (0,0), (2, 2)) == ([0, 1, 2], [0, 1, 2])


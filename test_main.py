import main


def test_alive():
    "Checking for alive cell"
    theboard = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
    result = [[True, False, False],
              [False, True, False],
              [False, False, True]]
    assert main.alive(theboard[0][0]) == result[0][0]
    assert main.alive(theboard[1][0]) == result[1][0]
    assert main.alive(theboard[2][0]) == result[2][0]
    assert main.alive(theboard[1][1]) == result[1][1]
    assert main.alive(theboard[2][1]) == result[2][1]


def test_neighbours():
    theboard = [[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]]
    assert main.neighbours(theboard, 0, 0) == 2
    assert main.neighbours(theboard, 1, 1) == 2
    assert main.neighbours(theboard, 2, 1) == 1


def test_rules():
    "Checking for rules are correctly applied"
    theboard = [[0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
    result = [[0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert main.rules(theboard) == result


def test_rules_block():
    theboard = [[0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
                
    result = [[0, 0, 0, 0, 0],[0, 1, 1, 0, 0],[0, 1, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
    assert main.rules(theboard) == result


def test_display():
    #Checking display with given characters
    theboard = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    result = '\u25E6 \u25E6 \u25E6\n\n\u25B2 \u25B2 \u25B2\n\n\u25E6 \u25E6 \u25E6'
    assert main.display(theboard) == result
"""
Isaam Shah
Project 2, part 2
"""

import pytest
from main import Connect4


@pytest.fixture
def game():
    return Connect4()


@pytest.mark.parametrize("vertical", [[(5, 0), (4, 0), (3, 0), (2, 0)]])
def test_check_win_vertical(game, vertical):
    for r, c in vertical:
        game.board[r][c] = 'O'
    assert game.check_win('O') is True


@pytest.mark.parametrize("diagonal", [[(5, 0), (4, 1), (3, 2), (2, 3)]])
def test_check_win_diagonal_up_right(game, diagonal):
    for r, c in diagonal:  
        game.board[r][c] = 'X'
    assert game.check_win('X') is True


@pytest.mark.parametrize("vertical2", [[(5, 0), (4, 0), (3, 0)]])
def test_no_win_vertical(game, vertical2):
    # vertical no win check
    for r, c in vertical2:
        game.board[r][c] = 'X'
    assert game.check_win('X') is False


@pytest.mark.parametrize("diagonal2", [[(5, 0), (4, 1), (3, 2)]])
def test_no_win_diagonal_up_right(game, diagonal2):
    # diagonal no win check
    for r, c in diagonal2:
        game.board[r][c] = 'O'
    assert game.check_win('O') is False


"""
    Document the results:

    Test vertical checks for 4 in a row vertically: 
        Column 0 for Rows 5, 4, 3, 2 
    if 'O' found in those cells then returns True that it's a win condition

    Test diagonal checks for 4 in a row ascending diagonal (upward right slant):
        Column 0 for row 5 
        Column 1 for row 4 
        Column 2 for row 3
        Column 3 for row 2 
    if 'X' found in those cells then returns True that it's a win condition

    Test for no win vertical checks that there's no 4 chips in column yet:
        Column 0 for Rows 5, 4, 3
    Since the chips are in three rows on column 0, it will return False as intended that it's not a win condition
    
    Test for no win diagonal checks that there's no 4 in a row ascending diagonally:
        Column 0 for row 5 
        Column 1 for row 4 
        Column 2 for row 3
    Since only three chips were found to ascend diagonally, it will return False as intended that it's not a win condition

    Result: 
    4 passed, 0 failed. No bugs found in the vertical or diagonal (up-right) logic of check_win, and no false wins when only 3 chips are in a line.

    Issue:
    One issue I had during testing was that I checked the win condition without placing the chips on the board first, and the test failed.
"""

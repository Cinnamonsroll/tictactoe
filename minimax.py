import math
from board import flatten
import copy
def get_available_states(grid):
    available_points = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                available_points.append({
                    "x": i,
                    "y": j
                })
    return available_points
def has_won(grid, player):
          all_possible_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
          win = None
          flattened_board = flatten(grid)
          for w in all_possible_wins:
              if len(list(filter(lambda x: x == player, [flattened_board[index - 1] for index in w]))) == 3: win = True
          return win
def minimax(grid, turn, depth, is_max):
     current_spots = get_available_states(grid)
     if has_won(grid, 1):
         return -10
     elif has_won(grid, 2):
         return 10
     elif len(current_spots) == 0:
         return 0
     best_score = -math.inf if is_max else math.inf
     for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                grid[i][j] = 2 if is_max else 1
                score = minimax(grid, turn, depth + 1, not is_max)
                grid[i][j] = 0
                best_score = max(score, best_score) if is_max else min(score, best_score)
     return best_score
def best_move(grid, turn):
    best_score = -math.inf
    moves = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                grid[i][j] = 2
                score = minimax(grid, turn, 0, False)
                grid[i][j] = 0
                if score > best_score:
                    best_score = 0
                    moves.append({
                    "x": i,
                    "y": j
                })
    return moves[len(moves) - 1]
    
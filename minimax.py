import math
from board import flatten

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
    flattened_board = flatten(grid)
    for w in all_possible_wins:
        if all(flattened_board[index - 1] == player for index in w):
            return True
    return False

def minimax(grid, turn, depth, is_max, alpha, beta):
    if has_won(grid, 1):
        return -10
    elif has_won(grid, 2):
        return 10
    elif len(get_available_states(grid)) == 0:
        return 0

    best_score = -math.inf if is_max else math.inf
    current_spots = get_available_states(grid)

    for spot in current_spots:
        i, j = spot['x'], spot['y']
        grid[i][j] = 2 if is_max else 1
        score = minimax(grid, turn, depth + 1, not is_max, alpha, beta)
        grid[i][j] = 0

        if is_max:
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
        else:
            best_score = min(score, best_score)
            beta = min(beta, best_score)

        if beta <= alpha:
            break

    return best_score

def best_move(grid, turn):
    best_score = -math.inf
    best_moves = []
    available_spots = get_available_states(grid)

    for spot in available_spots:
        i, j = spot['x'], spot['y']
        grid[i][j] = 2
        score = minimax([row[:] for row in grid], turn, 0, False, -math.inf, math.inf)
        grid[i][j] = 0

        if score > best_score:
            best_score = score
            best_moves = [{'x': i, 'y': j}]
        elif score == best_score:
            best_moves.append({'x': i, 'y': j})

    return best_moves[-1]
def flatten(t):
            return [item for sublist in t for item in sublist]
def full_board(grid):
            return len([x for x in flatten(grid) if x in [1, 2]]) == 9
def has_won(grid):
          all_possible_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
          win = None
          flattened_board = flatten(grid)
          for k in [1, 2]:
              for w in all_possible_wins:
                  if len(list(filter(lambda x: x == k, [flattened_board[index - 1] for index in w]))) == 3: win = True
          return win
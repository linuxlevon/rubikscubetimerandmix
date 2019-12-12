import random
import timer

moves = ['F', 'R', 'U', 'L', 'B', 'D', "F'", "R'", "U'", "L'", "B'", "D'", 'F2', 'R2', 'U2', 'L2', 'B2', 'D2']


rand_items = [moves[random.randrange(len(moves))]
              for item in range(9)]

print(rand_items)

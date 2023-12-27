import random
import scipy.stats as st

def roll_dice(*args: int) -> str:
  counted_val = []
  for i in range(1_000_000):
    val = 0
    for dice in args:
      val += random.randint(1,dice)
    counted_val.append(val)
  
  prob_list = []
  for i in range(1*len(args), sum(args)+1):
    prob_list.append((i, counted_val.count(i) * 100 / 1_000_000))

  print(f'{"VALUE":5}|{"RESULT":5}')
  for val, res in prob_list:
    print(f'{val:5}|{res:5.2f}% | ', '='*(int(res // .2)))


roll_dice(4,6,6)



import random
import time

def waiting_game() -> None: 
  target_time = random.randint(2,10)

  input(f'''
Your target time is {target_time} seconds.
 --- Press Enter to Begin --- ''')
  begining = time.perf_counter()

  input(f'''
... Press Enter again after {target_time} seconds ...''')
  end = time.perf_counter()

  elapsed_time = end-begining
  print(f'Elapsed time: {elapsed_time:.3f} seconds')
  hint = 'Congrats! You were just on time!'
  if (elapsed_time - target_time) > 0:
    hint = f'{abs(elapsed_time - target_time):.3f} seconds too slow'
  elif (elapsed_time - target_time) < 0:
    hint = f'{abs(elapsed_time - target_time):.3f} seconds too fast'
  print(hint)

waiting_game()

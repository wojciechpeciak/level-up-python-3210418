import sched
import time

def schedule_function(event_time: int, func: any, *args: any) -> None:
  scheduler = sched.scheduler(time.time, time.sleep)
  event = scheduler.enterabs(event_time, 0, func, args)
  print(f'{func.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
  scheduler.run()


schedule_function(time.time()+2, print, 'Hello from the future!')

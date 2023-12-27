from w_schedule_function import schedule_function
import playsound
import time

def alarm_set(target_time: str, audio_path: str, msg: str) -> None:
  trgt_time = time.mktime(time.strptime(target_time, '%d/%m/%y %H:%M:%S'))
  schedule_function(
    trgt_time, alarm_activate, 
    audio_path,
    msg)
  

def alarm_activate(audio_path: str, msg: str) -> None:
  playsound.playsound(audio_path, False)
  print(msg)


alarm_set(
  '27/12/23 13:11:59',
  '/workspaces/level-up-python-3210418/src/07 Schedule a Function/Email-02.wav',
  'Test time!')
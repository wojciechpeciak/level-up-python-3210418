import yagmail

def send_email(rcv_email: str, msg_body: str, subject: str) -> None:
  with yagmail.SMTP('login', 'pass') as yag:
    yag.send(rcv_email, subject, msg_body)


content = '''
Hi Wojtek!
The task is done. Email form python.'''
rcv = 'peciak@gmail.com'
org = 'test@test.pl'
sbj = 'Email form python'

send_email(rcv, content, sbj)
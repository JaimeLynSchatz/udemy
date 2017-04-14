import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)  # server and port number
type(conn)

print(conn)
print(conn.ehlo())

print(conn.starttls())
print conn.login('gmail address', 'password')

conn.sendmail('from email address', 'to email address', 'Subject: Here's the subject\n\nDear Al, So long and thanks for all the fish.\n\n-Al')


# Try it with Yahoo after you set up a dummy Yahoo account
import smtplib
fromMy = 'yourMail@yahoo.com' # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
to  = 'SomeOne@Example.com'
subj='TheSubject'
date='2/1/2010'
message_text='Hello Or any thing you want to send'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )

username = str('yourMail@yahoo.com')  
password = str('yourPassWord')  

try :
    server = smtplib.SMTP("smtp.mail.yahoo.com",587)
    server.login(username,password)
    server.sendmail(fromMy, to,msg)
    server.quit()    
    print 'ok the email has sent '
except :
    print 'can\'t send the Email'



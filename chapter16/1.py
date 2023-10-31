import smtplib

# SMTP - протокол отправки писем
smtp_obj = smtplib.SMTP('smtp.bk.ru', 587)
print(type(smtp_obj))


print(smtp_obj.ehlo())
print(smtp_obj.starttls())

print(smtp_obj.login('issadasd95@bk.ru', 'my_password'))

smtp_obj.sendmail('issadasd95@bk.ru', ['issadasd95@bk.ru', 'test@gmail.com'], \
                  'Subject: So long. \nDear Alice, so long and thanks for all the fish. \
                    Sincerely, Bob')

# разрыв соединения
smtp_obj.quit()


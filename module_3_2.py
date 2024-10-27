def send_email(message, recipient, sender="university.help@gmail.com"):
    a = 0
    for i in range(len(recipient)):
        if recipient[i] == '@':
            a +=1
    if a == 1 and (recipient[-3:] == '.ru' or recipient[-4:] == '.com' or recipient[-4:] == '.net') :
        pass
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    b = 0
    for i in range(len(sender)):
        if sender[i] == '@':
            b +=1
    if b == 1 and (sender[-3:] == '.ru' or sender[-4:] == '.com' or sender[-4:] == '.net') :
        pass
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email()
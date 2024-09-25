def send_email(message, recipient, sender = 'university.help@gmail.com'):
#проверяем содержание заданых переменные на наличие @ и окончание переданых строк через endswith
    name_recipient = '@' in recipient and (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'))
    name_sender = '@' in sender and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))
    if name_recipient == name_sender: # сравниваем переменные
        if recipient == sender:       # сравниваем переданые аргументы
            print('Нельзя отправить письмо самому себе ! ')
        else:
            if sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}! ') #выводим сравненые переменные

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')




#Пункты задачи:
##Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
##Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
#Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
##Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
# "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
#В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
#Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.


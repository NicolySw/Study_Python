"""
    Задача "Рассылка писем":
    Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же
    пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить
    его в редких случаях.
    Попробуем реализовать функцию с подробной логикой.
"""


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    """
    Проверка на корректность e-mail отправителя и получателя.
    Проверка на отправку самому себе.
    Проверка на отправителя по умолчанию.
    """
    variants = ('.com', '.ru', '.net')
    if not (recipient.endswith(variants) and sender.endswith(variants) and '@' in recipient and '@' in sender):
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    else:
        if sender == recipient:
            return "Нельзя отправить письмо самому себе!"
        else:
            if sender == "university.help@gmail.com":
                return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
            else:
                return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))

# Ожидаемый ответ:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!


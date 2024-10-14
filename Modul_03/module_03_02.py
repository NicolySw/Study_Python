"""
    Задача "Рассылка писем":
    Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же
    пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить
    его в редких случаях.
    Попробуем реализовать функцию с подробной логикой.
"""


def send_email(message, recipient, *, sender="university.help@gmail.ru"):
    """
    Проверка на корректность e-mail отправителя и получателя.
    Проверка на отправку самому себе.
    Проверка на отправителя по умолчанию.
    """
    variants = ('.com', '.ru', '.net')
    if not (recipient.endswith(variants) and sender.endswith(variants) and '@' in recipient and '@' in sender):
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    if sender == recipient:
        return "Нельзя отправить письмо самому себе!"
    if recipient == "university.help@gmail.com":
        return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
    else:
        return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'


print(send_email("mes", "university.helpgmail.ru"))

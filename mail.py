def send_email(message, recipient,sender = "university.help@gmail.com"):
    if ('@' not in recipient or '@' not in sender or not recipient.endswith((".com", ".ru", ".net"))
            or not sender.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('messagje','university.help@gmail.com','urban.teacher@mail.uk')
send_email('messagje','university.help@gmail.com')
send_email('messagje','urban.info@gmail.com')
send_email('messagje','urban.info@gmail.co')
send_email('messagje','urban.info@gmail.com')
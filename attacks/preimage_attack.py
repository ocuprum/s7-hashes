import random
import string

# Послідовно додаємо до повідомлення натуральні числа
def pa1(message, message_hash, hash_func, size=4):

    if len(message_hash) < size:
        return False
    short_message_hash = message_hash[-size:]

    number = 1
    new_hash = hash_func(message + str(number))[-size:]

    while new_hash != short_message_hash:
        number += 1
        new_hash = hash_func(message + str(number))[-size:]
    
    return number

# Міняємо символ на випадковій позиції на новий, випадково обраний, символ
def pa2(message, message_hash, hash_func, size=4):
    if len(message_hash) < size:
        return False
    short_message_hash = message_hash[-size:]

    pos = random.randint(0, len(message)-1)
    new_sym = random.choice(string.printable)
    message = message[:pos] + new_sym + message[pos+1:]
    new_hash = hash_func(message)[-size:]

    while new_hash != short_message_hash:
        pos = random.randint(0, len(message)-1)
        new_sym = random.choice(string.printable)
        message = message[:pos] + new_sym + message[pos+1:]
        new_hash = hash_func(message)[-size:]

    return message
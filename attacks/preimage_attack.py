import random
import string

chars = list(string.printable)
chars.remove(',')
chars.remove('\x0b')
chars.remove('\x0c')

# Послідовно додаємо до повідомлення натуральні числа
def pa1(message, message_hash, hash_func, size=4):
    messages, hashes = [], []

    if len(message_hash) < size:
        return False
    short_message_hash = message_hash[-size:]

    number = 1
    messages.append(message + str(number))
    nhash = hash_func(message + str(number))
    hashes.append(nhash)
    new_hash = nhash[-size:]

    while new_hash != short_message_hash:
        number += 1
        messages.append(message + str(number))
        nhash = hash_func(message + str(number))
        hashes.append(nhash)
        new_hash = nhash[-size:]
    
    return number, messages, hashes

# Міняємо символ на випадковій позиції на новий, випадково обраний, символ
def pa2(message, message_hash, hash_func, size=4):
    messages, hashes = [], []
    if len(message_hash) < size:
        return False
    short_message_hash = message_hash[-size:]

    pos = random.randint(0, len(message)-1)
    new_sym = random.choice(chars)

    message = message[:pos] + new_sym + message[pos+1:]
    messages.append(message)
    nhash = hash_func(message)
    hashes.append(nhash)
    new_hash = nhash[-size:]

    count = 1

    while new_hash != short_message_hash:
        pos = random.randint(0, len(message)-1)
        new_sym = random.choice(chars)

        message = message[:pos] + new_sym + message[pos+1:]
        messages.append(message)
        nhash = hash_func(message)
        hashes.append(nhash)
        new_hash = nhash[-size:]

        count += 1

    return count, messages, hashes
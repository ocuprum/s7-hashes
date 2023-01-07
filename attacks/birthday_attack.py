import random
import string

chars = list(string.printable)
chars.remove(',')
chars.remove('\x0b')
chars.remove('\x0c')

def ba1(message, message_hash, hash_func, size=8):
    if len(message_hash) < size - 1:
        return False
    
    messages, hashes_lst = [], []
    hashes = {}
    number = 0

    new_hash = message_hash[-size:]
    hashes[new_hash] = message

    while True:
        number += 1
        new_message = message + str(number)
        messages.append(new_message)

        nhash = hash_func(new_message)
        hashes_lst.append(nhash)
        new_hash = nhash[-size:]

        hash_preimage = hashes.get(new_hash, [])
        
        if hash_preimage:
            return number, messages + [hash_preimage + [new_message]], hashes_lst

        hashes[new_hash] = hash_preimage + [new_message]

def ba2(message, message_hash, hash_func, size=8):
    if len(message_hash) < size - 1:
        return False
    
    messages, hashes_lst = [], []
    hashes = {}

    new_hash = message_hash[-size:]
    hashes[new_hash] = {message}

    count = 0
    while True:
        pos = random.randint(0, len(message)-1)
        new_sym = random.choice(string.printable)
        message = message[:pos] + new_sym + message[pos+1:]
        messages.append(message)

        nhash = hash_func(message)
        hashes_lst.append(nhash)
        new_hash = nhash[-size:]

        hashes[new_hash] = hashes.get(new_hash, set()) | {message}
        
        count += 1

        if len(hashes[new_hash]) == 2:
            return count, messages + [hashes[new_hash]], hashes_lst
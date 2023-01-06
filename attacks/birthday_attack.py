import random
import string

def ba1(message, message_hash, hash_func, size=8):
    
    if len(message_hash) < size - 1:
        return False
    
    hashes = {}
    number = 1

    new_hash = message_hash[-size:]
    hashes[new_hash] = message

    while True:
        number += 1
        new_message = message + str(number)
        new_hash = hash_func(new_message)[-size:]

        hash_preimage = hashes.get(new_hash, [])
        
        if hash_preimage:
            return hash_preimage + [new_message]

        hashes[new_hash] = hash_preimage + [new_message]

def ba2(message, message_hash, hash_func, size=8):
    if len(message_hash) < size - 1:
        return False
    
    hashes = {}

    new_hash = message_hash[-size:]
    hashes[new_hash] = {message}

    while True:
        pos = random.randint(0, len(message)-1)
        new_sym = random.choice(string.printable)
        message = message[:pos] + new_sym + message[pos+1:]
        new_hash = hash_func(message)[-size:]

        hashes[new_hash] = hashes.get(new_hash, set()) | {message}
        
        if len(hashes[new_hash]) == 2:
            return hashes[new_hash]
    
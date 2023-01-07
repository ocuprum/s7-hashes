from hashlib import blake2b
from attacks.preimage_attack import pa1, pa2
from attacks.birthday_attack import ba1, ba2
from writer.writer import writer

hash_func = lambda message: blake2b(bytes(message, 'utf-8')).hexdigest()

writer('pa1', pa1, hash_func)
writer('pa2', pa2, hash_func)
writer('ba1', ba1, hash_func)
writer('ba2', ba2, hash_func)
import string as str
import random
s="Aksh" 
def generate_code(l=3):
    characters = str.ascii_letters+str.digits
    return ''.join((random.choice(characters)) for _ in range(l))
re = []
def coder(b):
    for a in b:
        re.append(a[::-1])
    return re

def final(s):
    return generate_code()+s+generate_code()

                   




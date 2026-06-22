import string as str
import random
s="Aksh" 
def generate_code(l=3):
    characters = str.ascii_letters+str.digits
    return ''.join((random.choice(characters)) for _ in range(l))

re = []
def coder(a):
   return a[::-1]

def final(s):
    return generate_code()+s+generate_code()
if __name__=="__main__":
    print(final(s))
                   




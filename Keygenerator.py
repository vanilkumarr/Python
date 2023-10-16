import string
import random

char= list(string.ascii_lowercase + string.ascii_uppercase + string.digits+ '!@#$%^&*()_+')
random.shuffle(char)
key=''
for i in range(16):
    key+=random.choice(char)
print(key)
<<<<<<< HEAD
import string
import random

char= list(string.ascii_lowercase + string.ascii_uppercase + string.digits+ '!@#$%^&*()_+')
random.shuffle(char)
key=''
for i in range(16):
    key+=random.choice(char)
=======
import string
import random

char= list(string.ascii_lowercase + string.ascii_uppercase + string.digits+ '!@#$%^&*()_+')
random.shuffle(char)
key=''
for i in range(16):
    key+=random.choice(char)
>>>>>>> 09e140885114317c22ba6a5e030c255502b6aed0
print(key)
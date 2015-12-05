import hashlib

secretkey = 'iwrupvqb'

# init md5 object with secret key
m = hashlib.md5()
m.update(secretkey.encode('utf-8'))

counter = 0
while True:
    # start always with same input
    inp = m.copy()
    inp.update(str(counter).encode('utf-8'))

    hashed = inp.hexdigest()
    if (hashed[0:5] == '00000'):
        break
    counter += 1
print(counter)

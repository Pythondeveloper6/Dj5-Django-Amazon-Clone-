import random



def generate_code(length=8):
    data = '012345656789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''.join(random.choice(data) for x in range(length))
    return code 
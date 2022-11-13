import random
import string

def get_random_password() -> str:
    alph = string.ascii_uppercase + string.ascii_lowercase + string.digits
    n = 8
    password = "".join(random.sample(alph, n))
    return password


print(get_random_password())

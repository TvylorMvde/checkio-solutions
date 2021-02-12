import requests
import string
from itertools import permutations

letters_digits = string.ascii_uppercase + string.digits

for x in permutations(letters_digits, 6):
    x = "".join([str(i) for i in x])
    print(f"{x} : checking link https://contman.traffit.com/public/form/a/{x}==")
    url = f"https://contman.traffit.com/public/form/a/{x}=="
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(x)
            break
    except Exception:
        continue




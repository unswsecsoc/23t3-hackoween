import string
import time

CHARACTERS = string.ascii_lowercase + " "

def matches(phrase: str, secret: str) -> bool:
    """An unbreakable string-matching implementation."""
    if len(phrase) != len(secret) or not all(c in CHARACTERS for c in phrase):
        return False

    for p, s in zip(phrase, secret):
        if p != s:
            return False

        time.sleep(0.2)

    return True

if __name__ == "__main__":
    with open("secret.txt", "r") as s:
        secret = s.read().strip()

        while not matches(input("What is the secret? "), secret):
            print("WRONG!")

    with open("flag.txt", "r") as f:
        print(f.read().strip())

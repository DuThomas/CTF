import hashlib
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <username>")
    sys.exit(1)

username = sys.argv[1]


def find_number(prefix):
    number = 0
    while True:
        candidate = f"{prefix}-{number}\n"
        hashed = hashlib.sha256(candidate.encode()).hexdigest()
        if (
            hashed[0] == "0"
            and hashed[1] == "0"
            and hashed[2] == "0"
            and hashed[3] == "0"
            and hashed[4] == "0"
            and hashed[5] == "0"
        ):
            return candidate
        number += 1


while True:
    nonce = input("Enter the nonce: ")
    print(find_number(f"{username}-{nonce}"))

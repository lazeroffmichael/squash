def encryptRot(message, rot):
    res = ""
    for c in message:
        if c == " ":
            res += " "
        else:
            res += chr(ord("a") + (ord(c) - ord("a") + rot) % 26)
    return res


def decryptRot(message, rot):
    res = ""
    for c in message:
        if c == " ":
            res += " "
        else:
            res += chr(ord("a") + (ord(c) - ord("a") - rot) % 26)
    return res


if __name__ == "__main__":
    while True:
        r = int(input("Enter the rotation amount: "))
        res = input("Enter a message to encrypt: ")
        print("")
        encrypted = encryptRot(res, r)
        print("Encrypted: " + encrypted)
        print("Decrypted: " + decryptRot(encrypted, r))
        print("")

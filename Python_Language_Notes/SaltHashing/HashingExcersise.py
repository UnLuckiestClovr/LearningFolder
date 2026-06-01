import hashlib as hl # Cannot Select the Hashing Algorithm through Bcrypt


print('Ctrl+C to End Application')

while(True):
    inputData = input("Input Data to be Hashed: ")
    hashAlgo = input("Input Format to be Used [SHA1, SHA256, SHA512, MD5]: ")

    def hashSHA256(input: str):
        # Converts Str input into Bytes then hashes it, finally returns it in hexadecimal values.
        return hl.sha256(str(input).encode()).hexdigest()

    def hashSHA1(input: str):
        # Converts Str input into Bytes then hashes it, finally returns it in hexadecimal values.
        return hl.sha1(str(input).encode()).hexdigest()

    def hashSHA512(input: str):
        # Converts Str input into Bytes then hashes it, finally returns it in hexadecimal values.
        return hl.sha512(str(input).encode()).hexdigest()

    def hashMD5(input: str):
        # Converts Str input into Bytes then hashes it, finally returns it in hexadecimal values.
        return hl.md5(str(input).encode()).hexdigest()

    match hashAlgo:
        case 'SHA1':
            print(hashSHA1(inputData))
        case 'SHA256':
            print(hashSHA256(inputData))
        case 'SHA512':
            print(hashSHA512(inputData))
        case 'MD5':
            print(hashMD5(inputData))
        case _:
            pass

import hashlib

message = input(str("Phrase to hash: "))

print(hashlib.sha256(message.encode('utf-8')).hexdigest())


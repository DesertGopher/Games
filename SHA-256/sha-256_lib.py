import hashlib

message = input(str("Phrase to hash: "))

hashed_message = hashlib.sha256(message.encode('utf-8')).hexdigest()
print(hashed_message)

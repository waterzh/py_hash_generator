import hashlib

origin_str = input("Please enter origin string:")

salt = input("Please enter salt string:")
hash_object = hashlib.sha256((origin_str + salt).encode())
hash_str = hash_object.hexdigest()

print("Origin string:", origin_str)
print("Hash string:", hash_str)
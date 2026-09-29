import base64

def encrypt_data(data):
    encoded_data = base64.b64encode(data.encode())
    return encoded_data.decode()

def decrypt_data(data):
    decoded_data = base64.b64decode(data.encode())
    return decoded_data.decode()

print("=== Data Encryption and Decryption Tool ===")

text = input("Enter data: ")

# Encryption
encrypted = encrypt_data(text)
print("Encrypted data:", encrypted)

# Decryption
decrypted = decrypt_data(encrypted)
print("Decrypted data:", decrypted)

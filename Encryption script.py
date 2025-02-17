#A SCript that encrypts and decrypts 

from cryptography.fernet import Fernet

#Generate Encryption key

key = Fernet.generate_key()
cipher = Fernet(key)

#Encryption

message="I once tried to save a girl but instead she killed me. do i regret it? yes i do"
encrypted_message = cipher.encrypt(message.encode())

#decrypt 
decrypted_message = cipher.decrypt(encrypted_message).decode()

#Display results

print(f"Orginal: {message}")
print(f"cipher text: {encrypted_message}")
print(f"decrypted: {decrypted_message}")


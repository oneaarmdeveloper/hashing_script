import hashlib

def hash_password(password):
    # Convert string to bytes
    hash_object = hashlib.sha256(password.encode())
    
    # Get the hexadecimal representation
    return hash_object.hexdigest()
    
password = "passwordexample2345"
hashed_password = hash_password(password)

# Verifying if they match
verify_password = input("Enter your password here: ")

# Hash the input and compare
if hash_password(verify_password) != hashed_password:
    print("Login denied!")
else:
    print("Super! Access granted.")

    
 

---
title: "Payload Encryption"
linkTitle: "Payload Encryption"
tags: [advanced, integration, encryption]
categories: ["Knowledge Base"]
weight: 222
description: >-
     Secure Inter-Service Communication With Payload Encryption.
---

### Implementing Encrypted Payloads in FX Platform Services

In environments like the FX platform, where services exchange data over internal networks protected by TLS, there still exists a need for additional security measures. Specifically, there are scenarios where the confidentiality of certain payload parameters must be maintained, even from other developers within the platform. 

To address this, encrypting specific attributes or entire data structures within payloads before transmission is a practical solution. This process relies on AES symmetric encryption, where both encryption and decryption are performed using the same secret key.

#### Steps for AES Symmetric Encryption

1. **Key Generation**: The first step involves generating a 16-byte (128-bit) AES key. This key size is chosen for its balance between security and computational efficiency.

2. **Key Distribution**: The AES key must then be securely shared with the receiving service(s). This step is crucial and requires secure methods of transmission to ensure that only authorized recipients have access to the key.

3. **Agreement on Encryption Scope**: The sending and receiving services need to agree on which data within the payload will be encrypted. This could include specific attributes or entire data structures, depending on the sensitivity of the information.

4. **Encryption Process**: Before sending data, the sending service encrypts the agreed-upon elements of the payload using the AES key. This step transforms the data into a format that is unreadable without the key.

5. **Decryption by Recipient**: Upon receiving the encrypted payload, the recipient service uses the AES key to decrypt the data. It is recommended that the key is stored securely, often as an environment variable or within a secure storage solution, to prevent unauthorized access.

## AES Key Generation

You can use the following code snippet to generate an AES encryption key. Alternatively you can create one on websites such as 

```python
import secrets

def generate_aes_key():
    return secrets.token_bytes(16)

# Generate the AES key
aes_key = generate_aes_key()

# Represent the key in hex format for easier readability/storage
aes_key_hex = aes_key.hex()
print(f"AES Key (hex): {aes_key_hex}")
```

## Encryption Key Storage 
For enhanced security, both the sending and receiving services must adhere to stringent key management practices. Specifically, the AES key should be securely stored and retrieved from the FX secrets management system. Under no circumstances should the key be embedded directly in `config.json` files or included within Git repositories. Storing keys in such locations significantly increases the risk of unauthorized access and potential data breaches. 

Instead, leveraging dedicated secrets management tools ensures that the key remains encrypted and accessible only to authorized services and individuals, thereby maintaining the integrity and confidentiality of the encrypted payloads.

## Payload Encryption and Decryption

The following snippet demostrates how you can decrypt strings or dicts.

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import json

def encrypt_message(message, key):
    # Generate a random IV (initialization vector)
    iv = get_random_bytes(AES.block_size)
    # Create AES cipher instance with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Encrypt the message
    # The message needs to be padded to make it a multiple of the block size
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    # The IV needs to be shared with the ciphertext; we'll prepend it to the ciphertext
    # And then encode the result to make it easy to transmit
    encrypted_message = base64.b64encode(iv + ct_bytes).decode('utf-8')
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Decode the base64 encoded message
    encrypted_message_bytes = base64.b64decode(encrypted_message)
    # Extract the IV (which we know is the first 16 bytes)
    iv = encrypted_message_bytes[:AES.block_size]
    # Extract the ciphertext
    ct = encrypted_message_bytes[AES.block_size:]
    # Create a new AES cipher instance with the key and extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext and then unpad it
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt


# Shared secret token (key) - ensure this is 16, 24, or 32 bytes long
# For this example, we're using a 16-byte (128-bit) key
secret_token = b'39b96ec8e9f303bfbb14917b232866d5'  # This should be the same on both services

# Example usage simple string value
original_message = "This is a secret message"

encrypted_message = encrypt_message(original_message, secret_token)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, secret_token)
print(f"Decrypted: {decrypted_message}")


# Example usage dict. Please note dict must be json serializable
data = {"dummy":"dummy"}
encrypted_message = encrypt_message(json.dumps(data), secret_token)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, secret_token)
print(f"Decrypted: {decrypted_message}")
```



#### Conclusion

Encrypting payloads or specific payload attributes with AES symmetric encryption provides an effective way to enhance data confidentiality in the FX platform's service-to-service communications. This method ensures that sensitive information remains protected, even in environments where multiple developers have access to the platform. 

By following the outlined steps and adhering to best practices for key management and encryption, services can maintain the integrity and confidentiality of their data exchanges.
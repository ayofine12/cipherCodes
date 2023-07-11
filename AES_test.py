from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# 키, IV 생성
aes_key = get_random_bytes(16)  # AES-128
iv = get_random_bytes(16)

# 송신 측의 cipher 객체를 생성해준다
sender_cipher = AES.new(aes_key, AES.MODE_CBC, iv)

# 평문
plaintext = input("enter: ")
print()

# padding
padded_data = pad(plaintext.encode(), AES.block_size)

# 암호화
ciphertext = sender_cipher.encrypt(padded_data)
print("ciphertext:", ciphertext)
print()

'''
송신자와 수신자 통신
'''
# 수신 측의 cipher 객체를 생성해준다
receiver_cipher = AES.new(aes_key, AES.MODE_CBC, iv)

# 복호화
padded_data = receiver_cipher.decrypt(ciphertext)

# unpadding
data = unpad(padded_data, AES.block_size)

print("Decrypted data:", data)
print()

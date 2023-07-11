from Crypto.Random import get_random_bytes
import rsa

# Bob은 공개키 / 개인키를 생성
(b_pubkey, b_privkey) = rsa.newkeys(2048)

# pubkey와 privatekey를 미리 만들었다고 가정
'''
with open('b_pubkey.pem', 'rb')as f:
    b_pubkey = rsa.PublicKey.load_pkcs1(f.read())

with open('b_privkey.pem', 'rb')as f:
    b_privkey = rsa.PrivateKey.load_pkcs1(f.read())
'''

# Alice는 AES키, IV, 그리고 MAC키 생성
a_aes_key = get_random_bytes(16)  # AES-128
a_iv = get_random_bytes(16)
a_mac_key = get_random_bytes(32)  # SHA-256

print(f'a_aes_key: {a_aes_key}')
print(f'a_iv: {a_iv}')
print(f'a_mac_key: {a_mac_key}')
print()

# 위 세개의 값들을 이어붙인다
con = a_aes_key + a_iv + a_mac_key
print(f'con: {con}')
print()

# Alice는 Bob의 공개키를 이용해 con을 암호화
encrypted_con = rsa.encrypt(con, b_pubkey)
print(f'encrypted_con: {encrypted_con}')
print()

# Bob은 Bob의 개인키를 이용해 암호화된 con을 복호화
decrypted_con = rsa.decrypt(encrypted_con, b_privkey)
print(f'decrypted_con: {decrypted_con}')
print()

# Bob이 얻게 되는 aes_key, iv, mac_key
b_aes_key = decrypted_con[:16]
b_iv = decrypted_con[16:32]
b_mac_key = decrypted_con[32:]

print(f'b_aes_key: {b_aes_key}')
print(f'b_iv: {b_iv}')
print(f'b_mac_key: {b_mac_key}')
print()
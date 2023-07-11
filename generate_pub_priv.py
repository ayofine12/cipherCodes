import rsa

(pubkey, privkey) = rsa.newkeys(2048)

with open("b_pubkey.pem", 'wb')as f:
    f.write(pubkey.save_pkcs1('PEM'))

with open("b_privkey.pem", 'wb')as f:
    f.write(privkey.save_pkcs1('PEM'))

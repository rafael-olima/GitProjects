from basic.RSA import myRSA
from basic.Encryption import myEncryption

grsa = myRSA()
print(grsa.get_private_key())
print(grsa.get_public_key())

enc = myEncryption(grsa.get_private_key(),grsa.get_public_key())


message = b"encrypted data"

cipher = enc.encrypt_file(message)
print(cipher)

original = enc.decrypt_file(cipher)
print(original)

hash = enc.generate_hash(message)
print(hash)

hash = '6c8addc760fb5a92541fdc5668675dc0a8dc9a22979482fab329daba544a9bd9'

verify = enc.verify_hash(hash,message)
print(verify)
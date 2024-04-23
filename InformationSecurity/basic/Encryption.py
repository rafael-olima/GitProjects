from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
import hashlib

class myEncryption:

    def __init__(self,private_key,public_key):
        self.__private_key = private_key
        self.__public_key = public_key

    def encrypt_file(self, file):
        block_size = 256
        encrypted_blocks = []
        offset = 0
        while offset < len(file):
            block = file[offset:offset + block_size]
            encrypted_block = self.__public_key.encrypt(
                block,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            encrypted_blocks.append(encrypted_block)
            offset += block_size
        return b''.join(encrypted_blocks)

    def decrypt_file(self,cipher):
        original = self.__private_key.decrypt(
            cipher,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original

    def signing(self,file):
        #message = b"A message I want to sign"
        signature = self.__private_key.sign(
            file,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verification_sing(self,signature,file):
        try:
            self.__public_key.verify(
                signature,
                file,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature as e:
            return False

    def generate_hash(self,file):
        hash = hashlib.sha256(file).hexdigest()
        return hash

    def verify_hash(self,hash,file):
        new_hash = hashlib.sha256(file).hexdigest()
        if hash == new_hash:
            return True
        else:
            return False


from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class myRSA:

    def __init__(self):
        self.__private_key = None
        self.__public_key = None
        self.load_keys()


    def get_private_key(self):
        return self.__private_key

    def get_public_key(self):
        return self.__public_key

    def load_keys(self):
        try:
            with open("private_key.pem", "rb") as private_key_file:
                self.__private_key = serialization.load_pem_private_key(private_key_file.read(),password=None)

            with open("public_key.pem", "rb") as public_key_file:
                self.__public_key = serialization.load_pem_public_key(public_key_file.read())
        except FileNotFoundError as fnfe:
            self.generate_keys()

    def generate_keys(self):
        self.__private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

        private_pem = self.__private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        with open("private_key.pem", 'wb') as file:
            file.write(private_pem)

        self.__public_key = self.__private_key.public_key()

        public_pem = self.__public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open("public_key.pem", 'wb') as file:
            file.write(public_pem)


grsa = myRSA()
"""

# Imprimir as chaves PEM
print("Chave Privada:")
print(private_pem.decode())
print("\nChave Pública:")
print(public_pem.decode())"""
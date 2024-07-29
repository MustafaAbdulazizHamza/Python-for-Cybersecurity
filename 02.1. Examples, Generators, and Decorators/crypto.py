from cryptography.fernet import Fernet, MultiFernet
import argparse as arg

def SaveKeys(KeyFile, k1, k2):
    with open(KeyFile, 'w') as f:
        f.write(f"{k1}\n{k2}")
def Encrypt(plaintext, KeyFile):
    k1 = Fernet.generate_key()
    k2 = Fernet.generate_key()
    SaveKeys(KeyFile, k1, k2)
    mf = MultiFernet([Fernet(k1), Fernet(k2)])
    return mf.encrypt(plaintext.encode())

argparser = arg.ArgumentParser(description="A Cryptography tool")
argparser.add_argument("-p", "--plaintext", required=True, help = "The plaintext to encrypt")
argparser.add_argument("-k", "--keys", required=True ,help="An output file to store keys")
args = argparser.parse_args()

ciphertext = Encrypt(args.plaintext, args.keys)
print(ciphertext)
import hashlib
algos = ['md5', 'sha256', "sha224", "sha3_256"]
plaintext = 'Hello'
digests = [hashlib.new(algo, plaintext.encode()).hexdigest() for algo in algos]
for digest in digests: print(digest, "\n")
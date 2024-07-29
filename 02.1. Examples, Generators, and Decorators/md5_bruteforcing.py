import hashlib, os, re, sys, argparse

def MD5_Bruteforcing(MD5_hash ,Dictionary_path):
    with open(Dictionary_path, 'r' ,errors='replace') as D:
        for password in D:
            if hashlib.md5(password.strip().encode('utf-8')).hexdigest() == MD5_hash:
                print("*{} --> {}*".format(MD5_hash, password.strip()))
                sys.exit(0)


argument = argparse.ArgumentParser(description="This tool is used to carry out md5 hash bruteforcing")
argument.add_argument('-H', '--Hash', required=True, help="The MD5 hashsum")
argument.add_argument('-D', '--Dictionary',  required=True, help="A wordlist")
args = argument.parse_args()
if not os.path.isfile(args.Dictionary):
    print("The dictionary {} you have provided does not exist".format(args.Dictionary))
    sys.exit(404)
if not re.match(r'[0-9a-fA-F]{32}$', args.Hash):
    print("The hash you have provided is not a valid MD5 hash")
    sys.exit(1)
MD5_Bruteforcing(args.Hash, args.Dictionary)
print(f"The password was not found into the provided dictionary {args.Dictionary}")
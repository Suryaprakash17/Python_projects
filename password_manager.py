from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
write_key()

def load_key():
    file = open('key.key', 'rb')
    key_1 = file.read()
    file.close()
    return key_1

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for i in f.readlines():
            data = i.rstrip()
            name, pwd = data.split('|')
            print('User:', name + ',| Password:', fer.decrypt(pwd.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input('Password:')
    with open('passwords.txt', 'a') as f:
        f.write(name+'|' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input('Would you like to add the password or view the existing password or want to quit (press q): ').lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode')
        continue
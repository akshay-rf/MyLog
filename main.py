import os
from os.path import basename
from datetime import date

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ',':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', '!':'!', "'":"'",
                    '@':'@', '#':'#', '$':'$', '%':'%', '^':'^',
                    '&':'&', '*':'*', '_':'_', '+':'+', '=':'=',
                    '[':'[', '{':'{', '}':'}', '\\':'\\', '|':'|', ';':';',
                    '"':'"', ':':':', '<':'<', '>':'>', '`':'`', '~':'~'} 

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            cipher += ' '
    
    return cipher

def write_encode():
    os.system('cls' if os.name == 'nt' else 'clear')
    file_name = str(date.today())

    if os.path.isfile(f"{file_name}.txt"):
        fill = open(f"{file_name}.txt", 'r')
        text = fill.read()
        fill.close()

        if text == '':
            with open(f"{file_name}.txt", 'w') as f:
                raw_input = input("""\nYour Log: """).upper()
                encoded_input = encrypt(raw_input)
                f.write(f"{encoded_input} ")
                f.close()
        
        else:
            while True:
                print("""\n[1] Overwrite
[2] Append
[3] Back\n""")
                try:
                    value = int(input("> "))
                    if value > 3 or value < 1:
                        print("invalid input")
                    else:
                        if value == 1:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            with open(f"{file_name}.txt", 'w') as f:
                                raw_input = input("""\nYour Log: """).upper()
                                encoded_input = encrypt(raw_input)
                                f.write(f"{encoded_input} ")
                            f.close()
                            break

                        if value == 2:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            with open(f"{file_name}.txt", 'a') as f:
                                raw_input = input("""\nYour Log: """).upper()
                                encoded_input = encrypt(raw_input)
                                f.write(f"{encoded_input} ")
                            f.close()
                            break

                        if value == 3:
                            break

                except ValueError:
                    print("numbers only!")

    else:
        with open(f"{file_name}.txt", 'w') as f:
            raw_input = input("""\nYour Log: """).upper()
            encoded_input = encrypt(raw_input)
            f.write(f"{encoded_input} ")
            f.close()


def decrypt(message): 
        message += ' '
      
        decipher = '' 
        citext = '' 
        for letter in message: 
            if (letter != ' '): 
                i = 0
                citext += letter 
      
            else: 
                i += 1

                if i == 2 : 
                    decipher += ' '
                else: 
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                    .values()).index(citext)] 
                    citext = '' 
      
        return decipher 


def read_data():
    os.system('cls' if os.name == 'nt' else 'clear')
    files = os.listdir()
    file_dict = dict()
    num = 1
    print(" ")
    dont_run = False

    if len(files) == 0:
        dont_run = True
        print("No Logs here")
    
    for i in files:
        print(f"[{num}] {i.replace('.txt', '')}")
        file_dict.__setitem__(num, i)
        num+=1
    
    file_dict.__setitem__(num, "Back")
    print(f"[{num}] Back")

    while not dont_run:
        try:
            val = int(input("\n> "))
            if val > len(files)+1:
                print("invalid input")
            else:
                file_name = file_dict[val]
                if file_name == "Back":
                    break
                else:
                    with open(file_name, 'r') as f:
                        enc_log = f.read().strip()
                        log = decrypt(enc_log)
                    f.close()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""\nYour Log:\n{log}""")
                    input("\nPress ENTER to continue")
                    break

        
        except ValueError:
            print("numbers only!")


def main_interface(usr):
    file_list = os.listdir()
    fol_ex = False
    for i in file_list:
        if i == f"{usr}'s Log":
            fol_ex = True

    if fol_ex:
        os.chdir(os.path.join(os.path.abspath(os.path.curdir),u"{}'s Log".format(usr)))
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nWELCOME {usr.upper()}​!​​​​")
            print('''\n[1] Add Log
[2] Read Log
[3] Log Out\n''')
            try:
                value = int(input("> "))
                if value > 3 or value < 1:
                    print("invalid input")
                else:
                    if value == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        write_encode()

                    if value == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        read_data()

                    if value == 3:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

            except ValueError:
                print("numbers only!")

    if not fol_ex:
        os.mkdir(f"{usr}'s Log")
        os.chdir(os.path.join(os.path.abspath(os.path.curdir),u"{}'s Log".format(usr)))

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nWELCOME {usr.upper()}​!​​​​")
            print('''\n[1] Add Log
[2] Read Log
[3] Log Out\n''')
            try:
                value = int(input("> "))
                if value > 3 or value < 1:
                    print("invalid input")
                else:
                    if value == 1:
                        write_encode()

                    if value == 2:
                        read_data()

                    if value == 3:
                        break

            except ValueError:
                print("numbers only!")        


def register(usr, pwd):
    file_lst = os.listdir()
    dir_exist = False
    for i in file_lst:
        if i == 'users':
            dir_exist = True
    
    if dir_exist:
        os.chdir(os.path.join(os.path.abspath(os.path.curdir),u'users'))
        with open(f"{usr}", 'w') as t:
            t.write(pwd)
        t.close()

    if not dir_exist:
        os.mkdir("users")
        os.chdir(os.path.join(os.path.abspath(os.path.curdir),u'users'))
        with open(f"{usr}", 'w') as t:
            t.write(pwd)
        t.close()
    print("\nuser registered\n")     


def login(usr, pwd):
    path = os.getcwd()
    fol = basename(path)

    try:
        if fol == 'users':
            file_list = os.listdir()
            main_int = False

            for i in file_list:
                if usr == i:
                    main_int = True

            if main_int:
                with open(usr, 'r') as f:
                    password = f.read()
                f.close()

                if pwd == password:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main_interface(usr)
                
                else:
                    print("\nincorrect password\n")
                    input("[ERROR] Press ENTER to continue")

            if not main_int:
                print("\nUser does not exist. Please register.\n")
                input("[ERROR] Press ENTER to continue")
        else:
            os.chdir(os.path.join(os.path.abspath(os.path.curdir),u'users'))
            file_list = os.listdir()
            main_int = False

            for i in file_list:
                if usr == i:
                    main_int = True

            if main_int:
                with open(usr, 'r') as f:
                    password = f.read()
                f.close()

                if pwd == password:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main_interface(usr)
                
                else:
                    print("\nincorrect password\n")
                    input("[ERROR] Press ENTER to continue")

            if not main_int:
                print("\nUser does not exist. Please register.\n")
                input("[ERROR] Press ENTER to continue")

    except FileNotFoundError:
        print("\nno users registered\n")
        input("[ERROR] Press ENTER to continue")
run = 0
while True:
    if run == 0:
        ogg_path = os.getcwd()
        with open("path", 'w+') as t:
            t.write(ogg_path)
            file_path = os.path.realpath(t.name)         
        t.close()

    with open(file_path, 'r') as t:
        og_path = t.read()
    t.close()
    
    os.chdir(og_path)
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''\n███    ███ ██    ██ ██       ██████   ██████  
████  ████  ██  ██  ██      ██    ██ ██       
██ ████ ██   ████   ██      ██    ██ ██   ███ 
██  ██  ██    ██    ██      ██    ██ ██    ██ 
██      ██    ██    ███████  ██████   ██████  ''')

    print("""\n[1] Register
[2] Login
[3] Quit\n""")
    try:
        value = int(input("> "))
        if value > 3 or value < 1:
            print("invalid input")
            input("[ERROR] Press ENTER to continue")
        else:
            if value == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nREGISTER:")
                username = input("\nusername: ")
                password = input("password: ")
                register(username, password)

            if value == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nLOGIN:")
                username = input("\nusername: ")
                password = input("password: ")
                login(username, password)

            if value == 3:
                break

    except ValueError:
        print("numbers only!")
        input("[ERROR] Press ENTER to continue")

    run += 1

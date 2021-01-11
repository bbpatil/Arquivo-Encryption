def Encrypt(filename, key):
		file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open(filename, "wb")
    file.write(data)
    file.close()

def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open(filename, "wb")
    file.write(data)
    file.close()

choice = ""
err = ""
while choice != 3:
    print(" ")
    print("_____________________________________________")
    print("|````````````````````````````````````````````|")
    print("|    <=======   Arquivo Locker   ======>     |")
    print("|--------------------------------------------|")
    print("|    File Encryption and Decryption Tool     |")
    print("|--------------------------------------------|")
    print("|    ********** By Shiva Teja **********     |")
    print("|____________________________________________|")
    print("``````````````````````````````````````````````")
    print("Your available options are: 1) Encrypt a file.")
    print("                            2) Decrypt a file.")
    print("                            3) Exit")
    print(" ")
    if err:
        print(err)
        print(" ")
    try:
        choice = int(input(Enter your choice: "))
        err=""
    except:
        err = "Please select from given choice."
    if choice == 1:
        logo = '''     
  ___                       _   _          
 | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _  
 | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \ 
 |___|_||_\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
        
        print(logo)
        print("")
        filename = input("Enter the filename for encryption: "))
        key = int(input("Enter a key (0-255): "))
        Encrypt(filename, key)
        print("_____________________________________________")
        print("|````````````````````````````````````````````|")
        print("|    File Encryption is done succssfully !   |")
        print("|____________________________________________|")
        print("``````````````````````````````````````````````")
        print("")
        home_menu = input("Enter 'Y' for Menu or 'N' to quit: ")
        if home_menu.lower() == "y":
            continue
        else:
            break


    elif choice == 2:
        logo = '''
  ___                       _   _          
 |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _  
 | |) / -_) _| '_| || | '_ \  _| / _ \ ' \ 
 |___/\___\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
	    
        print(logo)
        print("")
        filename = input("Enter the filename for decryption: ")
        key = int(input("Enter your key (0-255): "))
        Decrypt(filename, key)
        print("______________________________________________")
        printprint("|````````````````````````````````````````````|")
        printprintprint("|    File Decryption is done succssfully !   |")
        print("|____________________________________________|")
        print("``````````````````````````````````````````````")
        print("")
        home_menu = input("Enter 'Y' for Menu or 'N' to quit: ")
        if home_menu.lower() == "y":
            continue
        else:
            break

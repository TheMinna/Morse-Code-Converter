
morse_dict = {
    "A": "·-",
    "B": "-···",
    "C": "-·-·",
    "D": "-··",
    "E": "·",
    "F": "··-·",
    "G": "--·",
    "H": "····",
    "I": "··",
    "J": "·---",
    "K": "-·-",
    "L": "·-··",
    "M": "--",
    "N": "-·",
    "O": "---",
    "P": "·--·",
    "Q": "--·-",
    "R": "·-·",
    "S": "···",
    "T": "-",
    "U": "··-",
    "V": "···-",
    "W": "·--",
    "X": "-··-",
    "Y": "-·--",
    "Z": "--··",
    "0": "-----",
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
    }

# Logo made with 'Text to ASCII Art Generator (TAAG)' by patorjk.com:
print('''                                                                                                     
          ____                                                                                       
        ,'  , `.                                               ,----..                               
     ,-+-,.' _ |                                              /   /   \               ,---,          
  ,-+-. ;   , ||  ,---.   __  ,-.                            |   :     :  ,---.     ,---.'|          
 ,--.'|'   |  ;| '   ,'\,' ,'/ /| .--.--.                    .   |  ;. / '   ,'\    |   | :          
|   |  ,', |  ':/   /   '  | |' |/  /    '    ,---.          .   ; /--` /   /   |   |   | |  ,---.   
|   | /  | |  |.   ; ,. |  |   ,|  :  /`./   /     \         ;   | ;   .   ; ,. : ,--.__| | /     \  
'   | :  | :  |'   | |: '  :  / |  :  ;_    /    /  |        |   : |   '   | |: :/   ,'   |/    /  | 
;   . |  ; |--''   | .; |  | '   \  \    `..    ' / |        .   | '___'   | .; .   '  /  .    ' / | 
|   : |  | ,   |   :    ;  : |    `----.   '   ;   /|        '   ; : .'|   :    '   ; |:  '   ;   /| 
|   : '  |/     \   \  /|  , ;   /  /`--'  '   |  / |        '   | '/  :\   \  /|   | '/  '   |  / | 
;   | |`-'       `----'  ---'   '--'.     /|   :    |        |   :    /  `----' |   :    :|   :    | 
|   ;/                            `--'---'  \   \  /          \   \ .'           \   \  /  \   \  /  
'---'                                        `----'            `---`              `----'    `----'   
                                                                                                     
      ''')

print("Welcome to Morse Code Converter!")
print("")

def converter():
    user_phrase = (input("Please type a phrase in Latin alphabets and/or numbers: ")).upper()

    morse_code = ""
    for n in user_phrase:
        if n not in morse_dict and n != " ":
            print("Please use only Latin alphabets and/or numbers.")
        elif n == " ":
            n=" "
            morse_code += f"{n} " # Also adds space
        elif n in morse_dict:
            n = morse_dict[n]
            morse_code += f"{n} " # Also adds space
    morse_code = morse_code[:-1]  # Deletes the final space from the completed string
    print(f"Morse code: {morse_code}")

converter()

is_on = True
while is_on:
    print("")
    again = (input("Another one? (Y/N) ")).upper()
    if again == "Y":
        converter()
    if again == "N":
        print("")
        print("Thank you for using Morse Code Converter!\nBye Bye!")
        is_on = False
MORSE_CODE_DICT = { 
    'A':'.-','B':'-...',
    'C':'-.-.', 'D':'-..', 
    'E':'.','F':'..-.',
    'G':'--.','H':'....',
    'I':'..', 'J':'.---', 
    'K':'-.-','L':'.-..', 'M':'--', 
    'N':'-.','O':'---','P':'.--.', 
    'Q':'--.-','R':'.-.', 'S':'...',
    'T':'-','U':'..-','V':'...-',
    'W':'.--','X':'-..-', 
    'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.',
    ')':'-.--.-',
    ' ': '|'}


text = input("Enter message to be converted to morse code: ") 

morse_message_list = []
for char in text:
    if char.isalpha:
        char = char.upper()

    next_char = MORSE_CODE_DICT[char]
    morse_message_list.append(next_char)   

morse_message_string = " ".join(morse_message_list)   
print(morse_message_string)  
   
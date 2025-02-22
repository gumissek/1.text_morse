
morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-', 'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


keep_continue=True
while keep_continue:
    word = input('Type word or statement to translate into morse (only letters/numbers)(exclude special characters e.g @/!), if you want to exit type q: ')
    if word!='q':
        if word!='':
            morse_word=''

            for char in word:
                if char ==' ':
                     morse_word+='    '
                else:
                    try:
                        morse_word+=morse[char.upper()]
                    except KeyError:
                        print(f'That character {char} is special character and doesnt exist in morse dictionary, add has not been added to final word')
                        pass
                    else:
                        morse_word+=' '
            print(f'Here is your word/statement: \nYour word: {word}\nIn morse: {morse_word}')
        else:
            print('Your word is empty, try typing your word again')

    else:
        keep_continue=False




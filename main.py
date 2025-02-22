from traceback import print_tb

chars  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
    word = input('Type word or statement to translate into morse (only letters/numbers), if you want to exit type q: ')
    if word!='q':
        if word!='':
            morse_word=''

            for char in word:
                if char ==' ':
                     morse_word+='    '
                else:
                    morse_word+=morse[char.upper()]
                    morse_word+=' '
            print(f'Here is your word/statement: \nYour word: {word}\nIn morse: {morse_word}')
        else:
            print('Your word is empty, try typing your word again')

    else:
        keep_continue=False




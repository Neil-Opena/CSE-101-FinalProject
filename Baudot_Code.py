#Neil Opena 110878452

#Final Programming Project
#Part 1: Baudot Code

#if...value == 00011 / 00010 / 00001 - special
#else.....return ()

letterdict = {
    
    '10000' : 'A',  '11111' : 'P',
    '00110' : 'B',  '10111' : 'Q',
    '10110' : 'C',  '00111' : 'R',
    '11110' : 'D',  '00101' : 'S',
    '01000' : 'E',  '10101' : 'T',
    '01110' : 'F',  '10100' : 'U',
    '01010' : 'G',  '11101' : 'V',
    '11010' : 'H',  '01101' : 'W',
    '01100' : 'I',  '01001' : 'X',
    '10010' : 'J',  '00100' : 'Y',
    '10011' : 'K',  '11001' : 'Z',
    '11011' : 'L',  '10001' : '-',
    '01011' : 'M',  '00011' : 'ER',
    '01111' : 'N',  '00010' : 'FS',
    '11100' : 'O',  '00001' : ' ',
    '11000' : '/',
    
    }

figdict = {
    
    '10000' : '1',  '11111' : '+',
    '00110' : '8',  '10111' : '/',
    '10110' : '9',  '00111' : '-',
    '11110' : '0',  '00101' :  '',
    '01000' : '2',  '10101' :  '',
    '01110' :  '',  '10100' : '4',
    '01010' : '7',  '11101' : '\'',
    '11010' :  '',  '01101' : '?',
    '01100' :  '',  '01001' :  '',
    '10010' : '6',  '00100' : '3',
    '10011' : '(',  '11001' : ':',
    '11011' : '=',  '10001' : '.',
    '01011' : ')',  '00011' : 'ER',
    '01111' :  '',  '00010' : ' ',
    '11100' : '5',  '00001' : 'SP',
    '11000' :  '',
    
    }

response = input("Enter a Baudot-encoded message: \n")
codes = response.split(' ')
translation = ''

def translate(dictionary):
    global translation, codes
    for code in codes:
            if dictionary[code] == 'ER':
                #translation = translation + '*'
                #EXTRA CREDIT:
                translation = translation[:codes.index(code)-1] + translation[codes.index(code) + 2:]
            elif dictionary[code] == 'FS':
                dictionary = figdict
            elif dictionary[code] == 'SP':
                dictionary = letterdict
            else:
                translation = translation + (dictionary[code])

translate(letterdict)            
print (translation)


#TESTS:

#11110 00111 01100 01111 10011 00001 00100 11100 10100 00111 00001 11100 11101 10000 11011 10101 01100 01111 01000

#11010 01000 11111 00011 11011 11011 11100

#10110 00101 01000 00001 00010 10000 11110 10000 00010 00001 00111 11100 10110 10011 00101 












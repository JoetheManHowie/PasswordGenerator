#!/usr/bin/env python3

## Joe Howie
## April 7th, 2020
## generates random secure passwords from a text document
## eg run: python password_generator.py ../howtochangeyourmindsummary.txt 25 5 5


from random import random
import sys
from time import time

def main():
    '''
    Impliments the five steps of the algorithm:
    1) read .txt file
    2) selects a random chunk of text from the file
    3) remove punctuation and other undesireable characters, and pulls out n words
    4) randomly caplitalizes m letter in the string
    5) adds k random special characters to the password in random spots
    The resulting password is of length the specified length, 
    and the specified number of special characters
    '''
    try:
        ## 0) terminal params
        args = sys.argv
        filename = args[1]
        password_length = int(args[2])
        num_caps = int(args[3])
        num_sc = int(args[4])
        
        ## 1) read txt file    
        text = read_file(filename)
        
        ## 2) randomly select a passage of text n chars long      
        my_line = select_text(text, password_length)
        
        ## 3) remove punctuation like: ( ) , . ; : ' " _  etc..
        password_preped = remove_punctuation(my_line)
        password_preped = select_words(password_preped, password_length-num_sc)
        
        ## 4) randomly capitalize m letters in the string
        password = random_capitals(password_preped, num_caps)
        
        ## 5) add random special characters in the string
        password = random_special_chars(password, num_sc)
        
        ## 6) padding up to total length
        password = padding(password, password_length)
        print(password)
    # end try
    except (IndexError):
        print('you need to supply a file name\nLike: python password_generator.py myfile.txt')
        exit
    except (FileNotFoundError):
        print('File not found')
        exit
    # end except
# end def


def read_file(filename):
    text = open(filename, 'r')
    return text
# end def


def select_text(text, threshold = 50):
    line_by_line = text.readlines()
    fine_choice = []
    for line in line_by_line:
        if len(line) < threshold: continue
        fine_choice.append(line)
    # end for    
    my_line = fine_choice[int(random()*len(fine_choice))].rstrip() #.replace(' ', '') 
    return my_line
# end def


def remove_punctuation(line):
    chars = ['(', ')', '\'', '\"', ',', '.', '!', '?', ';', ':', '-', '_', '=', '+']
    chars.extend([str(i) for i in range(10)])
    for c in chars:
        line = line.replace(c, '')
    # end for
    return line
# end def


def select_words(line, length):
    words = sorted(line.split(' '), key=len)
    password = ''
    count = 0
    list_len = len(words)
    for i in range(list_len):
        w = words[list_len-1-i]
        #if i%2 ==0: w = words[i]
        if len(w) <= length- len(password):
            password += w
            count +=len(w)
        # end if
        if count == length: break
    # end for
    return password
# end def


def random_capitals(pw, m):
    pl = len(pw)
    password = ''
    rnums = get_random_nums(m, pl)
    for i in range(pl):
        if i in rnums:
            password += pw[i].upper()
        # end if
        else:
            password += pw[i].lower()
    # end for
    return password
# end def


def random_special_chars(pw, sc = 6):
    pl = len(pw)
    rnums = get_random_nums(sc, pl)
    special = ['@', '#', '$', '%', '^', '&', '*']
    special.extend([str(i) for i in range(10)])
    rsnum = get_random_nums(sc, len(special))
    password = ''
    a = 0
    for i in range(pl):
        if i in rnums:
            password += special[rsnum[a]]
            a +=1
        # end if
        password += pw[i]
    # end for
    return password
# end def


def get_random_nums(m, mod):
    rnums = []
    while(m > 0):
        rnums.append(int(random()*mod))
        m -= 1
    # end while
    return rnums
# end def


def padding(pw, tlen):
    pw_len = len(pw)
    alph = 'abcdefghijklmnopqrstuvwxyz'
    password = pw
    if pw_len != tlen:
        diff = tlen -pw_len
        ralph = get_random_nums(diff, len(alph))
        rspot = get_random_nums(diff, pw_len)
        a = 0
        password = ''
        for i in range(pw_len):
            if i in rspot:
                password += alph[ralph[a]]
                a +=1
            # end if
            password += pw[i]
        # end for
    return password
# end def 


if __name__ =="__main__":
    main()

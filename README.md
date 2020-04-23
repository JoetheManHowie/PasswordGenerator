# PasswordGenerator

## Introduction

With basically all your information online, it is obviously important to have strong password protection.
However, it is hard to be creative every time one needs a new password for an account.
It can be tempting to use the same or similar password for multiple accounts, but this is the digial equivalent of having one key for your car, house, safe, storage, and what have you.
The most secure passwords are simply the longest, with no underlying pattern (like words and phrases).
Indeed the longer the password, the harder it is to create and remember.
Luckly, this program has saved me the hassel of password creation.
Simply enter the desired length (25 is a good secure length), capital letters (most websites required at least one capital letter), and numbers & special characters (also required by most websites).

*Word of caution* While it is tempting to save these digially created password to a document on your computer, be aware of the danger of digitally storing your passwords in an unsecure location.
If you want to save these passwords to your computer, password protect this document with encryption or an application that has encryption buildin.

## Running the code

You will need a .txt file, preferably with at least 5000 words (more is better).

The current arguments need are in order

- path to .txt file (string)
- length of password (int) 
- number of capital letters (int)
- number of special characters and numbers (int)

### example run

`python password_generator.py <filename.txt> <int> <int> <int>`


## Coming Soon

I was to add a more particular selection on which special characters to permit in the command line inputs.
Also to separate the numbers from the special characters.
These will be added by the next version.
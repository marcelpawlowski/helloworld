#
#
#
####################
from sys import exit

print("Please Enter a Password to Evaluate")
passwd = input()
passwd_score = 0

def check_uppers(passwd):
    uppers=0
    upper_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
    for char in passwd:
        if char in upper_list:
            uppers += 1
        if uppers > 0:
            return True
        else:
            return False

def check_lowers(passwd):
    lowers=0
    lower_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    for char in passwd:
        if char in lower_list:
            lowers += 1
        if lowers > 0:
            return True
        else:
            return False

def check_numbers(passwd):
    numbers=0
    number_list = "0 1 2 3 4 5 6 7 8 9".split()
    for char in passwd:
        if char in number_list:
            numbers += 1
        if numbers > 0:
            return True
        else:
            return False

def check_len(passwd):
    if len(passwd) >= 8:
        return True
    else:
        return False

def evaluator(passwd_score):
    if check_numbers(passwd) & check_uppers(passwd) & check_lowers(passwd):
        if passwd_score <= 10:
            print("Password is weak. Add more characters!")


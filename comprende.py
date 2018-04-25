'''
Ye Olde Password Rater

task01: lower, upper, number?

task02: lower, upper, number, special character?
'''
LC_LETTERS = "qwertyuiopasdfghjklzxcvbnm"
UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
NUMBERS = "1234567890"
SPEC_CHAR = ".?!&#,;:-_*"

def pass_check(pwd):
    low = [1 for x in pwd if x in LC_LETTERS]
    cap = [1 for x in pwd if x in UC_LETTERS]
    num = [1 for x in pwd if x in NUMBERS]
    #spe = [1 for x in pwd if x in SPEC_CHAR]
    return len(low) >0 and len(cap)>0 and len(num)>0 #and len(spe)>0

                        #check 1: no special characters   #check 2
print pass_check("YOHO")  #f                                #f
print pass_check('yohO')  #f                                #f
print pass_check('yoh0')  #f                                #f
print pass_check('Y0hoOO')#t                                #f

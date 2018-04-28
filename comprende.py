#Carol Pan
#SoftDev2 pd7
#K15: Do You Even List?
#2018-04-26
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
    return len(low) >0 and len(cap)>0 and len(num)>0

                        #check 1: no special characters   #check 2
print pass_check("YOHO")  #f                                #f
print pass_check('yohO')  #f                                #f
print pass_check('yoh0')  #f                                #f
print pass_check('Y0hoOO')#t                                #f


def pass_strength(pwd):
    strength = 0
    
    spe = [1 for x in pwd if x in SPEC_CHAR]
    if len(spe) > 0:
        strength += 1

    if pass_check(pwd):
        strength += 3

    strength += len(pwd)//2

    if strength > 10:
        return 10
    else:
        return strength

print pass_strength("tr0ub;DOR") #8
print pass_strength("correcthorsebatterystaple@ABC123")#10
print pass_strength(";bc123AB") #8

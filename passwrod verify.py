print('Password Guidelines:\nMinimum 8 characters.\nThe alphabet must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $\n\n')
passWord = input("Enter password:")
pWord = []

for element in passWord:
    pWord.append(element)

def goodPwd(stuff):
    if len(stuff) < 8:
        print('Password must be a minimum of 8 characters')
    elif stuff.isalpha() == True:
        print('Password must only include at least 1 number 1-9.')
    elif stuff.isdigit() == True:
        print('Password must contain at least 1 letter')
    elif stuff.isupper() == True:
        print('Password must contain at least 1 lower case letter')
    elif stuff.islower() == True:
        print('Password must contain at least 1 upper case letter')
print(f'The password you have chosen is {passWord}')

goodPwd(passWord)
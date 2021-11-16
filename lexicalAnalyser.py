
if __name__ == "__main__" :

    s = input("Enter any operator : ");

    if (s[0] == '>') :
        if s[1] == '=' :
            print(' Greater than or equal');
        else :
            print('Greater than')
    elif (s[0] == '<') :
        if s[1] == '=' :
            print('Less than or equal');
        else :
            print('Less than')

    elif (s[0] == '='):
        if s[1] == '=' :
            print(' Equal to ');
        else :
            print('Assignment')
    
    elif s[0] == '!':
        if s[1] == '=' :
            print('Not equal to ');
        else :
            print('bit not')
    
    elif s[0] == '&' :
        if s[1] == '&':
            print("Logical And")
        else :
            print("Bitwise And")
    
    elif s[0] == '|' : 
        if s[1] == '|' :
            print('\n Logical Or');
        else :
            print('Bitwise or')
    
    elif s[0] == '+' :
        print("Addition")
    
    elif s[0] == '-' :
        print("Subtraction")
    
    elif s[0] == '*':
        print("Multiplication")
    
    elif s[0] == '/':
        print("Division")

    elif s[0] == '%':
        print("Modulus")

    else :
        print("Not an operator")
    
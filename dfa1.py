#q2
"""
dfa for length of string is atmost 2
"""

def start(c):
    if c == 'a' or c == 'b':
        return 1

def state1(c):
    if c == 'a' or c == 'b':
        return 2

def isValid(str):

    state = 0

    print("state Traversal : ")
    for char in str:

        print(state,end =" -> ")
        if state == 0:
            state = start(char)
        
        elif state == 1:
            state = state1(char)
        
        elif state == 2:
            return False
        
    print(state)
    return True

if __name__ == "__main__" :

    str = input("Enter a String : ")

    if isValid(str):
        print("string is accepted")
    else : 
        print("String is not accepted")
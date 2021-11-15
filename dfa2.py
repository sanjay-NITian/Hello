
#q3
"""dfa for length of stringis odd"""

def start(c):
    if c == 'a' or c == 'b' :
        return 1

def state1(c):
    if c == 'a' or c == 'b' :
        return 0

def isValid(str):
    state = 0

    print("state Traversal : ")
    for char in str:

        print(state, "->" , end = " ")

        if state == 0:
            state = start(char)
        
        elif state == 1:
            state = state1(char)

    print(state)
    if state == 0 :
        return False
    
    else :
        return True

if __name__ == "__main__":

    str = input("Enter a String : ")

    if isValid(str):
        print(str, "is accepted by dfa")
    else :
        print(str,"is not accepted by dfa")
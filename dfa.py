
# q1

"""dfa for table shown"""

def start(char) :
    if char == 'a':
        return 1
    elif char == 'b' :
        return 2

def state1(char):
    if char == 'a':
        return 0
    elif char == 'b':
        return 2

def isValid(s):
    
    state = 0

    print("State Traversal : ")
    for char in str :
        
        print(state, end = " -> ")
        if state == 0:
            state = start(char)

        elif state == 1 :
            state = state1(char)
        
        elif state == 2 : 
            return True
    
    return False

if __name__ == '__main__':

    str = input("Enter a  String : ")

    if isValid(str):
        print("string is Accepted")
    else :
        print("String is Invalid")
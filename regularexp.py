#code for re as a*

import re

pattern = re.compile(r'a*')

str = input("Enter a String : ")

# matches = re.finditer(pattern, str)
matches = re.findall(pattern,str)

print("\npattern matched : ")
for match in matches :
    print(match)
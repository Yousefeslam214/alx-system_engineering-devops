import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu)"

user_input = "yousefeslam214@gmail.com"

if(re.search(pattern, user_input)):
    print("valid email")
else:
    print("invaild email")




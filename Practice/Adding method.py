def Add(user_input):
    input = []
    add = 0
    for i in range(0,len(user_input)):
        add = int(user_input[i]) + add
    print"Addition is: ", add

while True:
    user = raw_input("Enter 2 integers separated by comma: ")
    if(user.Isalpha()):
        print"Enter digits only"
        continue
    
    else:
        user_input = user.split(",")
        Add(user_input)
        break
        









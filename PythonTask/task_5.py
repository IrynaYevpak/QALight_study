arg_A = int(input("number one: "))
arg_B = int(input("number two: "))
arg_C = int(input("number three: "))


def while_number (A, B, C):
    while A <= B:
        print("number one " + str(A))
        print(str(A) + " < " + str(B))
        A += C


while_number(arg_A, arg_B, arg_C)

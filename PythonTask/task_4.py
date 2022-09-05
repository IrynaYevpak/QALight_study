arg_A = int(input("number one: "))
arg_B = int(input("number two: "))
arg_C = int(input("number three: "))

def comparison(A, B, C):
    if A > B:
        print("Файно!")
    elif A == B:
        if C != B:
            print("От невдача...")
        elif C > B:
            print("Урааа...")
    else:
        print("Яка прикрість...")

comparison(arg_A, arg_B, arg_C)











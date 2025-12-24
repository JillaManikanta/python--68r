def funA():
    name=str(input("enter the name: "))
    passw=str(input("enter the password: "))
    correctname=""
    correctpassw=""
    while name!=correctname or passw!=correctpassw:
        print("login")
        correctname=str(input("enter the correct name: "))
        correctpassw=str(input("enter the correct password: "))
        if name!=correctname or passw!=correctpassw:
            print("invalid")
    print("successfull")
funA()
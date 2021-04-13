# password = input("put your password ")
#
# original_password = "correct"
#
# if original_password == password:
#     print("correct")
#
# else:
#     print("Incorrect")

age = int(input("Put your age >>> "))

if age >= 14:
    print("pasport is ready")

    if 20 <= age < 45:
        print("replace passport")

elif age < 1:
    print("Custom")

else:
    print("Forget about it")

# # ============================================
# # Lecture 5: Conditional Statements
# # ============================================

# # --- if, elif, else ---
# temperature = 35

# if temperature > 40:
#     print("Ghar raho")
# elif temperature > 30:
#     print("Paani le jao")
# else:
#     print("Maze se niklo")

# # --- AND Operator ---
# # Dono conditions true honi chahiye
# age = 18
# having_license = True

# if age >= 18 and having_license:
#     print("Drive kar sako")
# else:
#     print("Nahi kar sako")

# # --- OR Operator ---
# # Koi ek condition true ho kaafi hai
# has_cash = False
# has_card = True

# if has_cash or has_card:
#     print("Payment ho sakti hai")
# else:
#     print("Payment nahi hogi")

# # --- NOT Operator ---
# # Condition ulat jaati hai
# is_raining = False

# if not is_raining:
#     print("Bahar jao")
# else:
#     print("Ghar ruko")

# # --- Nested if ---
# # if ke andar if
# marks = 75

# if marks >= 50:
#     if marks >= 80:
#         print("A grade")
#     else:
#         print("B grade")
# else:
#     print("Fail")

# if / elif / else 

# #Assignment # 01

# user_age = 17
# if user_age >=18:
#     print("Congratulation")
# else:
#     print("Sorry")


# #Assignment # 02

# user_marks = 59
# if user_marks >=50:
#     if user_marks >=80:
#         print("A Grade")
#     elif user_marks >=70:
#         print("B Grade")
#     else: print("C Grade")
# else: print("Fail")


# #Assignment # 03

# user_name = "admin"
# password = "1234"                                           # mene password ko "Double quotes" mein is liay rakha q k user real application mein Input krtay password as a string add krta hai. 
# if user_name == "admin" and password == "1234":
#     print("Login Successful")
# else: 
#     print("Invalid user name and password")



# # Assignment # 04
# secret_number = 7
# user_number = int(input("Enter your Number: "))

# if user_number == secret_number:
#     print("correct! you win")
# elif user_number < secret_number:
#     print("Too Low")
# else:
#     print("Too High")



# # Assignment # 05
# secret_number = 9
# guess_1 = int(input("Attempt 1: "))

# if guess_1 == secret_number:
#     print("You Win!")
# else:
#     guess_2 = int(input("Attempt 2: "))

#     if guess_2 == secret_number:
#         print("You Win")

#     else:
#         guess_3 = int(input("Attempt 3:"))

#         if guess_3 == secret_number:
#             print("You Win")
        
#         else:
#             print("Gane-Over")


# Asssignment # 06

user_name = "admin"

guess_1 = input("Attempt 1: ")

if guess_1 == user_name:
    print("Welcom Admin")
else:
     guess_2 = input("Attempt 2: ")
     
     if guess_2 == user_name:
        print("Welcom Admin")
     else:
        guess_3 = input("Attempt 3: ")
        
        if guess_3 == user_name:
            print("Welcom Admin")
        else:
            print("Time-out! please wait at least 15 mins")
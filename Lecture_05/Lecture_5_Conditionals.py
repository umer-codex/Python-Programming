# ============================================
# Lecture 5: Conditional Statements
# ============================================

# --- if, elif, else ---
temperature = 35

if temperature > 40:
    print("Ghar raho")
elif temperature > 30:
    print("Paani le jao")
else:
    print("Maze se niklo")

# --- AND Operator ---
# Dono conditions true honi chahiye
age = 18
having_license = True

if age >= 18 and having_license:
    print("Drive kar sako")
else:
    print("Nahi kar sako")

# --- OR Operator ---
# Koi ek condition true ho kaafi hai
has_cash = False
has_card = True

if has_cash or has_card:
    print("Payment ho sakti hai")
else:
    print("Payment nahi hogi")

# --- NOT Operator ---
# Condition ulat jaati hai
is_raining = False

if not is_raining:
    print("Bahar jao")
else:
    print("Ghar ruko")

# --- Nested if ---
# if ke andar if
marks = 75

if marks >= 50:
    if marks >= 80:
        print("A grade")
    else:
        print("B grade")
else:
    print("Fail")
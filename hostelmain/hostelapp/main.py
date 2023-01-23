# -----------------------Input Data funtion-------------------------
food_item = input(
    "Please Enter Today Market item (like chicken , beef ,fish or egg # must use lowercase) : ")
member = int(input("Please Enter amount of today Members : "))
market_cost = int(input("Pleasr enter foodMarket cost : "))
# food_item = set(input("Enter Today Food item : "))

# ---------------------------------------------------------
# ------------Constant/updateable Value------------

member_name = ["Shakil", "Babu", "Sadik", "Rayhan", "Morsed", "Ibrahim"]
food_list = ["beef", "chicken", "fish", "egg"]


# ----------------------------------------------------------
# ------------------Oparetion of Data funtion----------------------
# --------------------Other Funtion-----------------------------


def foodcycle(*args):

    while True:
        try:
            for item in food_list:
                if item == food_item.lower():
                    print("Next food Market item is " + food_list[food_list.index(item) + 1])
        except IndexError:
            print("Next food Market item is Beef")

        break


# ---- Oparetion funtion


def millrate():
    millrate = market_cost/(member*6)
    return millrate

# --- Alart funtion---#


def alart():
    if millrate > 13:
        str1 = print("Maneger your millrate is high to Previouse day :( !!!")
        return str1
    elif millrate <= 20:
        str2 = print("Great job Maneger Continue Your manegment :)!")
        return str2
    else:
        pass


# --- Main App Funtion -----
# millrate = millrate()
# alart = alart()
# foodcycle = foodcycle(food_list, food_item)


# def mainapp():
#     main = print(millrate), alart, foodcycle
#     return main


# mainapp()

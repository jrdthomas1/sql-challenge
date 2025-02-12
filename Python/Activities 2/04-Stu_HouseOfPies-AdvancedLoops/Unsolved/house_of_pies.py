# variable indicating orders are being made
ordering = "y"

# empty cart
pie_cart = []

# while loop is initially active
while ordering == "y":

    # String with store intro
    print("Welcome to the house of pies! here are your pies:")
    print("------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak")

    pie_choice = input("which pie would you like? Enter the number here:")

    # list of pies
    pie_list = ["pecan", "apple crisp", "bean", "banoffee", "black bean", "blueberry", "buko", "burek", "tamale", "steak"]

    #position of pie type in list
    pie_index = int(pie_choice) - 1

    #order confirmation
    print(f"Great! We'll have that {pie_list[pie_index]} right out for you")

    # add 1 to the appropriate value of pie cart
    # pie_cart = pie_cart[pie_index] + 1
    #alternatively
    pie_cart[pie_index]+= 1

    # ask if another order would be made
    ordering = input("would you like to make another order? Type 'y' to do so. ")

#print number of pies ordered
print(len(pie_cart))
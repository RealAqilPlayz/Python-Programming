# Define a Python Dictionary
# Dictionary has key : value pairs
menu = {
    "Hawaiian Pizza": 11.99,
    "Pepperoni Roni": 13.99,
    "4 Cheese": 14.50,
    "Chicken Pepperoni": 9.90,
    "Smoky Mushroom": 8.90,
    "Salad": 5.00,
    "Fries": 3.00,
    "Coke Zero": 2.00,
    "Fanta Grapes": 2.50,
    "Iced Lemon Tea": 1.00
}

food_keys_list = list(menu.keys())



def display_menu():
    food_numbers = 1
    for food, price in menu.items():
        print(f"{food_numbers}.", food, f"- ${price:.2f}")
        food_numbers = food_numbers + 1


def take_order():
    global switch
    global total_orders
    order = input("Enter the item you want to order or 0 to finish order: ")

    if order == "R":
        print("Hello boss! Current revenue: " + str(revenue_of_the_day) + "\n")
        return

    if order == "0":
        switch = False
    elif int(order) > 0 and int(order) <= len(menu):
        total_orders.append(int(order))

    print(total_orders)
    print("\n")


def Print_Order_Summary():
    global total_orders
    global food_keys_list
    global total_amount

    print("🇸🇬" * 10 + " Order Summary " + "🇸🇬" * 10)
    for i in total_orders:
        print(food_keys_list[i - 1], menu[food_keys_list[i - 1]], sep=" - ")
        total_amount = total_amount + menu[food_keys_list[i - 1]]

    total_amount = round(total_amount, 2)
    print("Total amount before GST and Service Charge " + str(total_amount))
    print("+ 9% GST - " + str(round((total_amount * 0.09), 2)))
    print("+ 10% Service Charge - " + str(round((total_amount * 0.10), 2)))

    total_amount = total_amount + (total_amount * 0.09) + (total_amount * 0.10)
    total_amount = round(total_amount, 2)

    print("Total payable: " + str(total_amount))
    print("\n")





# Main Program Loop
# Forever Loop

customer_no = 1
revenue_of_the_day = 0
while True:

    print("=" * 50 + "Currently serving customer # " + str(customer_no))
    print(" " * 14 + "Welcome to Pizza R Us!")
    print("=" * 50)

    switch = True
    total_orders = []
    total_amount = 0

    # inner loop ensures we take orders from a customer repeatedly until key 0 is entered
    while switch:
        display_menu()
        take_order()

    Print_Order_Summary()

    customer_no = customer_no + 1
    revenue_of_the_day = revenue_of_the_day + total_amount















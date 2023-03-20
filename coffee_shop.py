"""
A program that will calculate the cost of a custom cup of coffee at a gourmet coffee shop,
based on the size of the cup, the type of coffee selected, and flavors that can be added to the coffee.

@author: Salik Tariq
@date: 20 March 2023
"""


# Helper functions to break down code into smaller functionalities

# function to get the size of coffee
def get_size():
    while True:
        size = input("What size cup do you want? (Small, Medium, or Large) ")
        if size.lower() in ["small", "medium", "large"]:
            return size.lower()
        else:
            print("Invalid size. Please enter either Small, Medium or Large.")


# function to set the price based on size
def set_price(coffee_size):
    if coffee_size.lower() == "small":
        return 2
    elif coffee_size.lower() == "medium":
        return 3
    elif coffee_size.lower() == "large":
        return 4
    else:
        return 0


# function to get the type of coffee
def get_coffee_type():
    while True:
        coffee_type = input("What kind of coffee do you want? (Brewed, Espresso, or Cold Brew) ")
        if coffee_type.lower() in ["brewed", "espresso", "cold brew"]:
            return coffee_type.lower()
        else:
            print("Invalid input. Please enter either Brewed, Espresso or Cold Brew.")


# function to set additional cost based on coffee type
def set_additional_cost(type_of_coffee):
    if type_of_coffee.lower() == "brewed":
        return 0
    elif type_of_coffee.lower() == "espresso":
        return 0.5
    elif type_of_coffee.lower() == "cold brew":
        return 1
    else:
        return 0


# function to get the flavor of coffee
def get_flavor():
    while True:
        want_flavor = input("Do you want a flavored syrup? (Yes or No) ")
        if want_flavor.lower() == "no":
            return "None"
        else:
            while True:
                flavor_type = input("Do you want Hazelnut, Vanilla, Caramel? ")
                if flavor_type.lower() in ["hazelnut", "vanilla", "caramel"]:
                    return flavor_type.lower()
                else:
                    print("Invalid input. Please enter either Hazelnut, Vanilla or Caramel.")


# function to set additional cost based on flavor
def set_flavor_cost(flavour):
    if flavour.lower() == "none":
        return 0
    else:
        return 0.5


# Main program

# Ask user for size of the coffee
size = get_size()

# Define price based on size
price = set_price(size)

# Ask user for type of coffee
coffee_type = get_coffee_type()

# Define additional cost based on type of coffee
additional_cost = set_additional_cost(coffee_type)

# Ask user if they want flavoring
flavor = get_flavor()

flavour_cost = set_flavor_cost(flavor)

# Calculate total cost
total_cost = price + additional_cost + flavour_cost

# Display summary of the user's order
print(f"You asked for a {size} cup of {coffee_type} coffee", end="")
if flavor.lower() == "yes":
    print(f" with {flavor.lower()} syrup.")
else:
    print(".")

# Display total cost of the cup of coffee
print(f"Your cup of coffee costs {total_cost:.2f}")

# Display total cost of the cup of coffee with a 15% tip
total_cost_with_tip = total_cost * 1.15
print(f"The price with a tip is {total_cost_with_tip:.2f}")

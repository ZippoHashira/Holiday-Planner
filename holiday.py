# Define function 'hotel_cost' that takes number of nights as an argument.
# Return 'total_cost' which is 'num_of_nights' times 'price'.
def hotel_cost(num_of_nights):
    price = 150
    total_cost = num_of_nights * price
    return total_cost


# Define function 'plane_cost' that takes city as an argument.
# Using 'if/elif' statement, return the correct cost of flight based on the city chosen.
# Else, return 0.
def plane_cost(city):
    if city.lower() == "london":
        return 400
    elif city.lower() == "paris":
        return 350
    elif city.lower() == "tokyo":
        return 320
    elif city.lower() == "seattle":
        return 500
    else:
        return 0


# Define function 'car_rental' which takes days as an argument.
# Return 'total_amount' which is 'days' times 'price'.
def car_rental(days):
    price = 200
    total_amount = days * price
    return total_amount


# Define function 'holiday_cost' which takes three arguments 'nights', 'city' and 'days'.
# Return 'total_price' which is the sum of 'nights', 'city' and 'days'.
def holiday_cost(nights, city, days):
    nights = hotel_cost(nights)
    city = plane_cost(city)
    days = car_rental(days)
    total_price = nights + city + days
    return total_price


# Request user to input the number of nights they will be staying at the hotel and store it in variable 'nights'.
# Request user to choose their destination city from the options provided and store it in variable 'city'.
# Request user to input the number of days they will be hiring the car for and store it in variable 'days'.
# Calculate the total by passing 'nights', 'city' and 'days' input as the arguments in 'holiday_cost' function.
nights = int(input("How many nights are you staying? "))
city = input("Where are you headed? (Options: London, Paris, Tokyo, Seattle) ")
days = int(input("How many days will you be hiring the car for? "))
total = holiday_cost(nights, city, days)

# Print out the details about the holiday using f-string.
print(f"""
Your booking details:
------------------------------------------------------
Destination: {city} 
Ticket price: £{plane_cost(city)}
Cost of {nights} night(s) of hotel: £{hotel_cost(nights)}
Car rental for {days} days: £{car_rental(days)}
-------------------------------------------------------
Total:      £{holiday_cost(nights, city, days)}
-------------------------------------------------------
Thank you for booking with Python Travel Agency!
""")
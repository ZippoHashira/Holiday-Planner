# Holiday Planner 
The ‘holiday.py’ program is designed to help calculate the cost of a holiday by considering various factors such as hotel stay, flight expenses, and car rental costs. It provides four functions:

1. hotel_cost(nights): Calculates the total cost for hotel stay based on the number of nights.

2. plane_cost(city): Determines the flight cost based on the destination city chosen.

3. car_rental(days): Computes the total cost of car rental based on the number of days.

4. holiday_cost(nights, city, days): Combines the above functions to calculate the overall total cost for the holiday.

## Usage
1. Clone the repository to your local machine or download the ‘holiday.py’ file directly.

2. Open the file in a Python editor or IDE of your choice.

3. Call the ‘holiday_cost’ function with the necessary arguments to calculate the total cost of your holiday. You can modify the function calls and arguments to customize the parameters as per your requirements.

4. Run the program. The output should display all the details about your holiday in a meaningful way.

## Functions
1. hotel_cost(nights): This function takes the number of nights a user will be staying at a hotel as an argument and returns the total cost for the hotel stay. You can customize the price per night charged at the hotel within the function.

2. plane_cost(city): This function takes the city you are flying to as an argument and returns the cost for the flight. The function utilizes if/else if statements to retrieve the price based on the chosen city. You can modify and extend the if/else if statements to include more cities and their respective prices.

3. car_rental(days): This function takes the number of days the car will be hired for as an argument and returns the total cost of the car rental. You can customize the daily rental cost within the function.

4. holiday_cost(nights, city, days): This function takes three arguments: the number of nights a user will be staying in a hotel, the city the user will be flying to, and the number of days the user will be hiring a car for. It calls the ‘hotel_cost’, ‘plane_cost’, and ‘car_rental’ functions with the respective arguments and returns the total cost for your holiday.

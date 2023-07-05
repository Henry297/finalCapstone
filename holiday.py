def hotel_cost(num_nights):
    price_per_night = 120  # Assuming a constant price per night
    total_cost = num_nights * price_per_night
    return total_cost


def plane_cost(city_flight):
    if city_flight == "Newcastle":
        return 200
    elif city_flight == "London":
        return 250
    elif city_flight == "Edinburgh":
        return 400
    else:
        return 0


def holiday_cost(city_flight, num_nights, rental_days):
    hotel_total = hotel_cost(num_nights)
    plane_total = plane_cost(city_flight)
    car_rental_total = rental_days * 50  # Assuming a constant price per rental day
    
    total_cost = hotel_total + plane_total + car_rental_total
    return total_cost


# Get user inputs
city_flight = input("Enter the city you will be flying to (Newcastle, London, Edinburgh): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car for: "))

# Calculate holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Print holiday details
print("Holiday Details:")
print("City of Flight:", city_flight)
print("Number of Nights at Hotel:", num_nights)
print("Number of Rental Days:", rental_days)
print("Hotel Cost:", hotel_cost(num_nights))
print("Flight Cost:", plane_cost(city_flight))
print("Car Rental Cost:", rental_days * 45)
print("Total Holiday Cost:", total_cost)



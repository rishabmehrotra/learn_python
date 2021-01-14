"""
Variable: A variable is nothing more than a name for something so you can use the name rather 
than the something as you code.

Rules/Best practices for declaring a variable
"""
cars = 100
space_in_a_car = 40.4
drivers = "as many as you want"
drivers_we_have = 50
passengers = "depends on how good your luck is"
passengers_in_reality = 40
cars_not_driven = cars - drivers_we_have
cars_driven = drivers_we_have
carpool_capacity = cars_driven * space_in_a_car
average_passenger_in_car = passengers_in_reality / cars_driven

print("Cars avaialble", cars)
print("Cars driven", cars_driven ,"Since there are only ", drivers_we_have ," available")
print("Numbers of not driven ", cars_not_driven)
print("Number of passengers that can driven", carpool_capacity)
print("Number of passengers in each car", average_passenger_in_car)
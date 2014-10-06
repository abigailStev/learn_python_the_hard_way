cars = 100 # Single equals is an assignment, double equals is a boolean statement
# cannot have a variable name that starts with a number
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven=drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# in this way, spaces are automatically placed around the variable included,
# so putting spaces before and after the quotes results in extra spaces
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
# able to have multiple things included in a print string like this

print
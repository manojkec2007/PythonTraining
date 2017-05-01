# coding=utf-8
"""
3. Write a program which prompts the user for a Fahrenheit temperature, 
convert the temperature to Celsius and 
print out the converted temperature.
"""
input = raw_input("Enter temperature in Fahrenheit:")
fahren = float(input)

#Convert Fahrenheit to Celsius : Formula T(°C) = (T(°F) - 32) × 5/9
celsius = (fahren - 32.0) * 5.0 / 9.0
print "Temperature in Celsius is:", celsius


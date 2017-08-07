aircraft_name = "Boeing"
aircraft_model = 777

# print adds spaces between variables!
print(aircraft_name, aircraft_model)

# concatenating the variables python needs to be informed of the explicit conversion
# else it will result in the following error
#   Traceback (most recent call last):
#       File "hello_python.py", line 7, in <module>
#           full_sentence = aircraft_name + aircraft_model
#   TypeError: Can't convert 'int' object to str implicitly

full_sentence = aircraft_name + ' ' + str(aircraft_model)
print(full_sentence)
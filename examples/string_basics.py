# print a length of string
hello_world = "Hello World!"
print(len(hello_world))

# print index positions of string
print(hello_world[1] + hello_world[4])

# using slice to access parts of string, similar to substring in Java but starts with 1
# begin index is inclusive, end exclusive
slice_example = "I'm going to be sliced!"
# prints - goi
print(slice_example[4:7])
# prints - I'm go
print(slice_example[:6])
# prints - 'm going to be sliced!
print(slice_example[1:])
# Is the slice silent on out-of-bounds conditions?

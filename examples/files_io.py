
# python will create file if not exists, w - write, r - read and a - append (updates)
menu_list = open('menu_list.txt', 'a')

menu_list.write("Curly fries\n")
menu_list.write("Fried rice\n")

menu_list.close()

menu_list = open('menu_list.txt', 'r')

# Reading each line, readline remembers next line to read
print("First Line", menu_list.readline())
print("Second Line", menu_list.readline())

menu_list = open('menu_list.txt', 'r')
menu_items = []

for menu_item in menu_list:
    # strip removes leading and trailing whitespaces
    menu_item = menu_item.strip()
    menu_items.append(menu_item)

print(menu_items)


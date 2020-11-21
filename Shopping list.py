shopping_list = []

print("What shall we buy from the shops")
print("Enter 'DONE' to stop adding items")

while True:
    #Asks for new items
    new_item = input("> ").upper()

    #Be able to quit the app
    if new_item == 'DONE':
        break

    #Add items to the shopping list
    shopping_list.append(new_item)

print("Here's your list:")

for item in shopping_list:
    print(item)

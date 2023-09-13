class Note:
def __init__(self):
self.notes = {}
# Dictionary to store notes (username -> list of items)
def
add_item(self):
username = input("Enter your username: ")
item = input("Enter an item to add: ")
if username
not in self.notes:
self.notes[username] = []
self.notes[username].append(item)
print(f"{item} has been added to
{username}'s list.")
def view_items(self):
username = input("Enter the username to view items: ")
if username
in self.notes:
items = self.notes[username]
if items:
print(f"Items for {username}:")
for index,
item in enumerate(items,
1):
print(f"{index}.
{item}")
else:
print(f"{username}'s list is empty.")
else:
print(f"User '{username}' does not exist.")
def delete_item(self):
username = input("Enter the username to delete an item from: ")
if username
in self.notes:
items = self.notes[username]
if items:
self.view_items()
try:
index = int(input("Enter the number of the item to delete: ")) -
1
if
0 <= index < len(items):
deleted_item = items.pop(index)
print(f"{deleted_item} has been deleted from
{username}'s list.")
else:
print("Invalid item number.")
except ValueError:
print("Invalid input. Please enter a valid item number.")
else:print(f"{username}'s list is empty.")
else:
print(f"User '{username}' does not exist.")
def menu(self):
while True:
print("\nOptions:")
print("1. Add an item")
print("2. View items")
print("3. Delete an item")
print("4. Quit")
choice = input("Enter your choice (1/2/3/4): ")
if choice ==
'1':
self.add_item()
elif choice ==
'2':
self.view_items()
elif choice ==
'3':
self.delete_item()
elif choice ==
'4':
print("Goodbye!")
break
else:
print("Invalid choice. Please select a valid option (1/2/3/4).")








if __name__ ==

"__main__":



note = Note()



note.menu()

pet_list=[{"name": "Buddy", "type": "Dog", "status": "Available"},
          {"name": "Kohi", "type": "Cat", "status": "Adopted"},
          {"name": "Mochi", "type": "Cat", "status": "Available"},
          {"name": "Chino", "type": "Dog", "status": "Available"},
          {"name": "Larry", "type": "Snail", "status": "Adopted"}]


# functions
def add_pet():
    while True:
        choice = input("Type yes to continue or no to go back: ")
        if choice == "yes":
            name = input("Name of pet: ")
            type = input("Type of pet: ")
            status = input("Available / Adopted: ")

            if name and type and status != "":
                pet_list.append({"name": name, "type": type, "status": status})
                print("Added successfully!")
            elif name or type or status == "":
                print("All questions should be answered!")
        elif choice == "no":
            break

def view_pets():
    for item in pet_list:
        print(item)

def count_available_available(count):
    while True:
        choice = input("Available or Adopted? ")
        if choice == "Available":
            for item in pet_list:
                if item["status"] == "Available":
                    count += 1
                    continue
            print(count)
        if choice == "Adopted":
            for item in pet_list:
                if item["status"] == "Adopted":
                    count += 1
                    break
            print(count)

def find_pet():
    while True:
        choice = input("Type yes to continue or no to go back: ")
        if choice == "yes":
            look = input("Search in Category: ")
            inside = input("Search Value: ")
            output = None 
            for item in pet_list:
                if item[look] == inside:
                    output = item
                    break
            print(output)
        elif choice == "no":
            break
                

def display_menu():
    while True:
        print(f"=== Pet Adoption Records ===")
        print("1. Add a pet\n2. View all pets\n3. Count available vs adopted\n4. Find a pet by name\n5. Exit")
        choice = int(input("Choose an option [1-5]: "))

        if choice == 1:
            add_pet()
        elif choice == 2:
            view_pets()
        elif choice == 3:
            avail_count = 0
            adopt_count = 0
            count_available_available(avail_count)
        elif choice == 4:
            find_pet()
        elif choice == 5:
            break

# main starts here
display_menu()
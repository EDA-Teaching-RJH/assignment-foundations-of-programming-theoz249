import time
name = ["Picard", "Riker", "Data", "Worf", "Spock"]
rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commader"]
div = ["Command", "Command", "Operations", "Security", "Science"]
id = ["0000", "1111", "2222", "3333", "4444"]


def init_database():
    print(name)
    print(rank)
    print(div)
    print(id)

def display_menu():
    Student = input("Input your username: ")
    time.sleep(0.1)
    print("wlecome", Student)
    time.sleep(0.3)
    while True:
        print("\n--- MENU ---")
        print("1. Add Crew")
        print("2. Remove Crew")
        print("3. Update Crew")
        print("4. Display Crew")
        print("5. search Crew")
        print("6. Filter by Division")
        print("7. Payroll")
        print("8. calculate officers")
        print("9. Exit")
        print("---------\n")
        option = input("Select option")
        if option == "1":
            add_member()
        elif option == "2":
            remove_member()



def add_member():
    new_name = input("Name: ").title()
    new_rank = input("Rank: ").title()
    new_div = input("Division: ").title()
    new_id = str(input("ID: "))
    if new_id not in id :
        if rank == "Captain" or rank == "Commander" or rank == "lt.Commander" or rank == "Lieutenant" or rank == "Ensign":
            name.append(new_name)
            rank.append(new_rank)
            div.append(new_div)
            id.append(new_id)
            print("Crew member added.")
        else:
            print("invalid rank")
    else:
        print("invalid id")

def remove_member():
    if len(id) != 0 :
        rem = input("ID to remove: ")
        if rem in id :
            idx = id.index(rem)
            name.pop(idx)
            rank.pop(idx)
            div.pop(idx)
            id.pop(idx)
            print("Removed.")
        else:
            print("id doesnt match")
    else:
        print("Invalid action.")





loading = 0
while loading < 5 :
    print("System loading" , loading)
    loading += 1
    time.sleep(0.1)
    if loading  == 5 :
        print("Systems online")
init_database()
display_menu()
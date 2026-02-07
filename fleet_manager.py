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
        print("\n---------")
        option = input("Select option")
        if option == "1"  or option  == "view database ":
            
def add_member

loading = 0
while loading < 5 :
    print("System loading" , loading)
    loading += 1
    time.sleep(0.1)
    if loading  == 5 :
        print("Systems online")
init_database()
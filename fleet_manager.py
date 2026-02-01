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
    while True:
        print("\n--- MENU ---")
        print("1. View database")
        print("2. ")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        print("6. View Crew")
        print("7. Add Crew")
        print("8. Remove Crew")
        print("9. Analyze Data")
        print("10. Exit")       


loading = 0
while loading < 5 :
    print("System loading" , loading)
    loading += 1
    time.sleep(0.1)
    if loading  == 5 :
        print("Systems online")
init_database()
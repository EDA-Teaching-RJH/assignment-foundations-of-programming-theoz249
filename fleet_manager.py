
name = ["Picard", "Riker", "Data", "Worf", "Spock"]
rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
div = ["Command", "Command", "Operations", "Security", "Science"]
id = ["0000", "1111", "2222", "3333", "4444"]


def init_database():
    print(name)
    print(rank)
    print(div)
    print(id)

def display_menu():
    Student = input("Input your username: ")
    print("wlecome", Student)
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
        option = input("Select option: ")
        if option == "1":
            add_member()
        elif option == "2":
            remove_member()
        elif option == "3":
            update_rank()
        elif option == "4":
            display_roster()
        elif option == "5":
            search_crew()
        elif option == "6":
            division_fylter()
        elif option == "7":
            payroll()
        elif option == "8":
            count_officers()
        elif option == "9":
            print("Shutting down.")
            break  
        else:
            print("Invalid.")


def add_member():
    new_name = input("Name: ").title()
    new_rank = input("Rank: ").title()
    new_div = input("Division: ").title()
    new_id = str(input("ID: "))
    if new_id not in id :
        if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Lt.Commander" or new_rank == "Lieutenant" or new_rank == "Ensign":
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
            print("ID doesnt match")
    else:
        print("Invalid action.")

def update_rank():
    rid = input("ID to update: ")
    if rid in id :
        rids = id.index(rid)
        rank.pop(rids)
        newRank = input("what is the new Rank of").title()
        if newRank == "Captain" or newRank == "Commander" or newRank == "lt.Commander" or newRank == "Lieutenant" or newRank == "Ensign":
            rida = rids - 1
            rank.insert(rida, newRank)
            print("successfully updated")
        else:
            print("invalid rank")
    else:
        print("invlid ID")
    
def display_roster():
            print("Current Crew List:")
            for i in range(len(name)):
                print(name[i] + " - "  + rank[i] + " - "  + div[i]) 


def search_crew():
    searchTerm = input("search for a term in the crew: ").title()
    if searchTerm in rank:
        x = rank.index(searchTerm)
        y = rank.count(searchTerm) - 1
        z = 0
        print(name[x]) 
        while z < y :
            x =  rank.index(searchTerm, x + 1)
            print(name[x]) 
            z += 1 
    elif searchTerm in div:
        x = div.index(searchTerm)
        y = div.count(searchTerm) - 1
        z = 0
        print(name[x]) 
        while z < y :
            x =  div.index(searchTerm, x + 1)
            print(name[x]) 
            z += 1  

def division_fylter() :    
    fylteropt = input("what division you want to filter: ").title()
    if fylteropt in div:
        if fylteropt = "Command":
            x = div.index(fylteropt)
            y = div.count(fylteropt) - 1
            z = 0
            print(name[x]) 
            while z < y :
                x =  div.index(fylteropt, x + 1)
                print(name[x]) 
                z += 1  
        elif fylteropt = "Operations":
            x = div.index(fylteropt)
            y = div.count(fylteropt) - 1
            z = 0
            print(name[x]) 
            while z < y :
                x =  div.index(fylteropt, x + 1)
                print(name[x]) 
                z += 1              
        elif fylteropt = "Security":
            x = div.index(fylteropt)
            y = div.count(fylteropt) - 1
            z = 0
            print(name[x]) 
            while z < y :
                x =  div.index(fylteropt, x + 1)
                print(name[x]) 
                z += 1  
        elif fylteropt =  "Science":
            x = div.index(fylteropt)
            y = div.count(fylteropt) - 1
            z = 0
            print(name[x]) 
            while z < y :
                x =  div.index(fylteropt, x + 1)
                print(name[x]) 
                z += 1
        else:
            print("invalid div")  
    else:
        print("Invalid input")

def payroll():
    capCost = rank.count("Captain") * 1000
    commCcost = rank.count("Commander") * 800
    ltcommost = rank.count("Lt.Commander") * 600
    ltCost = rank.count("Lieutenant") * 400
    enCost = rank.count("Ensign") * 200
    cost = capCost + commCcost + ltcommost + ltCost + enCost
    print("the total cost of the crew is: ", str(cost) + "$")

def count_officers():
    count = 0        
    for rank in r:
        if rank == "Captain" or rank == "Commander": 
            count +=  1
            print("High ranking officers: ", count)
loading = 0
while loading < 5 :
    print("System loading" , loading)
    loading += 1
    time.sleep(0.1)
    if loading  == 5 :
        print("Systems online")
init_database()
display_menu()

name = ["Picard", "Riker", "Data", "Worf", "Spock"]
rank = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
div = ["Command", "Command", "Operations", "Security", "Science"]
id = ["0000", "1111", "2222", "3333", "4444"]


def init_database():#this is a pece of code that shows the initial conents of the 4 lists
    print(name)
    print(rank)
    print(div)
    print(id)

def display_menu():#this is the mane peice of code that the user interacts with
    Student = input("Input your username: ").title() #asks the user for their name and capitalises the first letter
    print("wlecome", Student)#welcomes the user
    while True: #the main loop that displays the users options
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
        option = input("Select option: ")#asks for the users option to determine what operation to use
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


def add_member():#this is resposible for adding contents to all the list 
    new_name = input("Name: ").title()#asks the user for a new name, rank , division and id
    new_rank = input("Rank: ").title()
    new_div = input("Division: ").title()
    new_id = str(input("ID: "))
    if new_id not in id :#makes sure the id is unique 
        if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Lt.Commander" or new_rank == "Lieutenant" or new_rank == "Ensign":#makes sure the rank is a valid rank
            name.append(new_name)#adds the users new name, rank, division and id to the end of all the lists 
            rank.append(new_rank)
            div.append(new_div)
            id.append(new_id)
            print("Crew member added.")
        else:
            print("invalid rank")
    else:
        print("invalid id")

def remove_member():#resposible for removing com=ntents form the lists
    if len(id) != 0 :#makes sure the list of ids has entries
        rem = input("ID to remove: ")#asks the user for an id
        if rem in id :#makes sure the id the user has given is present in the list 
            idx = id.index(rem)#finds the index of the id the user has given
            name.pop(idx)#removes the contents of that idex from all the lists 
            rank.pop(idx)
            div.pop(idx)
            id.pop(idx)
            print("Removed.")
        else:
            print("ID doesnt match")
    else:
        print("Invalid action.")

def update_rank():#changes the rank of someone based on their id number
    rid = input("ID to update: ")#asks the user for an id of choice
    if rid in id :
        rids = id.index(rid)#finds the index of the id in the list
        rank.pop(rids)#removes rank from that index
        newRank = input("what is the new Rank: ").title()#asks the user for a different rank to be given 
        if newRank == "Captain" or newRank == "Commander" or newRank == "Lt.Commander" or newRank == "Lieutenant" or newRank == "Ensign": 
            rank.insert(rids, newRank)#inserts the new rank to the idex of the id 
            print("successfully updated")
        else:
            print("invalid rank")
    else:
        print("invlid ID")
    
def display_roster():#responsible for displaying the list 
            print("Current Crew List:")
            for i in range(len(name)):#loops ones for every element in the list of names 
                print(name[i] + " - "  + rank[i] + " - "  + div[i]) #prints the name,rank and division one by one


def search_crew():#resposible for searching for specific terms
    searchTerm = input("search for a term in the crew: ").title()#asks the user for a term to search
    if searchTerm in rank:#checks if the term the user used is in the list
        x = rank.index(searchTerm)#finds the first idex of the search term in the list
        y = rank.count(searchTerm) - 1#findds how many times the search term apears in the list and takes away 1 sisce we already founf the first index
        z = 0
        print(name[x])#prints the name thats on the index function found fist
        while z < y :#loops untill all the istances of the searchterm are found
            x =  rank.index(searchTerm, x + 1)#searches for the next instance of the search term on the list 
            print(name[x]) 
            z += 1 
    elif searchTerm in div:#same thing but works only if the term is in the division list
        x = div.index(searchTerm)
        y = div.count(searchTerm) - 1
        z = 0
        print(name[x]) 
        while z < y :
            x =  div.index(searchTerm, x + 1)
            print(name[x]) 
            z += 1  
    else :
        print("term doesnot exists")

def division_fylter() :#resposible for finding the amount of entris in a specifc devision
    fylteropt = input("what division you want to filter: ").title()
    if fylteropt in div:
        if fylteropt == "Command":
            x = div.index(fylteropt)
            y = div.count(fylteropt) - 1
            z = 0
            print(name[x]) 
            while z < y :
                x =  div.index(fylteropt, x + 1)
                print(name[x]) 
                z += 1  
        elif fylteropt == "Operations":
            x = div.index(fylteropt)
            y = div.count(fylteropt) - 1
            z = 0
            print(name[x]) 
            while z < y :
                x =  div.index(fylteropt, x + 1)
                print(name[x]) 
                z += 1              
        elif fylteropt == "Security":
            x = div.index(fylteropt)
            y = div.count(fylteropt) - 1
            z = 0
            print(name[x]) 
            while z < y :
                x =  div.index(fylteropt, x + 1)
                print(name[x]) 
                z += 1  
        elif fylteropt ==  "Science":
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

def payroll():#resposible for calculating the cost of the crew
    capCost = rank.count("Captain") * 1000 #finds how many times a specific rank apears in the list and multiplyes that number by their respective pay
    commCcost = rank.count("Commander") * 800
    ltcommost = rank.count("Lt.Commander") * 600
    ltCost = rank.count("Lieutenant") * 400
    enCost = rank.count("Ensign") * 200
    cost = capCost + commCcost + ltcommost + ltCost + enCost #adds all the costs
    print("the total cost of the crew is: ", str(cost) + "$")# displays all the costs

def count_officers():#resposible fot coutning how many oficers there are 
    c = rank.count("Captain")#finds how many times the terms captain and commander apear and prints it
    v = rank.count("Commander")
    count = c + v
    print("High ranking officers: ", count)

loading = 0#cosmetic 
while loading < 5 :
    print("System loading" , loading)
    loading += 1
    if loading  == 5 :
        print("Systems online")
init_database()
display_menu()
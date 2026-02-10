# part 1
def init_database():
    n = ["Picard", "Riker", "Data", "La Forge", "Worf"] # the lists with the characters data
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    d = ["Command", "Command", "Operations", "Operations", "Security"]
    i = ["PI1", "RI1", "DA1", "LF1", "WO1"]
    return n, r, d, i

# part 3
def add_member(n, r, d, i): # collecting data ensuring it passes required parameters and in correc format
    new_name = str(input("Name: ")).title()
    new_rank = str(input("Rank: ")).title()
    # Note: removed 'if new_rank in r' to allow multiple officers of the same rank
    new_div = str(input("Division: ")).title()
    new_id = str(input("ID: ")).upper()
    if new_id in i:
        print("Invalid ID Entered.")
        return
    # adding to our roster
    n.append(new_name)
    r.append(new_rank)
    d.append(new_div)
    i.append(new_id)

    print(f"Success, {new_name} has been added to the roster.")

# part 4
def remove_member(n, r, d, i):
    removee = str(input("Enter ID to remove: ")).upper() # ensures the id is entered correctly
    if removee in i:
        idX = i.index(removee) # finding the index
        removed_name = n[idX]

        # removing all other data
        n.pop(idX)
        r.pop(idX)
        d.pop(idX)
        i.pop(idX)

        print(f"Successfully removed {removed_name}, ID: {removee} from the roster.")
    else:
        print(f"Error: ID: {removee} not found - no changes are made.")

# part 5
def update_rank(n, r, d, i):
    update = str(input("Please Enter ID: ")).upper() # finds id and name of crew member
    if update in i:
        ranks = i.index(update)
        current_rank = r[ranks]
        crew_name = n[ranks]

        print(f"Current Rank for {crew_name} : {current_rank}") # prints current information

        new_rank = str(input("Please Enter New Rank: ")).title()
        r[ranks] = new_rank
        print(f"Sucess: {crew_name} has been promoted/demoted to {new_rank}") # prints change
    else:
        print(f"ID: {update} cannot be found.")

# part 6
def display_roster(n, r, d, i):
    print("--- CREW ---")
    for a in range(len(n)): # pulls the no of items in list
        print(f" Name: {n[a]:<15}, Rank: {r[a]:<15}, Division: {d[a]:<15}, ID: {i[a]:<10} ") #prints in an orderly form

# part 7
def search_crew(n, r, d, i):
    searched = str(input("Please Enter Term: ")).title()
    found = False # flagged if we find anyone
    for s in range(len(n)):
        if searched in n[s]:
            print(f"Match Found: {n[s]}, Rank: {r[s]}, Division: {d[s]}, ID: {i[s]}")
            found = True # person found, flag is raised

    if not found: # if no members are found
        print(f"No Members found with {searched}")

# part 8
def filter_by_division(n, r, d, i):
    div_search = str(input("Enter Division (Command, Operations, Security): ")).title()
    found = False # to flag if we find any
    for t in range(len(d)):
        if d[t] == div_search: # checking if we found the member
            print(f"Member Found - Name: {n[t]:<15}, Rank: {r[t]:<15}, Division: {d[t]:<15}, ID: {i[t]:<10}")
            found = True
    if not found:
        print(f"No member found in {div_search} division.") # fail safe

# part 9
def calculate_payroll(n, r):
    total_cost = 0
    for c in range(len(n)):
        ranked = r[c]
        if ranked == "Captain": # assigns salaries based off rank
            salary = 1000 
        elif ranked == "Commander":
            salary = 800
        elif ranked == "Lt. Commander":
            salary = 600
        elif ranked == "Lieutenant":
            salary = 400  
        elif ranked == "Ensign":
            salary = 200        
        else:
            salary = 0
            print(f"Invalid Rank for {n[c]}.")

        print(f"Name: {n[c]:<15}, Rank: {r[c]:<15}, Salary: {salary}") # print salaries
        total_cost += salary # total up the cost
    print(f"Total Cost Spent On Crew: {total_cost}")

# part 10
def count_officers(r):
    captains = 0
    commanders = 0
    lt_commanders = 0
    lieutenants = 0
    ensigns = 0
    for ra in r: # values for each rank
        if ra == "Captain": captains += 1
        elif ra == "Commander": commanders += 1
        elif ra == "Lt. Commander": lt_commanders += 1
        elif ra == "Lieutenant": lieutenants += 1
        elif ra == "Ensign": ensigns += 1
    # final personel count onboard
    print(f"Captains: {captains} | Commanders: {commanders} | Lt. Commanders: {lt_commanders} | Lieutenants: {lieutenants} | Ensigns: {ensigns}")
    print(f"Total Crew: {len(r)}")

# part 2
def display_menu(n, r, d, i): # our display menu showing options to user
    user_name = input("Please enter your full name: ")
    print(f"Welcome {user_name}")
    
    while True: # Added loop to keep menu open
        print("\n--- MENU ---")
        print("1. Add Member\n2. Remove Member\n3. Update Rank\n4. Display Roster")
        print("5. Search Crew\n6. Filter by Divisions\n7. Calculate Payroll\n8. Count Officers\n9. Exit")
        
        opt = input("\nPlease select an option: ")

        if opt == "1": add_member(n, r, d, i)
        elif opt == "2": remove_member(n, r, d, i)
        elif opt == "3": update_rank(n, r, d, i)
        elif opt == "4": display_roster(n, r, d, i)
        elif opt == "5": search_crew(n, r, d, i)
        elif opt == "6": filter_by_division(n, r, d, i)
        elif opt == "7": calculate_payroll(n, r)
        elif opt == "8": count_officers(r)
        elif opt == "9":
            print("Exiting Menu - System Shutdown")
            break

def main():
    n, r, d, i = init_database()
    display_menu(n, r, d, i)

main()
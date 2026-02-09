def main():
    n, r, d, i = init_database() # allows other functions to use the data

    # part 1
    def init_database():
        n = ["Picard", "Riker", "Data", "La Forge", "Worf"] # the lists with the characters data
        r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
        d = ["Command", "Command", "Operations", "Operations", "Operations", "Security"]
        i = ["PI1", "RI1", "DA1", "LF1", "WO1"]
        return n, r, d, i

    # part 2
    def display_menu(): # our display menu showing options to user
        user_name = input("Please enter your full name: ")
        opt = input((f"Welcome {user_name} - please select an option from the menu:"))
        print("\n--- MENU ---")
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Update Rank")
        print("4. Display Roster")
        print("5. Search Crew")
        print("6. Filter by Divisions")
        print("7. Calculate Payroll")
        print("8. Count Officers")
        print("9. Exit")

        if opt == "1": # calling individual functions when neccessary is cleaner than writing out new code everytime
            add_member()
        if opt == "2":
            remove_member()
        if opt == "3":
            update_rank()
        if opt == "4":
            display_roster()
        if opt == "5":
            search_crew()
        if opt == "6":
            filter_by_division()
        if opt == "7":
            calculate_payroll()
        if opt == "8":
            count_officers()
        if opt == "9":
            print("Exiting Menu - System Shutdown")

    def add_member(n,r,d,i): # collecting data ensuring it passes required parameters and in correc format
        new_name = str(input("Name: ")).title()
        new_rank = str(input("Rank: ")).title()
        if new_rank in r:
            print("Invalid Rank Entered.")
            return
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
        
    def remove_member(n,d,r,i):
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


main()

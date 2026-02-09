def main():

    # part 1
    def init_database():
        n = ["Picard", "Riker", "Data", "La Forge", "Worf"] # the lists with the characters data
        r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
        d = ["Command", "Command", "Operations", "Operations", "Operations", "Security"]
        i = ["PI1", "RI1", "DA1", "LF1", "WO1"]
        return n, r, d, i # allows other functions to use the data

    # part 2
    def display_menu():
        user_name = input("Please enter your full name: ")
        print(f"Welcome {user_name} - please select an option from the menu:")
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

main()

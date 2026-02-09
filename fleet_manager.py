def main():

    # part 1
    def init_database():
        n = ["Picard", "Riker", "Data", "La Forge", "Worf"] # the lists with the characters data
        r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant"]
        d = ["Command", "Command", "Operations", "Operations", "Operations", "Security"]
        i = ["PI1", "RI1", "DA1", "LF1", "WO1"]
        return n, r, d, i # allows other functions to use the data


main()

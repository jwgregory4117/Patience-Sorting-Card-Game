from cardSorter import CardSorter

def main():

    rounds = 5
    
    print("Playing {} games.".format(rounds))

    for run in range(rounds):
    
        print("\n=========== Begin Game " + str(run + 1) + " ==========")
        
        sorter = CardSorter()
        sorter.setup()
        sorter.play()
        
        print("=========== End Game " + str(run + 1) + " ==========")

        print("Simulation complete.")
    
main()

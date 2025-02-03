def main():
    while True:
        print("Select game:")
        print("1. BlackJack")
        print("2. Rock Paper Scissors")
        print("3. Fiche Personnage JDR")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            import python_venv.BJ
            python_venv.BJ.play_blackjack()
        elif choice == '2':
            import python_venv.RPS
            python_venv.RPS.play()
        elif choice == '3':
            import python_venv.fiche_perso
            python_venv.fiche_perso.create_character()
        elif choice == '4':
            print("Exiting the game loader.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
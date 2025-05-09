import question_c

def main():
    while True:
        print("\nMenu:")
        print("1 - Find DNA substring")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            dna_string1 = input("Enter the full DNA string (9-1000 characters): ")
            if len(dna_string1) <= 8 or len(dna_string1) > 1000:
                print("DNA string must be more than 8 characters and at most 1000.")
                continue

            dna_string2 = input("Enter a DNA substring of exactly 4 characters: ")
            if len(dna_string2) != 4:
                print("DNA substring must be exactly 4 characters.")
                continue

            positions = question_c.get_most_likely_ancestor_consensus(dna_string1, dna_string2)
            print("Positions:", *positions)
        
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
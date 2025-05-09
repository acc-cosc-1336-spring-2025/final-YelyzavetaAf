import question_d

def main():
    while True:
        print("\nMenu:")
        print("1 - Display multiplication table")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table = question_d.create_multiplication_table()
            question_d.display_multiplication_table(table)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()



    
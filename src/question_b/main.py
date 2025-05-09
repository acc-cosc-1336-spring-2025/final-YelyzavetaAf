import question_b

def main():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_list = question_b.get_stock_list()
            print(f"{'Company':<20} {'Symbol'}")
            print("-" * 35)
            for stock in stock_list:
                print(f"{stock.get_company_name():<20} {stock.get_symbol()}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()


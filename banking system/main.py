from check_balance import check_balance
from create_account import create_account
from deposit import deposit
from withdraw import withdraw



def main():
    print("Welcome to yab's banking system in python")
    print("Select an Option")
    print("1. Create an account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    try: 
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            print("bbye bugok")
        else:
            print("bobo wala sa choices")
    except ValueError:
        print("tanga tanga mo naman men")


    replay = input("o ano isa pa? (y/n): ").lower().strip()
    try:
        if replay == "y":
            main()
        elif replay == "n":
            print("bbye bugok")
        else:
            print("bobo makinig kasa instructions")
    except ValueError:
        print("bobo makinig kasa instructions")



if __name__ == "__main__":
    main()
from add_client import add_client
from create_campaign import create_campaign
from generate_report import generate_report
from track_campaign import track_campaign


def main():
    while True:
        print("\nWelcome to digital marketing")
        print("1. Add client")
        print("2. Create campaign")
        print("3. Track Campaign Report")
        print("4. Generate report")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if not choice:
                print("Please enter a valid choice")
                continue

            if choice == 1:
                add_client()
            elif choice == 2:    
                create_campaign()
            elif choice == 3:
                track_campaign()
            elif choice == 4:
                generate_report()
            elif choice == 5:
                print("Exiting from digital marketing")
                break
            else:
                print("Please enter a valid choice else")
        except ValueError:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()
        


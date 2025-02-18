accounts = {}

def create_account():
    try:
        name = input("enter ur name bitch: ")
        balance = float(input("ilan pera lalagay mo men: "))
        if balance < 0:
            print("bawal mababa sa zero men")
            return
        
        account_number = len(accounts) + 1001
        accounts[account_number] = {"name": name, "balance": balance}
        print(f"tapos na account mo men, account number mo ay {account_number}.")
    except ValueError:
        print("tanga dapat number lang yan")

        
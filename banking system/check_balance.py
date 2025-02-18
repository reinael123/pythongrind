from create_account import accounts

def check_balance():
    try:
        account_number = int(input("ano account number mo: "))
        if account_number not in accounts:
            print("tanga gawa ka muna account.")
            return
        
        print(f"yung balance mo ay {accounts[account_number]['balance']}.")
    except ValueError:
        print("tanga mo naman talaga men, dapat number yan")
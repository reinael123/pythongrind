from create_account import accounts

def deposit():
    try:
        account_number = int(input("ano muna account number mo: "))
        if account_number not in accounts:
            print("tanga mo naman gawa ka muna account")
            return
        
        amount = float(input("magkano papasok mo men: "))
        if amount < 0:
            print("tanga wala ka naman pera e")
            return
        
        accounts[account_number]["balance"] += amount
        print(f"ang bagong mong balance as {accounts[account_number]['balance']}")
    except ValueError:
        print("bobo mo talaga men, number lang dapat")
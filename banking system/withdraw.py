from create_account import accounts

def withdraw():
    try: 
        account_number = int(input("ano muna account number mo: "))
        if account_number not in accounts:
            print("tanga mo naman gawa ka muna account")
            return

        amount = float(input("magkano papasok mo men mo men: "))
        if amount < 0:
            print("tanga wala ka naman pera e")
            return

        if accounts[account_number]['balance'] < amount:
            print("tanga wala ka naman pera e")

        accounts[account_number]["balance"] -= amount
        print(f"ay wow may pera kana, ang bago mong pera ay {accounts[account_number]}")
    except ValueError:
        print("bobo mo talaga")
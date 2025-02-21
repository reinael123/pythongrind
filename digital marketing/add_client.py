from data import clients

def add_client():
    try:
        client_id = int(input("Enter client id: "))
        if client_id in clients:
            print("Client ID already exists. Please choose a different ID.")
            return
        
        name = input("Enter client name: ")
        email = input("Enter client email: ")
        clients[client_id] = {"name": name, "email": email}
        print("Client added successfully")
    except ValueError:
        print("Invalid input. Enter numeric number only")
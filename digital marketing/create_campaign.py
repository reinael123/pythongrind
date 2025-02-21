from data import clients, campaigns

def create_campaign():
    try:
        campaign_id = int(input("Please enter campaign id: "))
        if campaign_id in campaigns:
            print("campaign already exists: ")
            return
        
        client_id = int(input("Enter client id: "))
        if client_id not in clients:
            print("Client not found. Please check the client ID.")
            return
        
        name = input("Please enter your campaign name: ")
        impressions = int(input("please enter initial impressions"))
        clicks = int(input("please enter initial clicks"))
        conversations = int(input("please enter initial conversations"))

        campaigns[campaign_id] ={       #nag aadd ka ng key value pair sa campaigns na data#
            "name": name,
            "impressions": impressions,
            "clicks": clicks,
            "conversations": conversations
        }
        print("campaign added successfully ")
    except ValueError:
        print("invalid input.")

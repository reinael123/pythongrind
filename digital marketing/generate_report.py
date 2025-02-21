from data import clients, campaigns

def generate_report():
    try:
        campaign_id = int(input("Please enter campaign id: "))
        if campaign_id not in campaigns:
            print("wala yan, gawa ka muna ")
            return
        
        campaign = campaigns[campaign_id]
        print("\nCampaign Report: ")
        print(f"- Campaign name: {campaign['name']}")
        print(f"- Conversations: {campaign['conversations']}")
        print(f"- Clicks: {campaign['clicks']}")
        print(f"- Impressions: {campaign['impressions']}")
    except ValueError:
        print("Invalid Choice")
        

        
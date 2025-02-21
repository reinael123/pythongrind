from data import campaigns, clients

def track_campaign():
    try:
        campaign_id = int(input("Please enter campaign id: "))
        if campaign_id not in campaigns:
            print("wala yan, gawa ka muna ")
            return
        
        impressions = int(input("please enter initial impressions: "))
        clicks = int(input("please enter initial clicks: "))
        conversations = int(input("please enter initial conversations: "))

        campaigns[campaign_id]["impressions"] = impressions
        campaigns[campaign_id]["clicks"] = clicks
        campaigns[campaign_id]["conversations"] = conversations
        print("Campaign performance updated successfully!")
    except ValueError:
        print("Invalid Choice")
    
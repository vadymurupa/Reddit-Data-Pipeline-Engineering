from praw import Reddit

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent)
        print("Reddit connected.")
        return reddit
    except Exception as e:
        print(e, "Not connected. ")
        sys.exit(1)
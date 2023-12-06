from utils.constants import CLIENT_ID
from utils.constants import SECRET

def reddit_pipeline(file_name:str, subreddit:str, time_filter="day", limit=None):
    # Connecting to Reddit instance ( extraction, transformation, loading to csv. )
    instance = connect_reddit(CLIENT_ID, SECRET, "Airscholar agent")
    
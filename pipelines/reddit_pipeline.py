from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, transform_data, load_data_to_csv
import pandas as pd

def extract_posts(file_name:str, subreddit:str, time_filter="day", limit=None):
    # Connecting to Reddit instance ( extraction, transformation, loading to csv. )
    instance = connect_reddit(CLIENT_ID, SECRET, "Airscholar agent")
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)
    
    load_data_to_csv(post_df, path:f"OUTPUT_PATH/{file_name}.csv")
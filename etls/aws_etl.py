import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY
def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_SECRET_KEY)
        return s3
    except Exception as e:
        print(e)
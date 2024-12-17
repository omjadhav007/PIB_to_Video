from save_latest_videos import *

def is_present_in_db(id):
    if id==2085482:
        return True
    return False

save_videos(is_present_in_db)



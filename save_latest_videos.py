from avatarVideoGeneration import *
from web_scrapping import *

# def present_in_db(id):
#     return False

def save_videos(present_in_db,image_list_path="image_list.txt"):
    ids=scrap_ids(present_in_db)
    # print(ids)
    data=scrap_data_and_summarize(ids)
    # print(data)

    for i in range(len(data['summary'])):
        file_name=data['id'][i]
        script=data['summary'][i]
        video_path="video\\"+file_name+".mp4"
        audio_path="audio\\"+file_name+".wav"
        final_output_path="output_video\\"+file_name+".mp4"
        generate_audio(script,audio_path)
        word_timestamps=word_durations(audio_path)
        create_image_list(image_list_path,word_timestamps)
        generate_video(video_path,image_list_path)
        combine_audio_video(video_path,audio_path,final_output_path)

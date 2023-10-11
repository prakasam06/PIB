import subprocess
import requests
import os
import asyncio


API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"
headers = {"Authorization": "Bearer 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"}

from transformers import pipeline

def sentiment_analysis(data):
    # Load the sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")

    # Define the sentiment labels
    sentiment_labels = {'POS': 'POSITIVE', 'NEU': 'NEUTRAL', 'NEG': 'NEGATIVE'}

    result_list = []
    
    for i in sentiment_pipeline(data):
        sentiment_label = i['label']
        sentiment_score = i['score']
        
        # Calculate sentiment scores
        positive_score = round(sentiment_score * 100, 2)
        neutral_score = round(((1.0 - sentiment_score) / 2) * 100, 2)
        negative_score = round(((1.0 - sentiment_score) / 2) * 100, 2) / 2
        
        # Create a dictionary with sentiment scores
        sentiment_dict = {
            'SENTIMENT_LABEL': sentiment_labels[sentiment_label],
            'POSITIVE': positive_score,
            'NEUTRAL': neutral_score,
            'NEGATIVE': negative_score
        }
        
        result_list.append(sentiment_dict)
    
    return result_list





def crop_video(input_video_path, start_time,end_time,output_filename):
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    # Trim the video
    ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname="trimed_video/" + output_filename)
    

url = "https://www.youtube.com/watch?v=LVW_vr6ELJ8"

def youtube_video_trimming_process(video_url):
    
    from youtube_transcript_api import YouTubeTranscriptApi
    import pandas as pd
    
    indian_languages_interchanged = {"Bangla": "bn", "Bhojpuri": "bho", "Gujarati": "gu", "Hindi": "hi", "Kannada": "kn", "Malayalam": "ml", "Marathi": "mr", "Nepali": "ne", "Odia": "or", "Punjabi": "pa", "Sanskrit": "sa", "Tamil": "ta", "Telugu": "te", "Urdu": "ur"}
    all_languages = {'Afrikaans': 'af', 'Akan': 'ak', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Assamese': 'as', 'Aymara': 'ay', 'Azerbaijani': 'az', 'Bangla': 'bn', 'Basque': 'eu', 'Belarusian': 'be', 'Bhojpuri': 'bho', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Burmese': 'my', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chinese (Simplified)': 'zh-Hans', 'Chinese (Traditional)': 'zh-Hant', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Divehi': 'dv', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Ewe': 'ee', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'Ganda': 'lg', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Guarani': 'gn', 'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Kinyarwanda': 'rw', 'Korean': 'ko', 'Krio': 'kri', 'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lingala': 'ln', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Māori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Nepali': 'ne', 'Northern Sotho': 'nso', 'Norwegian': 'no', 'Nyanja': 'ny', 'Odia': 'or', 'Oromo': 'om', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Quechua': 'qu', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Sanskrit': 'sa', 'Scottish Gaelic': 'gd', 'Serbian': 'sr', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Southern Sotho': 'st', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te', 'Thai': 'th', 'Tigrinya': 'ti', 'Tsonga': 'ts', 'Turkish': 'tr', 'Turkmen': 'tk', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Western Frisian': 'fy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}

    video_id = video_url.split("=")[1]
    # retrieve the available transcripts
    
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
   
        # iterate over all available transcripts
        for transcript in transcript_list:
            # whether it has been manually created or generated by YouTube
            transcript.video_id,
            detected_lan = transcript.language_code,
            # whether this transcript can be translated or not
            transcript.is_translatable
            
            actual_subtitle = transcript.fetch()   
            
        subtitle_dict = {}
        subtitle_dict["subtitle"] = [ i["text"] for i in actual_subtitle]
        subtitle_dict["start_time"] = [ i["start"]  for i in actual_subtitle]
        subtitle_dict["end_time"] = [ i["start"] + i["duration"] for i in  actual_subtitle]


        sentiment_analysis_result = sentiment_analysis(list(subtitle_dict["subtitle"]))    
        subtitle_dict['POSITIVE'] = [ i['POSITIVE'] for i in sentiment_analysis_result]
        subtitle_dict['NEUTRAL'] = [ i['NEUTRAL'] for i in sentiment_analysis_result]
        subtitle_dict['NEGATIVE'] = [ i['NEGATIVE'] for i in sentiment_analysis_result]
        subtitle_dict['SENTIMENT_ANALYSIS_RESULT'] = [ i['SENTIMENT_LABEL']  for i in sentiment_analysis_result]


        video_analysis_dataframe = pd.DataFrame(subtitle_dict)
        print(video_analysis_dataframe)
        video_analysis_dataframe_neg = video_analysis_dataframe.query('SENTIMENT_ANALYSIS_RESULT == "NEG"')
        r = video_analysis_dataframe_neg
        # spliting_negative_clip(video_url,r)
        return video_analysis_dataframe
    except Exception as e:
        print("errorrrrrrrrrrrrrrrrrrr === ",str(e))    
        print("Subtitles are disabled for this video")
        
   

r = youtube_video_trimming_process(url)
    

def spliting_negative_clip(url,r):

    from tqdm import tqdm
    # global r  
    import yt_dlp


    ydl_opts = {
        'age_limit': 18,
        'outtmpl': 'downloaded_youtube_video/downloaded_video.mp4' 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


    list_trim_video = list(zip(r["start_time"],r["end_time"]))
    

    if len(list_trim_video) == 1:
        for i,j in tqdm(enumerate(list_trim_video)):
            
            crop_video("downloaded_youtube_video/downloaded_video.mp4",start_time=j[0],end_time=j[1],output_filename="video_" + str(i+1) + ".mp4")
            
        crop_video("downloaded_youtube_video/downloaded_video.mp4",start_time=0,end_time=list(r["end_time"])[-1],output_filename="full_video.mp4")

        os.remove("downloaded_youtube_video/downloaded_video.mp4")
        print("successfully!!!!!!!!!")
        

# spliting_negative_clip(url=url,r=r)
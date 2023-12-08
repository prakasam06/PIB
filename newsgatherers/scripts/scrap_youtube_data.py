import pandas as pd
from tqdm import tqdm


channel_name_list = ["indiatoday","cnnnews18","timesofindia","TheEconomicTimes","TimesNow"]
def youtube_video_scrape(channel_name):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    # from pprint import pprint as pp
    import pandas as pd
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.youtube.com/@" + channel_name + "/videos")

    channel_title = driver.find_element(By.XPATH, '//yt-formatted-string[contains(@class, "ytd-channel-name")]').text
    handle = driver.find_element(By.XPATH, '//yt-formatted-string[@id="channel-handle"]').text
    subscriber_count = driver.find_element(By.XPATH, '//yt-formatted-string[@id="subscriber-count"]').text
    thumbnails = driver.find_elements(By.XPATH, '//a[@id="thumbnail"]/yt-image/img')
    views = driver.find_elements(By.XPATH,'//div[@id="metadata-line"]/span[1]')
    titles = driver.find_elements(By.ID, "video-title")
    links = driver.find_elements(By.ID, "video-title-link")
    pub_times = driver.find_elements(By.XPATH, '//div[@id="metadata-line"]/span[2]')
    durations = driver.find_elements(By.XPATH, '//span[@class="style-scope ytd-thumbnail-overlay-time-status-renderer"]')


    videos_df = []
    for title, view, thumb, link, pub_time,duration in zip(titles, views, thumbnails, links, pub_times,durations):
        video_dict = {
            'title': title.text,
            'views': view.text,
            'thumbnail': thumb.get_attribute('src'),
            'link': link.get_attribute('href'),
            'published_time_ago': pub_time.text,
            'duration_of_video': duration.text
        }
        videos_df.append(pd.DataFrame([video_dict]))

    d = pd.concat(videos_df)
    return d
    

def scrap_data_from_youtube():
    df_list = []
    for df in tqdm(channel_name_list):
        data = youtube_video_scrape(df)
        print('im not error')
        data["channel_name"] = [ df for i in range(len(data))]
        print('im not error')
        df_list.append(data)
        
    d = pd.concat(df_list)
    d['type_of_platform'] = [ "youtube" for i in range(len(d))]
    
    return d

from tqdm import tqdm
from multiprocessing import Pool
from tqdm import tqdm
import pandas as pd
from newspaper import Article
import json
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

def time_age_function(publist_date):
    from datetime import datetime

    # Define the target datetime
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # target_datetime = datetime.strptime(publist_date, date_format)
    target_datetime = publist_date

    # Get the current datetime
    current_datetime = datetime.now()

    # Calculate the time difference
    time_difference = current_datetime - target_datetime

    # Extract the time difference components (days, seconds, etc.)
    days = time_difference.days
    seconds = time_difference.seconds

    # Calculate hours, minutes, and remaining seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Print the time difference
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds ago"
    
def get_summary_of_particular_news(url):
    
    final_dict = {}
    toi_article = Article(url, language="en") # en for English

    #To download the article
    toi_article.download()

    #To parse the article
    toi_article.parse()

    #To perform natural language processing ie..nlp
    toi_article.nlp()
    
    #To extract title
    # final_dict['Title'] = toi_article.title
  
    #  "Article's image:"
    final_dict['Image'] = toi_article.top_image

    #To extract text Article's Text:
    final_dict['main_text'] = toi_article.text
   
    #To extract summary Article's Summary:
    final_dict['Summary_article'] = toi_article.summary
    # final_dict['keywords_article'] = toi_article.keywords


    # Article's publish_date:"
    # final_dict['publish_date'] = toi_article.publish_date
    

    
    return final_dict

def clustering_news_data_scrape_function(news_tittle,language,max_results,past_no_of_hours):
    
    from gnews import GNews
    import pandas as pd
    from datetime import datetime  
    
    date_format = "%a, %d %b %Y %H:%M:%S GMT"

    google_news = GNews()
    google_news.period =  str(past_no_of_hours)+ 'h'  # News from last 7 days
    google_news.max_results = max_results  # number of responses across a keyword
    google_news.country = 'India'  # News from a specific country 
    google_news.language = language  # News in a specific language
    google_news.exclude_websites = ['yahoo.com', 'cnn.com']
    json_resp = google_news.get_news(news_tittle + " when:"+str(past_no_of_hours)+"h")
    youtube_json_resp = google_news.get_news(news_tittle + " site:https://www.youtube.com" + " when:"+str(past_no_of_hours)+"h")
    
    if len(youtube_json_resp) != 0:
        val_d = [ pd.DataFrame([i]) for i in youtube_json_resp]
        youtube_df = pd.concat(val_d)
        youtube_df['publisher'] = [ i['title']  for i in youtube_df['publisher']]
        youtube_df['published date']  = [ datetime.strptime(i, date_format) for i in youtube_df['published date']]
        youtube_df["published time ago"] = [ time_age_function(i)  for i in youtube_df['published date']]
        youtube_df['published date'] = pd.to_datetime(youtube_df['published date'])
        youtube_df.sort_values('published date',ascending=False)
        youtube_df.columns = ['youtube_title','youtube_description','youtube_published_date','youtube_url','youtube_publisher','youtube_published_time_ago']
    else:
        youtube_df = pd.DataFrame()
    
    json_resp_gnews = []  
    for i in json_resp:
        val = i
        val['url'] = val['url'].replace("rss/","") 
        json_resp_gnews.append(val)

    
    
    if len(json_resp_gnews) != 0:
        d = []
        
        for dis_1 in json_resp_gnews:
             
            try :
                particular_url_data = get_summary_of_particular_news(dis_1['url'])
                split_list = particular_url_data['main_text'].split(".") 
                split_list_analysis = sentiment_analysis(split_list)
                
                dict_analysis = { i:j['SENTIMENT_LABEL'] for i,j in zip(split_list,split_list_analysis)}                      
        
                particular_url_data['positive_sentence'] = [ i for i,j in dict_analysis.items() if j == 'POSITIVE' ]
                particular_url_data['neutral_sentence'] = [ i for i,j in dict_analysis.items() if j == 'NEUTRAL' ]
                particular_url_data['negative_sentence'] = [ i for i,j in dict_analysis.items() if j == 'NEGATIVE' ]
                
                dis_1.update(particular_url_data)
                dataframe_dis = pd.DataFrame([dis_1])
                
                if dataframe_dis is not None:
                    d.append(dataframe_dis)
                    
            except:
                dis_1.update({'Image':i['title'], 'main_text': 'none', 'Summary_article': i['title'],'positive_sentence': 'none','neutral_sentence': 'none','negative_sentence': 'none'})
                dataframe_dis = pd.DataFrame([dis_1])
                
                if dataframe_dis is not None:
                    d.append(dataframe_dis)
               
        df = pd.concat(d)
        df['publisher'] = [ i['title']  for i in df['publisher']]
        df['published date']  = [ datetime.strptime(i, date_format) for i in df['published date']]
        df["published time ago"] = [ time_age_function(i)  for i in df['published date']]
        df['published date'] = pd.to_datetime(df['published date'])
        df.sort_values('published date',ascending=False)
        
        return df,youtube_df
    else:
        return pd.DataFrame(),youtube_df
  

def state_wise_news_for_each_department(state,department,language,max_results,past_no_of_hours):
    
    from gnews import GNews
    import pandas as pd
    from datetime import datetime  
    
    date_format = "%a, %d %b %Y %H:%M:%S GMT"

    google_news = GNews()
    google_news.period =  str(past_no_of_hours)+ 'h'  # News from last 7 days
    google_news.max_results = max_results  # number of responses across a keyword
    google_news.country = 'India'  # News from a specific country 
    google_news.language = language  # News in a specific language
    google_news.exclude_websites = ['yahoo.com', 'cnn.com']
    json_resp = google_news.get_news( department + " for Government of " + state + " when:"+str(past_no_of_hours)+"h")
    json_resp_gnews = []  
    for i in json_resp:
        val = i
        val['url'] = val['url'].replace("rss/","") 
        json_resp_gnews.append(val)
        
    if len(json_resp_gnews) != 0:
        d = []
        
        for dis_1 in json_resp_gnews:
            
            try:
                particular_url_data = get_summary_of_particular_news(dis_1['url'])
                split_list = particular_url_data['main_text'].split(".") 
                split_list_analysis = sentiment_analysis(split_list)
                dict_analysis = { i:j['SENTIMENT_LABEL'] for i,j in zip(split_list,split_list_analysis)}                      
        
                particular_url_data['positive_sentence'] = [ i for i,j in dict_analysis.items() if j == 'POSITIVE' ]
                particular_url_data['neutral_sentence'] = [ i for i,j in dict_analysis.items() if j == 'NEUTRAL' ]
                particular_url_data['negative_sentence'] = [ i for i,j in dict_analysis.items() if j == 'NEGATIVE' ]
                
                dis_1.update(particular_url_data)
                dataframe_dis = pd.DataFrame([dis_1])
                
                
                if dataframe_dis is not None:
                    d.append(dataframe_dis)
                    
            except:
                
                dis_1.update({'Image':i['title'], 'main_text': 'none', 'Summary_article': i['title'],'positive_sentence': 'none','neutral_sentence': 'none','negative_sentence': 'none'})
                dataframe_dis = pd.DataFrame([dis_1])
                
                if dataframe_dis is not None:
                    d.append(dataframe_dis)
       
                  
        df = pd.concat(d)
        df['publisher'] = [ i['title']  for i in df['publisher']]
        df['published date']  = [ datetime.strptime(i, date_format) for i in df['published date']]
        df["published time ago"] = [ time_age_function(i)  for i in df['published date']]
        df['published date'] = pd.to_datetime(df['published date'])
        df.sort_values('published date',ascending=False)
        df['State'] = [ state for i in range(len(df))]
        df['Department'] = [ department for i in range(len(df))]
        
        website_data,youtube_data = clustering_news_data_scrape_function(news_tittle=dis_1['title'],language="english", max_results=15, past_no_of_hours=15)
        list_website_data_clustering = [ ]
        list_youtube_data_clustering = [ ]
        
        for i in df['title']:
            w,y = clustering_news_data_scrape_function(news_tittle=i,language="english", max_results=15, past_no_of_hours=15)
            w = w.to_json(orient='records')
            y = y.to_json(orient='records')
            list_website_data_clustering.append(w)
            list_youtube_data_clustering.append(y)
            
        df['website_data_clustering'] = list_website_data_clustering
        df['youtube_data_clustering'] = list_youtube_data_clustering

        return df
    else:
        return []
 





states_list = ['Delhi', 'Mumbai', 'Hyderabad', 'Chennai', 'Chandigarh', 'Kolkata', 'Bengaluru', 'Bhubaneswar', 'Ahmedabad', 'Guwahati', 'Thiruvananthpuram', 'Imphal', 'Aizawl', 'Agartala', 'Gangtok', 'Kohima', 'Shillong', 'Itanagar', 'Lucknow', 'Bhopal', 'Jaipur', 'Patna', 'Ranchi', 'Shimla', 'Raipur']
text_content = ["President's Secretariat", "Vice President's Secretariat", "Prime Minister's Office", "Cabinet", "Cabinet Committee Decisions", "Cabinet Committee on Economic Affairs (CCEA)", "Cabinet Secretariat", "Cabinet Committee on Infrastructure", "Cabinet Committee on Price", "Cabinet Committee on Investment", "AYUSH", "Other Cabinet Committees", "Department of Space", "Department of Ocean Development", "Department of Atomic Energy", "Election Commission", "Finance Commission", "Ministry of Agriculture & Farmers Welfare", "Ministry of Agro & Rural Industries",  "Ministry of Chemicals and Fertilizers", "Ministry of Civil Aviation", "Ministry of Coal", "Ministry of Commerce & Industry", "Ministry of Communications", "Ministry of Company Affairs", "Ministry of Consumer Affairs, Food & Public Distribution", "Ministry of Cooperation", "Ministry of Corporate Affairs", "Ministry of Culture", "Ministry of Defence", "Ministry of Development of North-East Region", "Ministry of Disinvestment", "Ministry of Drinking Water & Sanitation", "Ministry of Earth Sciences", "Ministry of Education", "Ministry of Electronics & IT", "Ministry of Environment, Forest and Climate Change", "Ministry of External Affairs", "Ministry of Finance", "Ministry of Fisheries, Animal Husbandry & Dairying", "Ministry of Food Processing Industries", "Ministry of Health and Family Welfare", "Ministry of Heavy Industries", "Ministry of Home Affairs", "Ministry of Housing & Urban Affairs", "Ministry of Information & Broadcasting", "Ministry of Jal Shakti", "Ministry of Labour & Employment", "Ministry of Law and Justice", "Ministry of Micro, Small & Medium Enterprises", "Ministry of Mines", "Ministry of Minority Affairs", "Ministry of New and Renewable Energy", "Ministry of Overseas Indian Affairs", "Ministry of Panchayati Raj", "Ministry of Parliamentary Affairs", "Ministry of Personnel, Public Grievances & Pensions", "Ministry of Petroleum & Natural Gas", "Ministry of Planning", "Ministry of Power", "Ministry of Railways", "Ministry of Road Transport & Highways", "Ministry of Rural Development", "Ministry of Science & Technology", "Ministry of Ports, Shipping and Waterways", "Ministry of Skill Development and Entrepreneurship", "Ministry of Social Justice & Empowerment", "Ministry of Statistics & Programme Implementation", "Ministry of Steel", "Ministry of Surface Transport", "Ministry of Textiles", "Ministry of Tourism", "Ministry of Tribal Affairs", "Ministry of Urban Development", "Ministry of Water Resources, River Development and Ganga Rejuvenation", "Ministry of Women and Child Development", "Ministry of Youth Affairs and Sports", "NITI Aayog", "PM Speech", "EAC-PM", "UPSC", "Special Service and Features", "PIB Headquarters", "Office of Principal Scientific Advisor to GoI", "National Financial Reporting Authority", "Competition Commission of India", "IFSC Authority", "National Security Council Secretariat"]
    


# Define your functions (time_age_function and state_wise_news_for_each_department) here...

def collect_data_for_state(state):
    global text_content
    final_dataframe_list = []
    for department in text_content:
        result = state_wise_news_for_each_department(state=state, department=department, language="english", max_results=5, past_no_of_hours=2)
        if len(result) != 0:
            final_dataframe_list.append(result)
    return final_dataframe_list

if __name__ == '__main__':

    # Number of processes to run concurrently
    num_processes = 6  # You can adjust this based on your system's capabilities
    
    with Pool(num_processes) as pool:
        results = list(tqdm(pool.imap(collect_data_for_state, states_list), total=len(states_list)))
    
    final_dataframe_list = [item for sublist in results for item in sublist if len(item) != 0]
    
    final_data = pd.concat([i for i in final_dataframe_list], ignore_index=True)
    
    sentiment_analysis_result = sentiment_analysis(final_data['description'].tolist())
    final_data['POSITIVE'] = [ i['POSITIVE'] for i in sentiment_analysis_result]
    final_data['NEUTRAL'] = [ i['NEUTRAL'] for i in sentiment_analysis_result]
    final_data['NEGATIVE'] = [ i['NEGATIVE'] for i in sentiment_analysis_result]
    final_data['SENTIMENT_ANALYSIS_RESULT'] = [ i['SENTIMENT_LABEL']  for i in sentiment_analysis_result]
            
    final_data.to_csv("final_data.csv",index=False)
    

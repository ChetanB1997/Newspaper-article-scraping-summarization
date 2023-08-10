from scrap import extract_article_data
import pandas as pd
import os.path
from convert import lang_convert
from summarize import summarize_text

url = "https://www.chinanews.com.cn/sh/2023/08-02/10054412.shtml"
data = extract_article_data(url)
# Create a DataFrame with the extracted data
df = pd.DataFrame([data])
# Save the DataFrame to a CSV file
df.to_csv(os.path.join('scrap_newspaper', 'article_data.csv'))


url2 = 'scrap_newspaper/article_data.csv'
l = lang_convert(url2)
df_new = pd.DataFrame(columns = ['Translated_Text'])
df_new['Translated_Text'] = l
df_new.to_csv(os.path.join('converted_data', 'data.csv'))


df = pd.read_csv('converted_data/data.csv')
df = df.drop('Unnamed: 0', axis=1)
df['summary'] = df['Translated_Text'].apply(summarize_text)
df.to_csv(os.path.join('summarize_data', 'data.csv'))

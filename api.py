# main.py
from fastapi import FastAPI, HTTPException
import validators
import pandas as pd
import os.path
from scrap import extract_article_data
from convert import lang_convert
from summarize import summarize_text

app = FastAPI()

@app.get("/process_url/")
def process_url(url: str):
    # Validate the URL
    if not validators.url(url):
        raise HTTPException(status_code=400, detail="Invalid URL")

    # Extract article data from the URL
    data = extract_article_data(url)

    # Create a DataFrame with the extracted data
    df = pd.DataFrame([data])

    # Save the DataFrame to a CSV file
    df.to_csv(os.path.join('scrap_newspaper', 'article_data.csv'))

    # Convert the data to another language
    url2 = 'scrap_newspaper/article_data.csv'
    l = lang_convert(url2)
    df_new = pd.DataFrame(columns=['Translated_Text'])
    df_new['Translated_Text'] = l
    df_new.to_csv(os.path.join('converted_data', 'data.csv'))

    # Summarize the text
    df = pd.read_csv('converted_data/data.csv')
    df = df.drop('Unnamed: 0', axis=1)
    df['summary'] = df['Translated_Text'].apply(summarize_text)
    df.to_csv(os.path.join('summarize_data', 'data.csv'))

    return {"message": "Processing completed successfully", "summary": df['summary'].tolist()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

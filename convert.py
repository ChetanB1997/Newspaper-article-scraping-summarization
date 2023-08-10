from transformers import pipeline
import pandas as pd
import os.path


def lang_convert(url):
    ll = []
    df = pd.read_csv(url)
    df = df['Text'].dropna()
    new_df = df.drop_duplicates()
    text_list = new_df.tolist()
    # print("****************************************************************")
    df_new = pd.DataFrame(columns = ['Translated_Text'])
    for text in text_list:
      # print(text)
        model_checkpoint = "Helsinki-NLP/opus-mt-mul-en"
        translator = pipeline("translation", model=model_checkpoint)

        # Define the maximum sequence length
        max_length = 512

        # Split the input text into smaller segments
        segments = [text[i:i+max_length] for i in range(0, len(text), max_length)]

        # Translate each segment and store the results in a list
        translated_texts = []
        for segment in segments:
            result = translator(segment)
            translated_texts.append(result[0]['translation_text'])

        ll.append([''.join(translated_texts)])
    return ll

if __name__ == "__main__":
    lang_convert()


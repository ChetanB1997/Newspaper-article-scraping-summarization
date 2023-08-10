import pandas as pd
from transformers import pipeline
import os.path

# # Create a summarization pipeline using Hugging Face transformers

# Function to summarize the text
def summarize_text(text):
    summarizer = pipeline(task='summarization')
    return summarizer(text, max_length=500, min_length=50, do_sample=False)[0]['summary_text']


if __name__ == "__main__":
    summarize_text()

#import libraries
import streamlit as st
from transformers import pipeline
import pandas as pd


# Creating a color evaluation for the response results
def color_evaluation(val):
    color = "green" if val == "POSITIVE" else "red"
    return f"color: {color}"

# loading in the hugging face model
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model = "distilbert-base-uncased-finetuned-sst-2-english")

classifier = load_model()

# create the title and placeholder text on the frontend
st.title("User Behavior Analyzer")
user_input = st.text_area("Enter 5 comments to analyze" ,placeholder = "Place one comment per line...")

# create the button for the frontend and the logic behind it
if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter at least one comment before analyzing")
   #split into individual comments and remove empty lines
    else:
        comments = user_input.splitlines()
        comments = [c for c in comments if c.strip()]
    
    # run each comment through the sentiment model
        results = classifier(comments)
        
    # build a dataframe with the comment, sentiment model and confidence score  
        df = pd.DataFrame({
         "Comment": comments,
            "Sentiment": [r['label'] for r in results],
            "Confidence": [r['score'] for r in results]
     })
        
    #display the results table color coded  
        st.dataframe(df.style.map(color_evaluation, subset = ['Sentiment']))
        
    #display summary line
        positive = (df["Sentiment"] == "POSITIVE").sum()
        total = len(df)
        st.markdown(f"** {positive} out of {total} comments are POSITIVE**")

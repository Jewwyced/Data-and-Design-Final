# User Behavior Analyzer

## How to run
pip install -r requirements.txt
streamlit run app.py
(first run downloads the model)

# About
The hardest part about this project was to commit to one model and idea. At first I wanted to do a more ui/ux model, something that can take a basic description and from there recommend a color palette, font style and CSS. I tried to pursue this idea with a model from a hugging face but quickly learned that the model wasn’t strong enough. The responses were basic and not interesting enough, which led me to my second and final design.

I used a model that differentiates positive and negative responses. It’s a frequently used model on Hugging Face called DistilBERT base uncased finetuned SST-2. The model is simple, you feed it sentences such as “I love life” or “I dislike apples” and it will in turn tell you whether your response is positive or negative. This project is contextualized by a UX/UI user behavior dataset from Mendeley Data containing 2,271 entries capturing user sentiment and satisfaction across platforms like Twitter, YouTube, and Facebook.

I have also included `flan.py` in this repository which documents my initial attempt with flan-t5-base and flan-t5-large before pivoting to DistilBERT.

So from there I created a basic Streamlit site with a title, a button and some placeholder text. There's a text box to input 5 sentences. From there the machine can detect the positive from the negative and return the results. It gives you a summary of the scores, clearly telling you what the results are and even has the positive and negative color coded. 

It’s a simple web application but uses a very effective model. This was a great learning experience, to be able to move from one idea to another, one model to the other and eventually bring my idea to life.

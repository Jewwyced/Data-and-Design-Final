from transformers import pipeline

generator = pipeline("text2text-generation", model = "google/flan-t5-large")

prompt = "As a UI designer, list colors, fonts, and CSS for a tropical vacation booking app:"

result = generator(prompt, max_new_tokens = 200)

print(result)

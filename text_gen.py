from transformers import pipeline

model = pipeline("text-generation")

print(model("I like AI because"))
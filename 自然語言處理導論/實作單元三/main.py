from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn.functional as F
from datasets import load_dataset
import pyttsx3

new_model = BertForSequenceClassification.from_pretrained(r'C:\Users\whitecloud\Documents\code\yuntech_HW\自然語言處理導論\實作單元三\saved_model')
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
labels = sorted(set([item['label'] for item in load_dataset("json", data_files='train'+'.json', split='train')]))

def ask_question(question_text):
    encoded_input = tokenizer(question_text, return_tensors='pt')


    with torch.no_grad():
        output = new_model(**encoded_input)
        logits = output.logits


    probabilities = F.softmax(logits, dim=1)
    predicted_label_index = torch.argmax(probabilities, dim=1).item()
    predicted_label_text = labels[predicted_label_index]

    print(f"BOX: {predicted_label_text}")
    pyttsx3.speak(f"BOX: {predicted_label_text}")

# question_text = "教官室在哪?"
while True:
    question_text = input("問題: ")
    if question_text == "exit":
        break
    ask_question(question_text)
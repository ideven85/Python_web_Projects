from transformers import pipeline

classification =  pipeline("sentiment-analysis").device

print(classification("I am sleepy"))
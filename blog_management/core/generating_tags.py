# Probably can first learn Django properly, then start using ML algorithms..
# Can't same the same for Spring Boot at least...Know it much better...
# With Django.. Learn it and flask first and revise CSS/React/Javascript/Typescript... and build a few projects

# todo
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)

inputs = tokenizer("I loved your post", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
print(model.config.id2label[predicted_class_id])

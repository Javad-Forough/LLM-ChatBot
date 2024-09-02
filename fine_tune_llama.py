# fine_tune_llama.py
from transformers import LlamaTokenizer, LlamaForCausalLM
from torch.optim import AdamW

# Load tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained("meta-llama/LLaMA-13B")
model = LlamaForCausalLM.from_pretrained("meta-llama/LLaMA-13B")

# Example data
train_texts = ["How can I reset my password?", "What is your refund policy?", "Where can I track my order?"]
train_labels = ["Please visit the account settings to reset your password.", 
                "Our refund policy allows returns within 30 days of purchase.", 
                "You can track your order through the 'My Orders' section in the app."]

# Tokenize data
train_encodings = tokenizer(train_texts, truncation=True, padding=True, return_tensors="pt")
labels_encodings = tokenizer(train_labels, truncation=True, padding=True, return_tensors="pt")

# Fine-tune model
model.train()
optimizer = AdamW(model.parameters(), lr=1e-5)

for epoch in range(3):  # Number of epochs can be adjusted
    optimizer.zero_grad()
    outputs = model(**train_encodings, labels=labels_encodings['input_ids'])
    loss = outputs.loss
    loss.backward()
    optimizer.step()

    print(f'Epoch {epoch+1} Loss: {loss.item()}')

# Save the fine-tuned model
model.save_pretrained("./fine_tuned_llama")
tokenizer.save_pretrained("./fine_tuned_llama")

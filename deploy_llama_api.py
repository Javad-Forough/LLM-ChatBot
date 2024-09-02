# deploy_llama_api.py
from flask import Flask, request, jsonify
from transformers import LlamaTokenizer, LlamaForCausalLM

# Load fine-tuned model and tokenizer
tokenizer = LlamaTokenizer.from_pretrained("./fine_tuned_llama")
model = LlamaForCausalLM.from_pretrained("./fine_tuned_llama")

# Set up Flask application
app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['text']
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

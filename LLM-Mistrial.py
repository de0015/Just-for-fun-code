from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return render_template('result.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)

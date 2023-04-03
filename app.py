from flask import Flask, render_template, request
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('reetghosh1/FakeNews')
model = AutoModelForSequenceClassification.from_pretrained('reetghosh1/FakeNews')

# Create a Flask application
app = Flask(__name__)


# Define the home page
@app.route('/')
def home():
    return render_template('index.html')


# Define the prediction page
@app.route('/predict', methods=['POST'])
def predict():
    # Get the news article from the form input
    article = request.form['article']

    # Tokenize the article text
    input_ids = tokenizer.encode(article, return_tensors='pt')

    # Get the model's prediction
    output = model(input_ids)[0].softmax(dim=1).detach().numpy()[0]
    label = int(output.argmax())
    prediction = "fake" if label == 0 else "real"

    # Render the prediction result page
    return render_template('result.html', prediction=prediction, article=article)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

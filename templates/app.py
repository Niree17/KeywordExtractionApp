from flask import Flask, render_template, request
from rake_nltk import Rake

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    keywords = None
    if request.method == 'POST':
        text = request.form['text']  # Get the text from the form
        r = Rake()  # Initialize Rake
        r.extract_keywords_from_text(text)  # Extract keywords
        keywords = r.get_ranked_phrases_with_scores()  # Get ranked phrases with scores
    return render_template('index.html', keywords=keywords)

if __name__ == '__main__':
    app.run(debug=True)

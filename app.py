"""
The web interface of MemeGenerator Application using Flask.

run the flask and use a browser to use the application.
"""

# Imports
import random
import os
import requests
from flask import Flask, render_template, request  # , abort

# Relative Imports
from QuoteEngine import Ingestor
from Image import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources.

    Generate the list of QuoteModel objects using the different available files.
    Generate the list of paths to the images.

    :returns: quotes_list, img_paths
    """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quote_objs = []
    for f in quote_files:
        tmp = Ingestor.parse(f)
        quote_objs = quote_objs + tmp

    images_path = "./_data/photos/dog/"

    images = []
    for filename in os.listdir(images_path):
        img = os.path.join(images_path, filename)
        images.append(img)

    return quote_objs, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, 'tmp.jpg', quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form["image_url"]
    body = request.form["body"]
    author = request.form["author"]
    extension = image_url.split(".")[-1]
    file_name = 'tmp'
    file_path = f"./static/{file_name}.{extension}"
    response = requests.get(image_url)
    with open(file_path, "wb") as file:
        file.write(response.content)
    path = meme.make_meme(file_path, 'tmp.jpg', body, author)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

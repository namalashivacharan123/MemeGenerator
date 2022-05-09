"""
This module implements CLI of MemeGenerator Application.

Run python3 meme.py -h to know more about commands.
"""

import os
import random
import argparse

# Relative Imports
from QuoteEngine import Ingestor, QuoteModel
from Image import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, body=quote.body, author=quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a meme")
    parser.add_argument('--path', nargs=1, type=str, help="Path to the image", default=None)
    parser.add_argument('--body', nargs=1, type=str, help="quote body", default=None)
    parser.add_argument('--author', nargs=1, type=str, help="quote author", default=None)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))

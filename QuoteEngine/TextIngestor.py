"""Ingest Data from a text file."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Ingest data from a text file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        """Parse content of text file and return list of quote objects."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes_list = []
        with open(path, 'r') as f:
            for line in f.read().split('\n'):
                if len(line) > 0:
                    body, author = line.split('-')
                    body = body.strip().strip("\"").strip()
                    author = author.strip()
                    temp_quote_obj = QuoteModel(body, author)
                    quotes_list.append(temp_quote_obj)
        return quotes_list

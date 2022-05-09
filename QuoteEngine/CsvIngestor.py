"""Ingests the data from CSV file using pandas."""

import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CsvIngestor(IngestorInterface):
    """
    Load quotes from CSV file.

    Inherits IngestorInterface. Implements abstract class parse.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        """
        Parse the CSV file.

        :param path: The path to the CSV file.
        :type path: str
        :return: List of quotes. Each quote is a QuoteModel instance.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        df = pd.read_csv(path)
        quotes_list = [QuoteModel(body=x, author=y) for x, y in zip(df['body'], df['author'])]

        return quotes_list


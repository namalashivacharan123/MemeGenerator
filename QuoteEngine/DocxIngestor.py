"""Ingests data from DOCX file using docx library."""

import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    Load quotes from .docx files.

    Inherits IngestorInterface. Implements the abstract method parse.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """
        Parse .docx file.

        :param path: The relative path to the .docx file
        :type path: str

        :returns: The list of quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes_list = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split('-')
                body = body.strip().strip("\"").strip()
                author = author.strip()
                quote_obj = QuoteModel(body, author)
                quotes_list.append(quote_obj)

        return quotes_list

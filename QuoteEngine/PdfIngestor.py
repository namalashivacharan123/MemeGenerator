"""Ingest from a PDF file."""

import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PdfIngestor(IngestorInterface):
    """Ingest Data from a pdf file."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """Parse the provided pdf file and provide list of quote objects."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/pdf_to_text.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        with open(tmp, "r") as file_ref:
            quotes_list = []
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    body, author = line.split('-')
                    body = body.strip().strip("\"").strip()
                    author = author.strip()
                    tmp_quote = QuoteModel(body, author)
                    quotes_list.append(tmp_quote)

        os.remove(tmp)
        return quotes_list

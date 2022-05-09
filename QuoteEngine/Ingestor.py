"""Ingest data from any kind of file."""

from .IngestorInterface import IngestorInterface

from .TextIngestor import TextIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor
from .DocxIngestor import DocxIngestor


class Ingestor(IngestorInterface):
    """Ingest data from any file type."""

    different_ingestors_list = [
        TextIngestor,
        CsvIngestor,
        PdfIngestor,
        DocxIngestor
    ]

    @classmethod
    def parse(cls, path):
        """
        Parse content of the file.

        :param path: Path to the file.
        :type path: str
        :return: A list of quote objects.
        """
        for ingestor in cls.different_ingestors_list:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

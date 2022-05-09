"""The Interface to ingest quotes from different types of files."""

from abc import abstractmethod, ABC


class IngestorInterface(ABC):
    """IngestorInterface is an interface to ingest quotes."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """
        Say whether the file can be ingested or not.

        :param path: The path to the file.
        :type path: str
        :return: bool (True means can be ingested. False means cannot be ingested.)
        """
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """
        Parse the contents of the file.

        An Abstract Method.
        :param path: The path to the file.
        :type path: str
        :return: The list of quote objects.
        """
        pass

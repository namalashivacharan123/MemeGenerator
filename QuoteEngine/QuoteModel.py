"""Model to the quote object."""


class QuoteModel:
    """QuoteModel is model to the Quote."""

    def __init__(self, body, author):
        """Instantiate QuoteModel with body and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return the string representation of the QuoteModel."""
        return f"\"{self.body}\" - {self.author}"

    def __repr__(self):
        """Return the representation of the QuoteModel."""
        return f"\"{self.body}\" - {self.author}"

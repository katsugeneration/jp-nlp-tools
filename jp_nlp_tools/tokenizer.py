from typing import List
import MeCab


class MeCabTokenizer(object):
    """Japanese morpheme tokenizer used by mecab."""

    def __init__(self):
        self._tagger = MeCab.Tagger("-Owakati")
        self._tagger.parse('')  # Avoiding mecab parser error

    def tokenize(self, text: str) -> List[str]:
        """Tokenize mecab wakati option.

        Args:
            text (str): target text.

        Return:
            tokenized (List[str]): tokenized stringss.
        """
        return self._tagger.parse(text).split()

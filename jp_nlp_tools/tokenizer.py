from typing import List
from abc import ABCMeta, abstractmethod
import MeCab


class ITokenizer(metaclass=ABCMeta):
    """Tokenize text interface."""

    @abstractmethod
    def tokenize(
            self,
            text: str) -> List[str]:
        """Tokenize target text to str list.

        Args:
            text (str): target text.

        Return:
            tokenized (List[str]): tokenized stringss.
        """
        pass


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

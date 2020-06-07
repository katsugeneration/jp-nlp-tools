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


class NgramTokenizer(ITokenizer):
    """Ngram tokenization.
    
    Args:
        base_tokenizer (Tokinzer): base tokenizer useed for tokenize text before ngram concatenate.
        n (int): ngram's n value.

    """

    def __init__(
            self,
            base_tokenizer: ITokenizer,
            n :int = 2):
        self._base_tokenizer = base_tokenizer
        self._n = n

    def tokenize(self, text: str) -> List[str]:
        """Tokenize base tokenizer and concatenate ngram.

        Args:
            text (str): target text.

        Return:
            tokenized (List[str]): tokenized and ngram concatenated stringss.
        """
        tokens = self._base_tokenizer.tokenize(text)
        length = len(tokens)
        return ["".join(tokens[i:i+self._n]) for i in range(length-self._n+1)]

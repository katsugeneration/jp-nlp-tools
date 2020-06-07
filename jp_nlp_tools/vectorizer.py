from typing import Type, Tuple
from sklearn.feature_extraction.text import _VectorizerMixin
from jp_nlp_tools.tokenizer import ITokenizer


class VectorizerFactory:
    """Scikit-learn format vectorizer factory ."""

    stop_words = ['。', 'は', '、', 'の', '（', '）', 'に', 'で', 'を', 'た', 'し', 'が', 'と', 'て', 'ある', 'れ', 'さ', 'する', 'いる', 'から', 'も', '・', 'として', '「', '」', 'い', 'こと', '–', 'な', 'なっ', 'や', 'れる', 'など', 'ため', 'この', 'まで', 'また', 'あっ', 'ない', 'あり', 'なる', 'その', 'られ', '後', '『', '』', 'へ']

    @classmethod
    def generate(
            cls,
            class_: Type[_VectorizerMixin],
            tokenizer: ITokenizer,
            ngram_range: Tuple[int, int] = (1, 1)) -> _VectorizerMixin:
        """Generate vectorizer with tokenizer.

        Args:
            class_ (Type[_VectorizerMixin]): scikit-learn vectorizer class.
            tokenizer (ITokenizer): tokenizer instance.
            ngram_range (Tuple): ngram range definition.

        Return:
            vectorizer (_VectorizerMixin): initilized vectorizer instance.
        """
        _vectorizer = class_(
            input='content',
            encoding='utf-8',
            decode_error='ignore',
            tokenizer=tokenizer.tokenize,
            stop_words=cls.stop_words,
            ngram_range=ngram_range)
        return _vectorizer

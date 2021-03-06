from nose.tools import ok_, eq_
import numpy as np
from sklearn.feature_extraction.text  import CountVectorizer
from jp_nlp_tools.tokenizer import MeCabTokenizer
from jp_nlp_tools.vectorizer import VectorizerFactory


class TestVectorizerFactory:
    def test_generate(self):
        tokenizer = MeCabTokenizer()
        vectorizer = VectorizerFactory.generate(CountVectorizer, tokenizer)
        ok_(vectorizer)

    def test_vectorize(self):
        tokenizer = MeCabTokenizer()
        vectorizer = VectorizerFactory.generate(CountVectorizer, tokenizer)
        ret = vectorizer.fit_transform(['今日は晴れます'])
        np.testing.assert_array_equal(np.array([[1, 1, 1]]), ret.toarray())
        ok_('今日' in vectorizer.vocabulary_)
        ok_('晴れ' in vectorizer.vocabulary_)
        ok_('ます' in vectorizer.vocabulary_)

    def test_ngram_range(self):
        tokenizer = MeCabTokenizer()
        vectorizer = VectorizerFactory.generate(CountVectorizer, tokenizer, ngram_range=(1, 2))
        ret = vectorizer.fit_transform(['今日は晴れます'])
        np.testing.assert_array_equal(np.array([[1, 1, 1, 1, 1]]), ret.toarray())
        ok_('今日' in vectorizer.vocabulary_)
        ok_('晴れ' in vectorizer.vocabulary_)
        ok_('ます' in vectorizer.vocabulary_)
        ok_('今日 晴れ' in vectorizer.vocabulary_)
        ok_('晴れ ます' in vectorizer.vocabulary_)

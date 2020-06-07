from nose.tools import ok_, eq_
from jp_nlp_tools.tokenizer import MeCabTokenizer, NgramTokenizer


class TestMeCabTokenizer:
    def test_init(self):
        tokenizer = MeCabTokenizer()
        ok_(tokenizer)

    def test_tokenize(self):
        tokenizer = MeCabTokenizer()
        ret = tokenizer.tokenize('今日は晴れます')
        eq_(['今日', 'は', '晴れ', 'ます'], ret)


class TestNgramTokenizer:
    def test_init(self):
        _tokenizer = MeCabTokenizer()
        tokenizer = NgramTokenizer(_tokenizer)
        ok_(tokenizer)

    def test_tokenize(self):
        _tokenizer = MeCabTokenizer()
        tokenizer = NgramTokenizer(_tokenizer)
        ret = tokenizer.tokenize('今日は晴れます')
        eq_(['今日は', 'は晴れ', '晴れます'], ret)

        tokenizer = NgramTokenizer(_tokenizer, 3)
        ret = tokenizer.tokenize('今日は晴れます')
        eq_(['今日は晴れ', 'は晴れます'], ret)

from nose.tools import ok_, eq_
from jp_nlp_tools.tokenizer import MeCabTokenizer


class TestMeCabTokenizer:
    def test_init(self):
        tokenizer = MeCabTokenizer()
        ok_(tokenizer)

    def test_tokenize(self):
        tokenizer = MeCabTokenizer()
        ret = tokenizer.tokenize('今日は晴れます')
        eq_(['今日', 'は', '晴れ', 'ます'], ret)

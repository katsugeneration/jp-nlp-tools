Japanese NLP Tools

# Required
- mecab
- mecab dictionary（ex: mecab-ipadic-neologd）
- python >= 3.7

# Usage

Insatll
```
pip install -U git+ssh://github.com/katsugeneration/jp-nlp-tools.git
```

Execute tokenizer
```
python -c "import jp_nlp_tools.tokenizer; tokenizer = jp_nlp_tools.tokenizer.MeCabTokenizer(); print(tokenizer.tokenize('今日の天気は晴れです。'))"
```
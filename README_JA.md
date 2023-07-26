# OpenAI Quickstart

<p align="center">
    <br> <a href="README.md">English</a> | <a href="README-CN.md">中文</a> | 日本語
</p>


このプロジェクトは、大規模言語モデルとその人工知能ガバナンスと制御（AIGC）シナリオへの応用に関心のあるすべての人のためのワンストップ学習リソースとして設計されています。理論的基礎、開発基礎、実践例を提供することで、このプロジェクトはこれらの最先端のトピックに関する包括的なガイダンスを提供します。

## 特徴

- **大規模言語モデルの理論と開発の基礎**: GPT-4 のような大規模言語モデルのアーキテクチャ、学習方法、アプリケーションなど、その内部構造を深く掘り下げる。

- **LangChain による AIGC アプリケーション開発**: AIGC アプリケーションを開発するために LangChain を使用するハンズオン例とチュートリアルで、大規模言語モデルの実用的なアプリケーションを実証します。

## はじめに

このリポジトリをローカルマシンにクローンすることから始めることができます:

```shell
git clone https://github.com/DjangoPeng/openai-quickstart.git
```

その後、ディレクトリに移動し、各モジュールの指示に従って開始してください。

## スケジュール

| 日付       | 説明                                                                                                                                                                                                        | コース教材                                                                          | イベント                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 7月12日(月) **第1週** | 大型モデルの基礎: 理論と技術の進化 <br/> - ラージモデルの初期的探求: 起源と発展 <br/> - ウォームアップ: 注意のメカニズムを読み解く <br/> - 変革のマイルストーン: Transformer の台頭 <br/> - 異なる道を歩む: GPTと Bert の選択 | お勧めの資料:<br/>- [Attention Mechanism: Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)<br/>- [An Attentive Survey of Attention Models](https://arxiv.org/abs/1904.02874)<br/>- [Transformer: Attention is All you Need](https://arxiv.org/abs/1706.03762)<br/>- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | [[Homework](docs/homework_01.md)] |
| 7月16日(木) | GPT モデルファミリー: スタートから現在まで <br/> - GPT-1 から GPT-3.5 まで: 進化 <br/> - ChatGPT: 勝利の行方 <br/> - GPT-4: 新たな始まり <br/>プロンプト学習 <br/> - Chain-of-Thought (CoT): 先駆的な仕事 <br/> - Self-Consistency: マルチパス推論 <br/> - Tree-of-Thoughts (ToT): ストーリーの続き | お勧めの資料:<br/>- [GPT-1: Improving Language Understanding by Generative Pre-training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)<br/>- [GPT-2: Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)<br/>- [GPT-3: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)<br/><br/><br/>追加資料:<br/>- [GPT-4: Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE](https://www.semianalysis.com/p/gpt-4-architecture-infrastructure)<br/>- [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/abs/2303.10130)<br/>- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712)<br/><br/> | [[Homework](docs/homework_02.md)] |
| 7月19日(火) **第2週** | 大規模モデル開発の基礎: OpenAI の組み込み <br/> - 一般的な人工知能の前夜 <br/> - 「3つの世界」と「チューリング・テスト」 <br/> - コンピュータのデータ表現 <br/> - 表現学習と埋め込み <br/> Embeddings Dev 101 <br/> - コースプロジェクト: GitHub openai-quickstart <br/> - OpenAI の埋め込みを始める                      | お勧めの資料:<br/>- [Representation Learning: A Review and New Perspectives](https://arxiv.org/abs/1206.5538)<br/>- [Word2Vec: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)<br/>- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf)<br/><br/>追加資料:<br/><br/>- [Improving Distributional Similarity with Lessons Learned from Word Embeddings](http://www.aclweb.org/anthology/Q15-1016)<br/>- [Evaluation methods for unsupervised word embeddings](http://www.aclweb.org/anthology/D15-1036) | [[Homework](docs/homework_03.md)]<br/>コード:<br/>[[embedding](openai_api/embedding.ipynb)] |
| 7月23日(土) | OpenAI ラージモデル開発と応用実践 <br/> - OpenAI ラージモデル開発ガイド <br/> - OpenAI 言語モデルの概要 <br/> - OpenAI GPT-4、GPT-3.5、GPT-3、モデレーション <br/> - OpenAI トークンの請求と計算 <br/>OpenAI API の紹介と実践 <br/> - OpenAI モデル API <br/> - OpenAI コンプリーション API  <br/> - OpenAI チャットコンプリケーション API <br/> - コンプリーション vs チャットコンプリーション <br/>OpenAI ラージモデル活用実践 <br/> - テキスト補完の初期段階 <br/> - チャットボットの初期段階 | お勧めの資料:<br/><br/>- [OpenAI Models](https://platform.openai.com/docs/models)<br/>- [OpenAI Completions API](https://platform.openai.com/docs/guides/gpt/completions-api)<br/>- [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api) | コード:<br/>[[models](openai_api/models.ipynb)] <br/>[[tiktoken](openai_api/count_tokens_with_tiktoken.ipynb)] |


## コントリビュート

コントリビュートこそが、オープンソースコミュニティを、学び、刺激し、創造するための素晴らしい場所にしているのです。どのような貢献でも大いに歓迎します。提案や機能要望がある場合は、まず issue を開いて変更したい点を議論してください。

## ライセンス

このプロジェクトのライセンスは Apache-2.0 License です。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 連絡先

Django Peng - pjt73651@email.com

プロジェクトリンク: https://github.com/DjangoPeng/openai-quickstart

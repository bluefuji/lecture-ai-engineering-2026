# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]： fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：
aws_aws___search_documentation({'search_phrase': 'Amazon S3 バージョニング 概要', 'topics': ['general']})
aws_aws___search_documentation({'topics': ['general'], 'search_phrase': '"Versioning" "Amazon S3" what is'})
- 気づき・疑問：mcpサーバーを増やすことで、既存のツールをすぐに使えるというのは利点である。ただしそのツールの挙動がサーバー側のプログラムになってしまうので読めない点はネックである。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 
- やったこと：app/mcp_server.pyにおいて、glossary_get_lecture_summaryの機能を追加した。
- 結果：以下の出力結果を得た。
第2回では、**「ファインチューニングとLoRA」**をテーマに学びます。

主な学習内容は以下の通りです。

- **事前学習とファインチューニングの違い**：ファインチューニングが向く場面・向かない場面を理解します。
- **SFT（教師あり微調整）**：入力と望ましい出力のペアで学習させる仕組みと、データの質の重要性を学びます。
- **PEFTとLoRA**：全パラメータを更新するのではなく、小さな低ランク行列だけを学習させることでメモリやコストを大幅に削減するLoRAの考え方を学びます。
- **QLoRAとの関係**：重みを4bit量子化してベースモデルのメモリを抑える仕組みについて触れます。
- **演習**：Google Colab上で小さなモデルを架空のFAQデータでLoRA学習させ、学習の前後で出力の変化（JSON形式の遵守率や内容正解率）を比較します。

関係する回：第2回

--- trace ---
[tool call]   glossary_get_lecture_summary({'lecture': 2})
[tool return] glossary_get_lecture_summary -> # 第2回 ファインチューニングとLoRA

## この回のねらい

- 事前学習とファインチューニングの違い、ファインチューニングが向く場面と向かない場面を理解する
- LoRAの考え方を理解し、Google Colab上で小さなモデルを…
[usage] 入力 5,942 tokens / 出力 237 tokens / モデル応答 2 回

- 気づき・疑問：使えるツールの数が7から8に増えていて、指定された回の講義の要点を返すようになった。

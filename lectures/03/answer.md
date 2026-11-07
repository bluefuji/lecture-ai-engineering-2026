# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
　明らかに自身の知識から回答するのではなく、知らないはずの用語集の知識を有した返答を行う。

- `--trace` で見えたツール呼び出し（ツール名と引数）：
[tool call]   make_quiz({'lecture': 2})

- 1つの質問での LLM 呼び出し回数（`requests`）：
[usage] RunUsage(cost=Decimal('0.0005580'), details={'text_prompt_tokens': 910}, input_text_tokens=910, input_tokens=910, output_tokens=114, requests=2, tool_calls=1)
つまり、requests=2から、二回

- 追加したツールと、docstring に書いた説明：
def make_quiz(lecture: int) -> str:
    """指定した回の用語から1つを選び、
    確認問題と答えを返す。
 
    「第2回の確認問題を出して」のように、
    復習用の問題を求められたときに使う。
    """
    terms = [entry for entry in load_glossary() if entry["lecture"] == lecture]
    if not terms:
        return f"第{lecture}回の用語は用語集にありません。"

    entry = random.choice(terms)
    return json.dumps(
        {
            "question": f"「{entry['definition']}」に当てはまる用語は何でしょう？",
            "answer": entry["term"],
        },
        ensure_ascii=False,
    )

## 宿題

- 取り組んだレベル：基礎 / 実装 
- やったこと：
基礎：instructionsにて、「宿題の答えそのものは書かず、考え方のヒントで導く。」->「考え方のヒントで導かずに、一気に問いや宿題の答えそのものを書く。」に変更し、"uv run python -m app.agent --trace "LoRAとQLoRAの違いは？"を実行した。

実装:AIを利用して、学習の記録を learning_log/ フォルダに保存するツール save_learning_log を作り、保存の前に利用者の確認を挟んだ。その後'uv run python -m app.agent --trace '学習記録として「今日は save_learning_log の承認フローを実装した」と保存して''を実行した。

- 結果：
# 基礎：
# before:"""
講座の用語集によると、LoRAとQLoRAの違いは主に次の点にあります。
- **LoRA**
  事前学習済みの重みを固定したまま、重みの更新分を小さな低ランク行列（2つの行列の積）で表し、その部分だけを学習するPEFT（Parameter-Efficient Fine-Tuning）手法です。学習するパラメータを大幅に削減できます。
- **QLoRA**
  ベースモデルの重みを4ビットなどに**量子化**してメモリを大幅に節約した上で、LoRAによるファインチューニングを行う手法です。これにより、より大きなモデルを小さなGPUメモリでも扱えるようになります。
このように、LoRAは低ランク行列で学習パラメータを減らす手法であり、QLoRAはそのベースモデルを量子化（4ビット化など）してメモリ効率をさらに高めた発展形となります。
関係する回：第2回
--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
"""
# after:"""
LoRAとQLoRAの違いは以下の通りです。
* **LoRA**
  事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法です。学習するパラメータが少なく、学習結果（アダプタ）も小さいファイルで保存できます。
* **QLoRA**
  ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法です。より大きなモデルを小さなGPUで扱えるようにします。
（関連する回：第2回）
--- trace ---
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
"""

# 実装:
"""
保存内容の確認: save_learning_log({'content': '- 今日は save_learning_log の承認フローを実装した'})
この内容を保存しますか？ [y/N]: y
学習記録を `learning_log/2026-11-07.md` に保存しました。
（関連する回はありません）

--- trace ---
[tool call]   save_learning_log({'content': '- 今日は save_learning_log の承認フローを実装した'})
"""
learning_log内容を引用"""
## 2026-11-07T17:43:27+09:00
- 今日は save_learning_log の承認フローを実装した
"""


- 気づき・疑問：
基礎では、instructionsを変えたが、考えを導くようなまとめの部分が消失したように思われる。あるいはどちらかと言えば、before段階が考え方を導き答えを教えないという処理をしていないと考えられ、「考え方を導いて、～をしない」という処理がむしろ高度な処理であると考えられる。
実装では、LLMを介してセッションログを残すことが可能になったと考えられる。例えば、第一回で実装した履歴の残るようにするAIを、こちらでも実装すれば、その内容を残すことができるようになると考えられる。


from types import SimpleNamespace

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=34,
        ),
        text="回答",
    )
    chat = SimpleNamespace(send_message=lambda question: response)

    assert ask.ask("質問", chat) == "回答"
    assert "[トークン数] 入力: 12 / 出力: 34" in capsys.readouterr().out


def test_run_conversation_reuses_chat_until_empty_input(monkeypatch, capsys):
    questions = []

    class FakeChat:
        def send_message(self, question):
            questions.append(question)
            return SimpleNamespace(
                usage_metadata=SimpleNamespace(
                    prompt_token_count=1,
                    candidates_token_count=1,
                ),
                text=f"{question}への回答",
            )

    follow_up_questions = iter(["追加質問", ""])
    monkeypatch.setattr("builtins.input", lambda prompt: next(follow_up_questions))

    ask.run_conversation(FakeChat(), "最初の質問")

    assert questions == ["最初の質問", "追加質問"]
    output = capsys.readouterr().out
    assert "最初の質問への回答" in output
    assert "追加質問への回答" in output

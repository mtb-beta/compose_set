# compose_set

自分が作曲・編曲するときに考えることをそのまま音に変換するライブラリを目指してるリポジトリです。

# テキストをmidiに変換する

```
(venv) $ python -m compose.midi.text_to_mid ./sample/text_to_mid/donguri.txt ./sample/text_to_mid/donguri.midi
```

# コード進行の書いたcsvをmidiに変換する

```
(venv) $ python -m compose.midi.chord_to_mid ./sample/chord_to_mid/canon.txt ./sample/chord_to_mid/canon.midi
```

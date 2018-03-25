import pretty_midi

sample_data = [
    {
        'note_name': 'C5',
        'velocity': 100,
        'start': 0,
        'end': 0.5
    },
    {
        'note_name': 'E5',
        'velocity': 100,
        'start': 0,
        'end': 0.5
    },
    {
        'note_name': 'G5',
        'velocity': 100,
        'start': 0,
        'end': 0.5
    },
]


def _output_midi(path, instrument):
    """
    pretty_midのinstrumentをmidiファイルに書き出すユーティリティ関数
    """
    cello_c_chord = pretty_midi.PrettyMIDI()
    cello_c_chord.instruments.append(instrument)
    cello_c_chord.write(path)

def _note_mapper(note_dict):
    """
    noteのjsonからprety_midiのNoteのオブジェクトに変換するマッピング関数
    """
    # NoteNameからmidiのnote numberを探す
    note_number = pretty_midi.note_name_to_number(note_dict['note_name'])

    # midiのノートを作る
    note = pretty_midi.Note(
        velocity=note_dict['velocity'],
        pitch=note_number,
        start=note_dict['start'],
        end=note_dict['end']
    )

    return note


def data_to_midi(data, midi_path):
    """
    辞書形式でmidiのnoteデータを渡すとmidiファイルに変換するユーティリティ関数
    """
    # Celloと言う楽器のプログラムナンバーを取得（なんでも良いがとりあえず）
    cello_program = pretty_midi.instrument_name_to_program('Cello')

    # プログラムナンバーを元に楽器を生成
    instrument_track = pretty_midi.Instrument(program=cello_program)

    # データをinstrumentトラックに出力
    for note_data in data:
        note = _note_mapper(note_data)
        instrument_track.notes.append(note)

    # ファイル書き出し
    output_mid(path, instrument_track)

import pandas as pd
import pretty_midi

def load_csv(path):
    """
    csv形式のmidiテキストデータを読み込むユーティリティ関数
    """
    dtype = {
        "NoteName": 'str',
        "Start": 'float',
        "End": 'float',
        "Velocity": 'int',
    }
    data = pd.read_csv(path, dtype=dtype)

    return data


def text_to_midi(text_path, midi_path):
    data = load_csv(text_path)

    instrument_track = get_instrument()

    # データをinstrumentトラックに出力
    for index, row in data.iterrows():
        note = _note_mapper(row)
        instrument_track.notes.append(note)

    # ファイル書き出し
    output_midi(midi_path, instrument_track)

def output_midi(path, instrument):
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
    note_number = pretty_midi.note_name_to_number(note_dict['NoteName'])

    # midiのノートを作る
    note = pretty_midi.Note(
        velocity=note_dict['Velocity'],
        pitch=note_number,
        start=note_dict['Start'],
        end=note_dict['End']
    )

    return note

def get_instrument(instrument_name="Cello"):
    """
    トラックを生成
    """
    # Celloと言う楽器のプログラムナンバーを取得（なんでも良いがとりあえず）
    cello_program = pretty_midi.instrument_name_to_program(instrument_name)

    # プログラムナンバーを元に楽器を生成
    instrument_track = pretty_midi.Instrument(program=cello_program)
    return instrument_track

def data_to_midi(data, midi_path):
    """
    辞書形式でmidiのnoteデータを渡すとmidiファイルに変換するユーティリティ関数
    """
    instrument_track = get_instrument()

    # データをinstrumentトラックに出力
    for note_data in data:
        note = _note_mapper(note_data)
        instrument_track.notes.append(note)

    # ファイル書き出し
    output_mid(path, instrument_track)


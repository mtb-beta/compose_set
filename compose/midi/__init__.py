import compose.core
import pandas as pd
import pretty_midi

def normalize_duration(data):
    """
    StartとEndをノーマライズする。
    1を４分音符にしている。
    """
    norm_tmp = data.copy()
    data.Start = norm_tmp.Start / 2
    data.End = norm_tmp.End / 2
    return data


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

def chord_notes(chordname):
    scale = compose.core.Scale(key='C')
    note_number = scale.diatonic_number(chordname[:1])
    return scale.diatonic(note_number)

def chord_to_midi(chord_path, midi_path):
    """
    chord 進行のファイルをmidiファイルに変換する
    """

    # コード進行のファイルを読み込む
    dtype = {
        "ChordName": 'str',
        "Start": 'float',
        "End": 'float',
        "Velocity": 'int',
    }
    data = pd.read_csv(chord_path, dtype=dtype)

    # midiファイルに書き出すために変換する
    text_midi = []
    for index, row in data.iterrows():
        for note in chord_notes(chordname=row.ChordName):
            row_tmp = []
            row_tmp.append(note+'5')
            row_tmp.append(row.Velocity)
            row_tmp.append(row.Start)
            row_tmp.append(row.End)
            text_midi.append(row_tmp)
    text_midi = pd.DataFrame(text_midi, columns=['NoteName', 'Velocity', 'Start', 'End', ])

    # midiファイルに書き出す
    output_text_to_midi(text_midi, midi_path)

def output_text_to_midi(text_midi_list, midi_path):
    """
    text midiファイル形式のリストをファイルに書き出す。
    """
    data = normalize_duration(text_midi_list)

    instrument_track = get_instrument()

    # データをinstrumentトラックに出力
    for index, row in data.iterrows():
        note = _note_mapper(row)
        instrument_track.notes.append(note)

    # ファイル書き出し
    output_midi(midi_path, instrument_track)

def text_to_midi(text_path, midi_path):
    """
    text ファイルをmidiファイルに変換する
    """
    # 読込
    data = load_csv(text_path)

    # 出力
    output_text_to_midi(data, midi_path)

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


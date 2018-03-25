from . import text_to_midi
import argparse

if __name__ == "__main__":
    """
    text_to_midiのコマンドライン
    $ python -m compose.midi.text_to_mid ./sample/sample.txt ./sample/sample.midi
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("text_path", help="path to input text file.")
    parser.add_argument("midi_path", help="path to output midi file.")
    args = parser.parse_args()
    text_to_midi(args.text_path, args.midi_path)

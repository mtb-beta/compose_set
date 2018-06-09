from . import chord_to_midi
import argparse

if __name__ == "__main__":
    """
    chord_to_midiのコマンドライン
    $ python -m compose.midi.chord_to_mid ./sample/sample.txt ./sample/sample.midi
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("chord_path", help="path to input chord file.")
    parser.add_argument("midi_path", help="path to output midi file.")
    args = parser.parse_args()
    chord_to_midi(args.chord_path, args.midi_path)

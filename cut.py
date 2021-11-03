import sys

from pydub import AudioSegment


def cut_audio(t1: int, t2: int, in_file: str, out_file: str) -> bool:
    new_audio = AudioSegment.from_wav(in_file)
    new_audio = new_audio[t1:t2]
    new_audio.export(out_file, format="wav")
    return True


if __name__ == '__main__':
    t1 = int(sys.argv[1]) * 1000
    t2 = int(sys.argv[2]) * 1000
    in_file = sys.argv[3]
    out_file = sys.argv[4]
    cut_audio(t1, t2, in_file, out_file)


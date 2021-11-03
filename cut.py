import sys

from pydub import AudioSegment


def cut_audio(t1: int, t2: int, in_file: str, out_file: str) -> bool:
    new_audio = AudioSegment.from_wav(in_file)
    new_audio = new_audio[t1:t2]
    new_audio.export(out_file, format="wav")
    return True


def slice_audio(size, in_file, out_file):
    pass


if __name__ == '__main__':
    t1 = int(sys.argv[1]) * 1000
    t2 = int(sys.argv[2]) * 1000
    in_file = sys.argv[3]
    out_file = sys.argv[4]
    try:
        all_ = sys.argv[5]
        size = sys.argv[6]
        slice_audio(t1, t2, in_file, out_file)
    except IndexError:
        cut_audio(t1, t2, in_file, out_file)


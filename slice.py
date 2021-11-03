import sys
from math import ceil

from pydub import AudioSegment


def slice_audio(t: int, in_file: str, out_file: str) -> bool:
    new_audio = AudioSegment.from_wav(in_file)
    no_slices = ceil(len(new_audio) / t)
    t0 = 0
    t1 = t
    for i in range(no_slices):
        new_audio = new_audio[t0:t1]
        new_file = f"{out_file.rpartition('.wav')[0]}_{i+1}.wav"
        new_audio.export(new_file, format="wav")
        t0 = t1
        t1 += t
    return True


if __name__ == '__main__':
    t = int(sys.argv[1]) * 1000
    in_file = sys.argv[2]
    out_file = sys.argv[3]
    slice_audio(t, in_file, out_file)

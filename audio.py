import math
from time import sleep, time

from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio

try:
    from itertools import izip
except ImportError:  # Python 3
    izip = zip
    xrange = range

p = PyAudio()


def sine_tone(frequency, duration, volume=0.01, sample_rate=48000):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    stream = p.open(format=p.get_format_from_width(2),  # 16 bit
                    channels=1,  # mono
                    rate=sample_rate,
                    output=True)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    before = time()
    samples = [int(s(t) * 0x7fff + 0x8000).to_bytes(4, 'little') for t in range(n_samples)]
    while time()-before <= 0.1:
        sleep(0.001)
    stream.write(b''.join(samples))

    # fill remainder of frameset with silence
    stream.write(b'\x00\x80' * restframes)

    stream.stop_stream()
    stream.close()


# sine_tone(400, 1)
# sleep(3)
# sine_tone(500, 1)

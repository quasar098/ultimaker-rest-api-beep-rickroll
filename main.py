import requests
from time import sleep
from audio import sine_tone
from data import data, REST
from _thread import start_new_thread


amt = 0.17


def make_request(freq_hz: int, time_s: float):
    sine_tone(freq_hz, time_s)  # todo add ultimaker thing


def make_sound(freq: int, time_ms: int):
    start_new_thread(make_request, (freq, time_ms/1000))
    print(f'sleeping {time_ms/1000}')


def main():
    whole_note = 2105.26315789  # in ms

    for thisNote in range(0, len(data), 2):
        divider = data[thisNote + 1]
        if divider > 0:
            noteDuration = whole_note / divider
        else:
            noteDuration = whole_note / abs(divider)
            noteDuration *= 1.5

        make_sound(data[thisNote], noteDuration * 0.9)

        sleep(noteDuration/1000)

        sleep(0.02)


if __name__ == '__main__':
    main()

import requests
from time import sleep, time
# from audio import sine_tone
from data import data, REST
from os import system
from _thread import start_new_thread
from json import load


with open("config.json", 'r') as f:
    config = load(f)


amt = 0.17


def make_request(freq_hz: int, time_s: float):
    # sine_tone(freq_hz, time_s)  # todo add ultimaker thing
    assert isinstance(freq_hz, int)
    assert isinstance(time_s, (float, int))
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Digest username="{config["username"]}", realm="Jedi-API", nonce="{config["nonce"]}", uri="/api/v1/printer/beep", response="{config["response"]}", qop=auth, nc={config["nc"]}, cnonce="{config["cnonce"]}"',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': f'{config["address"]}',
    'Pragma': 'no-cache',
    'Referer': f'{config["address"]}/docs/api/'
}

    json_data = {
    'frequency': freq_hz,
    'duration': round(time_s*1000)-10,
}

    response = requests.post('{config["address"]}/api/v1/printer/beep', headers=headers, json=json_data, verify=False)


def make_sound(freq: int, time_ms: int):
    make_request(freq, time_ms/1000)
    print(f'sleeping {time_ms/1000}')


def main():
    whole_note = 2105.26315789  # in ms
    while True:
        for thisNote in range(0, len(data), 2):
            divider = data[thisNote + 1]
            if divider > 0:
                noteDuration = whole_note / divider
            else:
                noteDuration = whole_note / abs(divider)
                noteDuration *= 1.5

            before = time()

            make_sound(data[thisNote], noteDuration * 0.9)

            while time()-before <= noteDuration/1000:
                sleep(0.001)

            sleep(0.02)
        sleep(5)


if __name__ == '__main__':
    main()

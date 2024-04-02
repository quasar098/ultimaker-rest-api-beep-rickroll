# ultimaker rest api beep rickroll

utilize ultimaker 3d printers perform a rickroll via beep instructions from the rest api built in to the printer

copied timestamps & hz from [here](https://github.com/robsoncouto/arduino-songs/blob/master/nevergonnagiveyouup/nevergonnagiveyouup.ino)

## notice

may or may not work, this is untested code since i do not have access to an ultimaker 3d printer currently

this works by using the swagger api built into my ultimaker printer. one of the endpoints allows the printer to "beep" at different frequencies for different times, so rick rolling is possible on my ultimaker printer

## how to use

find the ip address of the printer, and connect to it on the web dashboard

go to the `/docs/api/` on the printer

then, go to the authorization section and request credentials

then, go over to your 3d printer and press allow access or whatever

then, open up the devtools panel in your browser and go to the networking tab

then, make a beep request (on the printer section of the rest api webpage)

there should be one networking request in the devtools networking section, so just click that and scroll until you find the `Authorization` request header, and copy some values into a newly created config.json (you must create it, and dont forget to use correct json format) like below

```json
{
    "username": "copy and replace this text here",
    "nonce": "copy and replace this text here",
    "response": "copy and replace this text here",
    "nc": "copy and replace this text here",
    "cnonce": "copy and replace this text here",
    "address": "replace this"
}
```

for the `address` in the json, just put in the address of the printer and use http protocol (e.g. `http://192.168.1.56`)

i think that's it maybe i missed something maybe i didnt idk

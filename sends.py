from settings import TOKEN, URL
import requests


def send_message(chat_id: int, text, parse_mode=False):
    url = URL+'sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    if parse_mode:
        payload["parse_mode"] = "HTML"

    requests.get(url, params=payload)

def send_contact(chat_id, numer, fname, lname=None):
    url = URL+"sendContact"
    payload = {
        "chat_id": chat_id,
        "phone_number": numer,
        "first_name": fname,
    }
    if lname:
        payload['last_name'] = lname

    requests.post(url, params=payload)

def send_photo(chat_id, photo):
    url=URL+'sendPhoto'
    payload = {
        "chat_id": chat_id,
        "photo": photo,
    }
    requests.get(url, params=payload)

def send_location(chat_id: int, latitude, longitude):
    url=URL+"sendLocation"

    payload = {
        "chat_id" : chat_id,
        "latitude" : latitude,
        "longitude" : longitude
    }

    requests.get(url, params = payload)

def send_video(chat_id: str, video):
    url=URL+"sendVideo"

    payload = {
        "chat_id" : chat_id,
        "video" : video
    }

    requests.get(url, params=payload)

def send_document(chat_id: str, document ):
    url=URL+"sendDocument"

    payload = {
        "chat_id" : chat_id,
        "document" : document
    }

    requests.get(url, params=payload)

def send_voice(chat_id: int, voice):
    url=URL+"sendVoice"

    payload = {
        "chat_id" : chat_id,
        "voice" : voice
    }

    requests.get(url, params=payload)

def send_audio(chat_id: int, audio):
    url=URL+"sendAudio"

    payload = {
        "chat_id" : chat_id,
        "audio" : audio
    }

    requests.get(url, params=payload)

def send_video_note(chat_id: int, video_note):
    url=URL+"sendVideoNote"

    payload = {
        "chat_id" : chat_id,
        "video_note" : video_note
    }

    requests.get(url, params=payload)

def send_emoji(chat_id, emoji=None):
    url=URL+"sendDice"

    payload = {
        "chat_id" : chat_id,
        "emoji" : emoji
    }

    requests.get(url, params=payload)


# send_contact("927181585", "+998990235051", "Jahongir", "Musayev")
# send_location("927181585", "39.658174", "66.919475")
# send_video("927181585", "BAACAgIAAxkBAANIZW3azxfWc5PKL4v5plqYswTroI8AAqg7AAKQQ3BLKNmZvYXQjlgzBA")
# send_document("927181585", "BQACAgIAAxkBAANKZW3bz4mcGMzN8gupN-uVlrBdOOgAArg7AAKQQ3BLcr3vFs2gTuozBA")
# send_voice("927181585","AwACAgIAAxkBAANMZW3dcQgPQZfXNavE2Xb_I-T8O1gAAsw7AAKQQ3BLOrWaKeOJFfszBA")
# send_audio("927181585" , "CQACAgIAAxkBAANPZW3zjQeaRmuC8pF4jnNzzo-5lJkAAgM5AAKEc5FJLyRl4IhqbsozBA")
send_emoji("927181585")
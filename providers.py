from joke import Joke
import requests


class JokeAPIProvider(Joke):

    def get_random_joke(self):
        url = "https://v2.jokeapi.dev/joke/Any"

        response = requests.get(url)

        data = response.json()

        if data["type"] == "single":
            return data["joke"]
        if data["type"] == "twopart":
            return data["setup"] + "\n" + data["delivery"]


class OfficialJokeProvider(Joke):

    def get_random_joke(self):
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        data = response.json()
        return data["setup"] + "\n" + data["punchline"]


class DadJokeProvider(Joke):

    def get_random_joke(self):
        url = "https://icanhazdadjoke.com/"
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["joke"]

import random
from providers import (
    JokeAPIProvider,
    OfficialJokeProvider,
    DadJokeProvider

)


def main():
    provider_list = [
        JokeAPIProvider(),
        OfficialJokeProvider(),
        DadJokeProvider

    ]
    provider = random.choice(provider_list)
    random_joke = provider.get_random_joke()
    print(random_joke)


if __name__ == "__main__":
    main()

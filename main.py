import random
from providers import (
    JokeAPIProvider,
    OfficialJokeProvider,
    DadJokeProvider

)


def get_random_joke():
    providers_list = [
        JokeAPIProvider(),
        OfficialJokeProvider(),
        DadJokeProvider()
    ]

    provider = random.choice(providers_list)
    return provider.get_random_joke()


def get_jokeapi_joke():
    provider = JokeAPIProvider()
    return provider.get_random_joke()


def get_official_joke():
    provider = OfficialJokeProvider()
    return provider.get_random_joke()


def get_dad_joke():
    provider = DadJokeProvider()
    return provider.get_random_joke()


def menu():
    print("===== JOKE GENERATOR =====")
    print("1.Random Joke")
    print("2.JokeAPI")
    print("3.Official Joke")
    print("4.Dad Joke")
    print("0.Exit")


def main():
    while True:
        menu()
        try:
            choice = int(input("Enter your choice(number): "))
        except ValueError:
            print("Enter a number from 0 to 4")
            continue
        if choice == 1:
            print(get_random_joke())

        elif choice == 2:
            print(get_jokeapi_joke())

        elif choice == 3:
            print(get_official_joke())

        elif choice == 4:
            print(get_dad_joke())

        elif choice == 0:
            print("bye")
            break

        else:
            print("please enter a number from 0 to 4")


if __name__ == "__main__":
    main()

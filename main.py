import requests
from bs4 import BeautifulSoup
from googletrans import Translator

#функция, которая получает информацию
def get_english_words():
    url = "https://randomword.com/"

    try:
        response = requests.get(url)

        #объект Soup
        soup = BeautifulSoup(response.content, "html.parser")

        english_words = soup.find("div", id="random_word").text.strip()

        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }

    except:
        print("Произошла ошибка")

def translate_word(word):
    translator = Translator()
    result = translator.translate(word, dest="ru")
    return result.text


# функция с игрой
def word_game():
    print("Добро пожаловать в игру!\n")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        #Перевод
        translated_word = translate_word(word)

        #start game
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")

        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word} ({translated_word})")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n  ")
        if play_again != "y":
            print("\nСпасибо за игру!  ")
            break

word_game()



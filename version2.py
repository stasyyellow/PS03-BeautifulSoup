import requests
from bs4 import BeautifulSoup
from googletrans import Translator


class WordFetcher:
    def __init__(self):
        self.url = "https://randomword.com/"

    def get_english_words(self):
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, "html.parser")

            english_words = soup.find("div", id="random_word").text.strip()
            word_definition = soup.find("div", id="random_word_definition").text.strip()

            return {
                "english_words": english_words,
                "word_definition": word_definition
            }
        except:
            print("Произошла ошибка")


class WordTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_word(self, word):
        result = self.translator.translate(word, dest="ru")
        return result.text


# Класс для игры, наследующийся от WordFetcher и WordTranslator
class WordGame(WordFetcher, WordTranslator):
    def __init__(self):
        super().__init__()  # вызываем инициализацию родительских классов
        self.translator = WordTranslator()  # инициализируем объект класса WordTranslator

    def play_game(self):
        print("Добро пожаловать в игру!\n")
        while True:
            word_dict = self.get_english_words()
            word = word_dict.get("english_words")
            word_definition = word_dict.get("word_definition")

            translated_word = self.translate_word(word)

            print(f"Значение слова - {word_definition}")
            user = input("Что это за слово? ")

            if user == word:
                print("Все верно!")
            else:
                print(f"Ответ неверный, было загадано это слово - {word} ({translated_word})")

            play_again = input("Хотите сыграть еще раз? y/n  ")
            if play_again.lower() != "y":
                print("\nСпасибо за игру!  ")
                break


# Запуск игры
if __name__ == "__main__":
    game = WordGame()
    game.play_game()


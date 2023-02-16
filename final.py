'''
1. Открыть ссылку https://swapi.dev/

2. Отправить метод GET https://swapi.dev/api/people/4/

3. Написать код который будет сохранять всех персонажей (имена), которые снимались во всех фильмах, с Дарт Вейдером, в тестовый файл, при этом в файле не должны содержаться дубли (В ИДЕАЛЕ, НО НЕ ОБЯЗАТЕЛЬНО).
'''

import requests


class Characters:

    def get_all_characters(self):

        dart_url = 'https://swapi.dev/api/people/4/'
        dart_result = requests.get(dart_url)
        print(dart_result.text)

        films_list = []
        films_result = dart_result.json()
        films = films_result.get('films')
        for i in films:
            films_list.append(i)
        print(films_list)

        characters_urls = []
        for film in films_list:
            film_url = film
            film_info = requests.get(film_url)
            film_info_result = film_info.json()
            chars = film_info_result.get('characters')
            for c in chars:
                if c not in characters_urls:
                    characters_urls.append(c)
        print(characters_urls)

        with open('final.txt', 'a+') as file:
            for char in characters_urls:
                character_url = char
                char_info = requests.get(character_url)
                char_info_result = char_info.json()
                character = char_info_result.get('name')
                file.writelines(f'{character}\n')
            file.close()



ch = Characters()
ch.get_all_characters()



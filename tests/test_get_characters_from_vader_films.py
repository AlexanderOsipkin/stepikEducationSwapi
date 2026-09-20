import requests


class TestDarthVader:
    """Получаем персонажей, которые снимались вместе с Дартом Вейдером"""

    def test_get_characters_from_vader_films(self):
        """Получаем персонажей из всех фильмов Дарта Вейдера и сохраняем их в файл"""

        # Основные данные персонажа
        base_url = "https://swapi.info/api"
        character_url = f"{base_url}/people/4"
        file_name = "vader_characters.txt"
        character_name = "Darth Vader"

        print(f"URL Персонажа - {character_name}: {character_url}")

        # Получаем информацию о Дарте Вейдере
        person_result = requests.get(character_url)
        print(f"Статус код GET запроса: {person_result.status_code}")

        # Проверяем успешность запроса
        assert person_result.status_code == 200
        print(f"Данные {character_name} получены успешно")

        character = person_result.json()

        # Получаем список фильмов в которых снимался персонаж
        film_urls = character.get("films")
        print(f"Количество фильмов {character_name}: {len(film_urls)}")

        # Используем set, чтобы имена персонажей не дублировались
        characters = set()

        # Получаем персонажей каждого фильма
        for film_url in film_urls:
            print(f"Получаем данные фильма: {film_url}")

            film_result = requests.get(film_url)
            print(f"Статус код GET фильма: {film_result.status_code}")

            # Проверяем успешность запроса
            assert film_result.status_code == 200

            film = film_result.json()
            film_title = film.get("title")
            print(f"Фильм: {film_title}")

            # Получаем ссылки на персонажей фильма
            character_urls = film.get("characters")
            print(f"Количество персонажей в фильме: {len(character_urls)}")

            # Получаем имя каждого персонажа
            for character_url in character_urls:
                character_result = requests.get(character_url)

                # Проверяем успешность запроса
                assert character_result.status_code == 200

                character = character_result.json()
                character_name = character.get("name")

                # Добавляем имя
                characters.add(character_name)

        # Сохраняем имена персонажей в файл
        with open(file_name, "w", encoding="utf-8") as file:
            for character_name in sorted(characters):
                file.write(character_name + "\n")

        print(f"Всего уникальных персонажей: {len(characters)}")
        print(f"Все персонажи сохранены в файл {file_name}")
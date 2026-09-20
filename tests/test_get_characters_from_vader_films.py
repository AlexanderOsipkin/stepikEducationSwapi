from utils.swapi import Swapi


class TestCharacterFilms:
    """Получаем персонажей, которые снимались вместе с выбранным персонажем"""

    def test_get_characters_from_films(self):
        """Получаем персонажей из всех фильмов выбранного персонажа и сохраняем их в файл"""

        # Основные данные персонажа
        character_id = 4
        character_name = "Darth Vader"
        file_name = "vader_characters.txt"

        swapi = Swapi()

        print(f"ID персонажа - {character_id}")
        print(f"Имя персонажа - {character_name}")

        # Получаем информацию о персонаже
        character = swapi.get_character(character_id)
        print(f"Данные {character_name} получены успешно")

        # Получаем список фильмов в которых снимался персонаж
        film_urls = character.get("films")
        print(f"Количество фильмов {character_name}: {len(film_urls)}")

        # Используем set, чтобы имена персонажей не дублировались
        characters = set()

        # Получаем персонажей каждого фильма
        for film_url in film_urls:
            print(f"Получаем данные фильма: {film_url}")

            film = swapi.get_film(film_url)
            film_title = film.get("title")
            print(f"Фильм: {film_title}")

            # Получаем ссылки на персонажей фильма
            character_urls = film.get("characters")
            print(f"Количество персонажей в фильме: {len(character_urls)}")

            # Получаем имя каждого персонажа
            for character_url in character_urls:
                character = swapi.get_character_by_url(character_url)
                character_name = character.get("name")

                # Добавляем имя
                characters.add(character_name)

        # Сохраняем имена персонажей в файл
        with open(file_name, "w", encoding="utf-8") as file:
            for character_name in sorted(characters):
                file.write(character_name + "\n")

        print(f"Всего уникальных персонажей: {len(characters)}")
        print(f"Все персонажи сохранены в файл {file_name}")
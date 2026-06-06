# N7Playwright POM Framework

Базовий фреймворк для автоматизації UI тестування на базі Python, Playwright та Pytest.

## Структура
- `config/` - Налаштування середовища (URL, таймаути).
- `pages/` - Класи Page Object Model (POM).
- `tests/` - Тестові сценарії (Pytest).
- `utils/` - Допоміжні утиліти (логер).

## Запуск тестів
1. Активуйте віртуальне середовище: `.\venv\Scripts\Activate.ps1`
2. Запустіть тести: `pytest tests/ui/test_sauce_demo.py -s`

## N8Запуск Юніт-тестів
У проєкті реалізовано юніт-тести для допоміжних утиліт (папка `tests/unit/`).
Для їх запуску виконайте команду:
`python -m pytest tests/unit/`

## N9Запуск Інтеграційних API-тестів
У проєкті реалізовано клієнт та інтеграційні тести для перевірки API за допомогою Playwright `APIRequestContext`.
Для запуску виконайте команду:
`python -m pytest tests/integration/`

## N10Системне тестування (E2E)
Для запуску наскрізних системних сценаріїв використовуйте команду:
`python -m pytest tests/system/`
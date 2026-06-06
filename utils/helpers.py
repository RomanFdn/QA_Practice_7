def format_player_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("Ім'я має бути рядком")
    return name.strip().capitalize()

def calculate_win_rate(wins: int, total_matches: int) -> float:
    if total_matches == 0:
        return 0.0
    if wins < 0 or total_matches < 0 or wins > total_matches:
        raise ValueError("Некоректні дані матчу")
    return round((wins / total_matches) * 100, 2)

"""
Игра камень ножницы бумага


R = Камень
S = Ножницы
P = Бумага
"""
class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(data_games: list) -> str:
    out_data = data_games[0][0] + " " + \
        data_games[0][1]  # Сразу предположим, что побеждает первый игрок, в противном случае перезаписываем переменную
    if len(data_games) != 2:
        raise WrongNumberOfPlayersError
    for player_info in data_games:
        if player_info[1] in ["P", "S", "R"]:
            continue
        else:
            raise NoSuchStrategyError
    player1_action, player2_action = data_games[0][1], data_games[1][1]
    if player1_action == player2_action:
        return out_data
    if player1_action == 'R' and player2_action == 'S':  # Камень - Ножницы
        return out_data
    if player1_action == 'S' and player2_action == 'P':  # Ножницы - Бумага
        return out_data
    if player1_action == 'P' and player2_action == 'R':  # Бумага - Камень
        return out_data
    else:
        out_data = data_games[1][0] + " " + data_games[1][1]
        return out_data




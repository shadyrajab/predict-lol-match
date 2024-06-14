import requests
from utils.var import RG_KEY
import pandas as pd


def get_summoner_puuid(nickname: str, tagline: str, region: str, handler) -> str:
    response = requests.get(
        f"https://{region.lower()}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nickname}/{tagline}?api_key={RG_KEY}"
    )
    if response.status_code == 200:
        return response.json()["puuid"]
    else:
        return handler("Nick de usuário inválido ou inexistente na região selecionada.")


def get_summoner_matchs(puuid: str, server: str) -> list:
    response = requests.get(
        f"https://{server}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count=10&api_key={RG_KEY}"
    )
    matchs = []
    for match in response.json():
        response = requests.get(
            f"https://{server}.api.riotgames.com/lol/match/v5/matches/{match}?api_key={RG_KEY}"
        ).json()

        for participant in response["info"]["participants"]:
            if participant["puuid"] == puuid:
                for column in ["challenges", "missions", "perks"]:
                    del participant[column]

                matchs.append(participant)

    return pd.DataFrame(matchs)

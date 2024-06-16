import requests
import pandas as pd


def format_data(dataframe: pd.DataFrame):
    remove_ping_columns(dataframe)
    sum_kills_and_assists(dataframe)
    sum_minions_and_jungle_minions_killed(dataframe)
    remove_games_that_ended_in_early_surrender(dataframe)
    delete_generic_columns(dataframe)
    get_item_name_by_id(dataframe)
    get_spell_name_by_id(dataframe)


def remove_ping_columns(dataframe: pd.DataFrame):
    ping_columns = []
    for column in dataframe.columns:
        if "Pings" in str(column):
            ping_columns.append(column)

    dataframe["allPings"] = dataframe[ping_columns].sum(axis=1)
    dataframe.drop(columns=ping_columns, inplace=True)


def sum_kills_and_assists(dataframe: pd.DataFrame):
    dataframe["participations"] = dataframe["kills"] + dataframe["assists"]


def sum_minions_and_jungle_minions_killed(dataframe: pd.DataFrame):
    farm_columns = []
    for column in dataframe.columns:
        if "MinionsKilled" in str(column):
            farm_columns.append(column)

    dataframe["totalFarm"] = dataframe[farm_columns].sum(axis=1)
    dataframe.drop(columns=farm_columns, inplace=True)

def remove_games_that_ended_in_early_surrender(dataframe: pd.DataFrame):
    dataframe.drop(
        dataframe[dataframe["gameEndedInEarlySurrender"]].index, inplace=True
    )


def delete_generic_columns(dataframe: pd.DataFrame):
    columns_to_delete = [
        "goldEarned",
        "championId",
        "champExperience",
        "doubleKills",
        "tripleKills",
        "quadraKills",
        "pentaKills",
        "largestMultiKill",
        "largestKillingSpree",
        "killingSprees",
        "summonerName",
        "summonerLevel",
        "summonerId",
        "riotIdTagline",
        "riotIdGameName",
        "puuid",
        "profileIcon",
        "participantId",
        "eligibleForProgression",
        "visionWardsBoughtInGame",
        "wardsKilled",
        "wardsPlaced",
        "gameEndedInEarlySurrender",
        "assists",
        "kills",
        "gameEndedInSurrender",
        "detectorWardsPlaced",
        "championTransform",
        "itemsPurchased",
        "inhibitorKills",
        "damageDealtToBuildings",
        "damageDealtToTurrets",
        "largestCriticalStrike",
        "lane",
        "role",
        "nexusLost",
        "nexusKills",
        "nexusTakedowns",
        "firstBloodKill",
        "physicalDamageDealt",
        "physicalDamageTaken",
        "firstTowerKill",
        "magicDamageDealt",
        "magicDamageTaken",
        "teamEarlySurrendered",
        "totalDamageDealt",
        "trueDamageDealt",
        "trueDamageTaken",
        "objectivesStolen",
        "turretKills",
        "totalDamageShieldedOnTeammates",
        "totalTimeCCDealt",
        "totalUnitsHealed",
    ]
    dataframe.drop(columns=columns_to_delete, inplace=True)


def get_item_name_by_id(dataframe: pd.DataFrame):
    itens = "https://ddragon.leagueoflegends.com/cdn/14.11.1/data/pt_BR/item.json"
    response = requests.get(itens).json()["data"]

    for item in ["item0", "item1", "item2", "item3", "item4", "item5", "item6"]:
        dataframe[item] = dataframe[item].apply(
            lambda s: response.get(str(s), {}).get("name", "No Item")
        )


def get_spell_name_by_id(dataframe: pd.DataFrame):
    spells = {
        "4": "Flash",
        "12": "Teleport",
        "14": "Ignite",
        "11": "Smite",
        "7": "Heal",
        "6": "Haste",
        "3": "Exhaust",
        "1": "Cleanse",
        "21": "Barrier",
    }
    for spell in ["summoner1Id", "summoner2Id"]:
        dataframe[spell] = dataframe[spell].apply(lambda x: spells.get(str(x)), None)

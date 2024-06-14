from dotenv import load_dotenv
import os

load_dotenv()

RG_KEY = os.getenv('RGKEY')

REGIONS = {
    'BR1': "AMERICAS",
    'EUN1': "EUROPE",
    'EUW1': "EUROPE",
    'JP1': "ASIA",
    'KR': "ASIA",
    'LA1': "AMERICAS",
    'LA2': "AMERICAS",
    'NA1': "AMERICAS",
    'OC1': "SEA",
    'PH2': "SEA",
    'RU': "EUROPE",
    'SG2': "SEA",
    'TH2': "SEA",
    'TR1': "EUROPE",
    'TW2': "SEA",
    'VN2': "SEA"
  }

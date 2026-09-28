"""
Isaam Shah
Sept 28, 2026
Lab 7: APIs and data collection
"""

import pandas as pd

# ----------------------------
# 1. Example DataFrame
# ----------------------------

dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}

df = pd.DataFrame(dict_)

print(df.head())
print(df.mean())

# ----------------------------
# 2. Get NBA Teams
# ----------------------------

from static import get_teams
nba_teams = get_teams()

print(f"First 2 teams: {nba_teams[:2]}")

# convert list of dictionary into a data frame
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

# filter the row that contains the "warriors" nickname
df_warriors=df_teams[df_teams['nickname']==' Warriors']
print(df_warriors)

# ----------------------------
# 3. Working with external API
# ----------------------------

# a. Download the pickle file
import requests


url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# save the download file as Golden_State.pkl
file_name = "Golden_State.pkl"

print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("Download failed.")

# b. Load DataFrame from pickle
games = pd.read_pickle(file_name)
print("\nGames data from pickle file: ")
print(games.head())

# c. Filter GSW vs Raptors
warriors_vs_raptors = games[games["MATCHUP"].str.contains("TOR")]
gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' vs. ')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

# d. Calculate averages
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"Warriors home average {home_avg_plus}")
print(f"Warriors away average {away_avg_plus}")
print(f"Warriors home points {home_avg_pts}")
print(f"Warriors away points {away_avg_pts}")

# Pick two teams to work on a through b (Liverpool, ManCity)
# a
url2 = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
file_name2 = "epl_matches.csv"

print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name2, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("Download failed.")

# b. Load DataFrame from csv
games2 = pd.read_csv(file_name)
print("\nGames data from csv file:")
print(games.head())

# c. Filter 
# Liverpool vs ManCity
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' vs. ')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]










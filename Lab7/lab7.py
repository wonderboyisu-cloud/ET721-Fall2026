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

# convert list of dictionary into a DataFrame
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

# filter the row that contains the "Warriors" nickname
df_warriors=df_teams[df_teams['nickname'] == 'Warriors']
print(df_warriors)

# access and save the id, which is the first row first column of warriors
id_warriors=df_warriors[['id']].values[0][0]
print(f"Id of Warriors = {id_warriors}")

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
print(f"Warriors home points average {home_avg_pts}")
print(f"Warriors away points average {away_avg_pts}")

print("\n---------LAB EXERCISE ----------")
# Pick two teams to work on step a through d. (Liverpool, ManCity)
# a 
url2 = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
file_name2 = "epl_matches.csv"

print("\nDownloading external data...")
response2 = requests.get(url2)
if response2.status_code == 200:
    with open(file_name2, "wb") as f:
        f.write(response2.content)
    print("Download complete.")
else:
    print("Download failed.")

# b
games2 = pd.read_csv(file_name2)
print("\nGames data from csv file:")
print(games2.head())
print("\n")

# c
# Liverpool vs Chelsea
lvp_home_vs_Chelsea = games2[(games2["HomeTeam"].str.contains("Liverpool")) & (games2["AwayTeam"].str.contains("Chelsea"))]
lvp_away_vs_Chelsea = games2[(games2["HomeTeam"].str.contains("Chelsea")) & (games2["AwayTeam"].str.contains("Liverpool"))]

# d
# Liverpool Goals
home_avg_g = lvp_home_vs_Chelsea['FTHG'].mean()  
away_avg_g = lvp_away_vs_Chelsea['FTAG'].mean()  

# Chelsea Goals
home_avg_g2 = lvp_away_vs_Chelsea['FTHG'].mean() 
away_avg_g2 = lvp_home_vs_Chelsea['FTAG'].mean() 

print(f"Liverpool home goals average: {home_avg_g}")
print(f"Liverpool away goals average: {away_avg_g}")
print(f"Chelsea home goals average: {home_avg_g2}")
print(f"Chelsea away goals average: {away_avg_g2}")







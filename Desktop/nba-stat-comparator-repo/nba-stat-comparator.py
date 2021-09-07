#Imports
from nba_api.stats.library.parameters import NumberOfGames
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm

#NBA stat database.
from nba_api.stats.static import players
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats

#Makes sure that the entire dataframe is displayed.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def players_stat_detail(name,id,type):
    player_dict = [player for player in players.get_players() if player['full_name'] == name][0]

    #Dataframe that illustrates player's career stats.
    career = playercareerstats.PlayerCareerStats(player_id=player_dict['id'])
    career_dataframe = career.get_data_frames()[0]

    team_id = career_dataframe[career_dataframe['SEASON_ID'] == id]['TEAM_ID']

    shotchartlist = shotchartdetail.ShotChartDetail(team_id = int(team_id), player_id = int(player_dict['id']), season_type_all_star = type, season_nullable = id, context_measure_simple = "FGA").get_data_frames()

    print(career_dataframe)



def draw(graphic, n1, i1, t1, n2, i2, t2):
    if graphic is None:
        graphic = plt.figure()
        ax = graphic.add_subplot()
        graphic.subplots_adjust(top=0.85)
          
    ax.text(0, 0.95, n1, transform=ax.transAxes, color='black', fontsize=12)
    ax.text(0, 0.90, i1, transform=ax.transAxes, color='black', fontsize=9)
    ax.text(0, 0.85, t1, transform=ax.transAxes, color='black', fontsize=9)
    ax.text(1, 0.95, n2, transform=ax.transAxes, horizontalalignment='right', color='black', fontsize=12)
    ax.text(1, 0.90, i2, transform=ax.transAxes, horizontalalignment='right', color='black', fontsize=9)
    ax.text(1, 0.85, t2, transform=ax.transAxes, horizontalalignment='right', color='black', fontsize=9)
    
    ax.text(1, 0.85, t2, transform=ax.transAxes, horizontalalignment='right', color='black', fontsize=9)

    return graphic

if __name__ == "__main__":

    #Generates title.
    title = 'Test'

    players_stat_detail('Kevin Durant',2020-21,'Regular Season')

    #Asks user for the two players' general info.
    player_name1 = input ("Enter player 1's full name: ")
    season_id1 = input ("Input season in format (####-##): ")
    season_type1 = input ("Regular Season (R) or Playoffs (P): ")
    if season_type1 == 'R':
        season_type1 = 'Regular Season'
    elif season_type1 == 'P':
        season_type1 = 'Playoffs'

    player_name2 = input ("Enter player 2's full name: ")
    season_id2 = input ("Input season in format (####-##): ")
    season_type2 = input ("Regular Season (R) or Playoffs (P): ")
    if season_type2 == 'R':
        season_type2 = 'Regular Season'
    elif season_type2 == 'P':
        season_type2 = 'Playoffs'    
    
    #Default, for testing.  
    draw(None, 'Kevin Durant','2020-21','Playoffs','James Harden','2020-21','Playoffs')
    #draw(None, player_name1, season_id1, season_type1, player_name2, season_id2, season_type2)
    plt.show()
   
import random
import numpy as np

def test(csv):
  player = csv.split(",")

  rteam = random.sample(player, len(player))

  team1 = rteam[:int(len(player)/2)]
  team2 = rteam[int(len(player)/2):]
  teams = [team1,team2]

  return teams

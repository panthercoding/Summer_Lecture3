import random
import numpy as np

"""
No need to modify. This premade function reads from a .txt file
and obtains the sorted list of teams from best seed to worst seed.
"""
def getRankedList(filename):
  with open(filename,"r") as file:
    teams = file.readlines()
    teams = [team.replace("\n","").strip() for team in teams]
  return(teams)

"""
TO DO: teams is a sorted list with the number 1 seed at index 0
and the bottom seed at the end of the list. this function
should return a dictionary where each key is a team name
and the corresponding value is the seed of that team

-> Hint: We iterate through the list and incrementally 
add a team entry to the dictionary each time inside the loop
"""
def buildSeedDictionary(teams):
  findSeed = {} 
  rank = 1
  for team in teams:
    """complete the code inside the loop """
  return(findSeed)

"""
Accepts the two teams as input as well as a seed dictionary.
It should first look up the seeds of both teams in the dictionary
and then return two numbers in the following order: the probability 
of team 1 winning, and the probability of team 2 winning. 

P(team 1 wins) = (seed of team 2)/(sum of the two seeds)
P(team 2 wins) = (seed of team 1)/(sum of the two seeds)
"""
def win_probabilities(team1,team2,findSeed):
  """delete the placeholder return below and complete the program """
  return 0,0

"""
No need to modify. It randomly returns a winner between the two
teams based on the probability function you implemented above.
You can print the winner of each contest by removing the
comment quotes of the if else loops. 
"""
def findWinner(team1,team2,findSeed):
  team1_prob, team2_prob = win_probabilities(team1,team2,findSeed)
  winner = np.random.choice([team1,team2],p=[team1_prob,1-team1_prob])
  """
  if (winner == team1):
    print("{} have eliminated the {}.".format(team1,team2))
  else:
    print("{} have eliminated the {}.".format(team2,team1))
  """
  return winner

"""
Should recursively simulate an elimination tournament involving a
list of teams: you can assume the number of teams is a power of 2 (1,2,4,8,16,...).

As a strategy, consider the base case where there is just one team:
trivially, that team should win. Otherwise, split the list of teams
into two brackets, find the winner of each bracket by calling playoffs,
and then have the two bracket winners face off using the findWinner( ) method.

to split the list, using list slicing:
 -> teams[:int(k)] will return a list of the first k teams
 -> teams[int(k):] will return a list of the remaining teams
"""
def playoffs(teams,findSeed):
  """ TO DO: Complete this function and delete the placeholder return below"""
  return(0)

"""
No need to modify. This is the main function that combines
everything from above to simulate a single NBA playoffs. 

Note that two fictional NBA teams were added to create
a 32-team tournament.
"""

def main():
  teams = getRankedList("nba_teams.txt")
  findSeed = buildSeedDictionary(teams)
  np.random.shuffle(teams)
  champion = playoffs(teams,findSeed)
  print()
  print("CONGRATULATIONS TO THE {}!".format(champion.upper()))

main()

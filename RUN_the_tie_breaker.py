from match import Match
from player import Player
from team import Team


def the_tie_breaker():

	#Initialising batting team
	Lengaburu = Team("Lengaburu")
	Enchai = Team("Enchai")

	the_match = Match(Lengaburu, Enchai)

	Lengaburu.createBatsmen(the_match)
	Enchai.createBatsmen(the_match)

	the_match.playMatch()

	
the_tie_breaker()
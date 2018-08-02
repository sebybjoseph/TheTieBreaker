from match import Match
from player import Player
from team import Team


def the_tie_breaker():

	#Initialising batting team
	Lengaburu = Team("Lengaburu")
	batsmen = []
	Kirat_Boli = Player()
	N_S_Nodhi = Player()
	batsmen.append(Lengaburu.createBatsman(Kirat_Boli, "Kirat Boli", [0.05, 0.10, 0.25, 0.10, 0.25, 0.01, 0.14, 0.10]))
	batsmen.append(Lengaburu.createBatsman(N_S_Nodhi, "N. S. Nodhi", [0.05, 0.15, 0.15, 0.10, 0.20, 0.01, 0.19, 0.15]))
	Lengaburu.batsmen = batsmen

	#Initialising Bowling team
	Enchai = Team("Enchai")
	batsmen = []
	D_B_Vellyers = Player()
	H_Mamla = Player()
	batsmen.append(Enchai.createBatsman(D_B_Vellyers, "D. B. Vellyers", [0.05, 0.10, 0.25, 0.10, 0.25, 0.01, 0.14, 0.10]))
	batsmen.append(Enchai.createBatsman(H_Mamla, "H. Mamla", [0.10, 0.15, 0.15, 0.10, 0.20, 0.01, 0.19, 0.10]))
	Enchai.batsmen = batsmen

	the_match = Match(Lengaburu, Enchai)

	the_match.playMatch()

	


the_tie_breaker()
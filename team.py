from player import Player

BALLS = 6
ONE_BALL = 1
OUTCOME_FOR_WICKET = "Out"

class Team:
	batsmen = []
	total_runs = 0
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def createBatsman(self, player, name, weights):
		player = Player(name, weights)
		self.batsmen.append(player)
		
		return player

	def batFirst(self):
		striker, non_striker = self.batsmen[0], self.batsmen[1]
		commentary = []
		commentary.append(self.name + " innings : ")
		for ball in range(1, BALLS+1):
			outcome = striker.getOutcome()[0]
			if outcome != OUTCOME_FOR_WICKET:
				striker.addRuns(outcome)
				striker.addBallsFaced(ONE_BALL)
				self.total_runs += outcome
				commentary.append("0."+str(ball)+" "+striker.name+" scored "+str(outcome))
				if outcome%2 != 0:
					striker, non_striker = non_striker, striker
			else:
				commentary.append("0."+str(ball)+" "+striker.name+" gets out. "+ self.name + " all out.")
				striker.addBallsFaced(ONE_BALL)
				striker.changeStatus("Out")
				break
		return self.total_runs, commentary

	def chase(self, runs_required):
		striker, non_striker = self.batsmen[0], self.batsmen[1]
		commentary = []
		commentary.append("\n"+self.name + " innings : ")
		match_won = False
		for ball in range(1, BALLS+1):
			outcome = striker.getOutcome()[0]
			if outcome != OUTCOME_FOR_WICKET:
				striker.addRuns(outcome)
				striker.addBallsFaced(ONE_BALL)
				self.total_runs += outcome
				commentary.append("0."+str(ball)+" "+striker.name+" scored "+str(outcome))
				if self.total_runs > runs_required:
					return "Win", commentary
					match_won = True
					break
				else:
					if outcome%2 != 0:
						striker, non_striker = non_striker, striker
			else:
				commentary.append("0."+str(ball)+" "+striker.name+" gets out. "+ self.name + " all out.")
				striker.addBallsFaced(ONE_BALL)
				striker.changeStatus("Out")
				if runs_required == self.total_runs:
					return "It's another tie ! ", commentary
				elif not match_won:
					return "Lost", commentary

		if runs_required == self.total_runs:
			return "It's another tie ! ", commentary
		elif not match_won:
			return "Lost", commentary

	def printSummary(self):
		print ("\n"+self.name+" - "+str(self.total_runs)+" runs.\n")
		for player in self.batsmen:
			player.printDetails()
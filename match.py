from player import Player

FIRST_BALL = 1
LAST_BALL = 6
BALLS_PER_OVER = 6
OUTCOME_FOR_WICKET = 'Out'
ONE_BALL = 1

class Match:
	
	commentary = []
	match_result = ""

	def __init__(self, batting_team, bowling_team):
		self.batting_team = batting_team
		self.bowling_team = bowling_team

	def playMatch(self):
		
		target, commentary = self.batting_team.batFirst()
		self.commentary += commentary
		
		result, commentary = self.bowling_team.chase(target)
		self.commentary += commentary
		
		if result == "Win":
			self.match_result = "\n"+self.bowling_team.name+" successfully chased the score."
		elif result == "Lost":
			self.match_result = "\n"+self.batting_team.name+" won by "+str(self.batting_team.total_runs - self.bowling_team.total_runs)+" runs"
		else:
			self.match_result = "\n"+result

		self.printMatchResult()

		self.batting_team.printSummary()
		self.bowling_team.printSummary()

		self.printCommentary()

	def printMatchResult(self):
		print (self.match_result)

	def printCommentary(self):
		print ("\n***Commentary***\n")
		for line in self.commentary:
			print (line)

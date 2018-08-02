import random

class Player:
	def __init__(self, name="", weighted_probability=[]):
		self.name = name
		self.possibilities = [0,1,2,3,4,5,6,'Out']
		self.weights = weighted_probability
		self.runs = 0
		self.balls_faced = 0
		self.status = "Not out"

	def getOutcome(self):
		return random.choices(self.possibilities,self.weights, k=1)

	def printDetails(self):
		star = ""
		if self.status == "Not out":
			star = "*"
		print (self.name, "-", str(self.runs)+star, "("+ str(self.balls_faced), "balls)")

	def __str__(self):
		return self.name

	def addRuns(self, runs):
		self.runs += runs

	def addBallsFaced(self, balls):
		self.balls_faced += balls

	def changeStatus(self, status):
		self.status = status
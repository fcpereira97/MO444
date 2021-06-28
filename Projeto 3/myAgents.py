from game import Agent
from game import Directions

class DumbAgent(Agent):

	def getAction(self, state):

		print ("Location: " + str(state.getPacmanPosition()))
		print ("Actions available: " + str(state.getLegalPacmanActions()))
		if Directions.WEST in state.getLegalPacmanActions():
			print ("Going West.")
			return Directions.WEST
		else:
			print ("Going West.")
			return Directions.STOP
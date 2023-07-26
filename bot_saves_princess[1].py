def directBot(steps, direction_one, directon_two):
	for i in range(abs(steps)):
		if steps < 0:
			print(direction_one)
		else:
			print(directon_two)
def solveBotSavesPrincess(multi_dimension):
	for i in range(len(multi_dimension)):
		for j in range(len(multi_dimension[i])):
			if multi_dimension[i][j] == "m":
				bot_pos = [i, j]
			elif multi_dimension[i][j] == "p":
				princess_pos = [i, j]
	bot_y_direction = bot_pos[0] - princess_pos[0]
	bot_x_direction  = bot_pos[1] - princess_pos[1]
	directBot(bot_y_direction, "Down", "Up")
	directBot(bot_x_direction, "Right", "Left")
solveBotSavesPrincess([["-", "-", "-"], ["-", "m", "-"], ["-", "-", "p"]])
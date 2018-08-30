

#!/usr/bin/env python

import csv
import random

class team:
	def __init__(self, name, coefficient, nation, pot):
		self.name = name
		self.nation = nation
		self.coefficient = coefficient
		self.pot = pot
		self.avoiding = None
		self.possiblegroups = []
		self.impossiblegroups = []
		self.toppos = []
		self.botpos = []
		self.placed = False
		self.multi = False
		self.marked = False

	def place(self):
		self.placed = True
	
	# avoid : specific for same nation avoidance
	def avoid(self, team):
		if team != self.avoiding:
			self.avoiding = team
			print self.name + ' avoiding ' + team.name
	
	# add possible group
	def possible(self, group):
		# if group not in self.impossiblegroups:
		self.possiblegroups.append(group)
		if group.half == 1:
			self.toppos.append(group)
		else:
			self.botpos.append(group)
	
	def getPossible(self):
		return self.possiblegroups

	def getImpossible(self):
		return self.impossiblegroups

	def clear(self):
		self.possiblegroups = []

	# remove possible group / set group unavailable for team
	def remove(self, group):
		if group in self.possiblegroups:
			self.possiblegroups.remove(group)
			print self.name + ' removed ' + group.name
			if group.half == 1:
				self.toppos.remove(group)
				print 'toppos'
			else:
				self.botpos.remove(group)
				print 'botpos'

	# def remove(self, group):
	# 	if group in self.possiblegroups:
	# 		self.possiblegroups.remove(group)
	# 		print self.name + ' removed ' + group.name
	# 	self.impossiblegroups.append(group)

	def mn(self):
		self.multi=True
		
	def mark(self):
		self.marked = True
		
	def unmark(self):
		self.marked = False
		
	def posgroupissub(self, groupset, half = 0):
		issub = True
		if half == 0:
			for group in self.possiblegroups:
				if group not in groupset:
					issub = False
		elif half == 1:
			for group in self.toppos:
				if group not in groupset:
					issub = False
		elif half == 2:
			for group in self.botpos:
				if group not in groupset:
					issub = False
	
	
				
		return issub		
		
	def __str__(self):
		return str(self.name) + ' | ' + str(self.nation) + ' | Pot ' + str(self.pot)

class group:
	def __init__(self, name):
		self.name = name
		if name == 'A' or name == 'B' or name == 'C' or name == 'D':
			self.half = 1
		else: 
			self.half = 2
		self.teams = []
		
	def addteam(self, team):
		self.teams.append(team)
		
	def __str__(self):
		result = 'Group ' + self.name + ":\n"
		for team in self.teams:
			result = result + team.name + '\n'
		return result
		
# def test(pots, groups, nations):
	

# 	for pot in pots:
# 		emergency_groups = []
# 		emergency_teams = []
# 		tmp_possible_groups = []
# 		tmp_groups = groups[:]
# 		for tm in pot:
# 			print (tm.name)

# 		tmp_pot = pot[:]
# 		n=8
# 		while n>0:
# 			tmp_possible_groups = []
# 			# all teams
# 			for tm in tmp_pot:
# 				tm.clear()
# 				tmp_groups = groups[:]
# 				# go through team already drawn to get rid impossible groups
# 				for group in groups:
# 					# tm.possible(group)
# 					for team in group.teams:
# 						# avoid same pot, same nation, Russia/Ukraine
# 						if team.pot == tm.pot or \
# 						team.nation == tm.nation or \
# 						team.nation == 'RUS' and tm.nation == 'UKR' or \
# 						team.nation == 'UKR' and tm.nation == 'RUS':
# 							tm.remove(group)
# 							if group in tmp_groups:
# 								tmp_groups.remove(group)
# 								# print("removed from %s" % group.name)

# 						#avoid top/bottom half
# 						if team.nation == tm.nation and len(nations[tm.nation]) > 1 :
# 							print("more than one team from %s" % tm.nation)
# 							for team_in_nation in nations[tm.nation]:
# 								if tm.name == team_in_nation.name:
# 									tm_index = nations[tm.nation].index(team_in_nation)
# 								elif team.name == team_in_nation.name:
# 									team_index = nations[tm.nation].index(team_in_nation)
# 							if tm_index/2 == team_index/2:
# 								print(tm.name, "avoids", team.name)
# 								if group.half == 1:
# 									print("%s avoids top half" % tm.name)
# 									for group_half in groups[:]:
# 										if group_half.half == 1:
# 											if group_half in tmp_groups:
# 												tmp_groups.remove(group_half)
# 											tm.remove(group_half)
# 											# print("removed from %s" % group.name)
# 								else:
# 									print("%s avoids bottom half" % tm.name)
# 									for group_half in groups[:]:
# 										if group_half.half == 2:
# 											if group_half in tmp_groups:
# 												tmp_groups.remove(group_half)
# 											tm.remove(group_half)
# 											# print("removed from %s" % group.name)

# 						#only possible groups limited for teams

# 				# set possible groups lef
# 				print(tm.name)
# 				# if len(tmp_groups) == 1:
# 				# 	print("ONLY ONE POSSIBLE GROUP %s" % tmp_groups[0].name)
# 				# 	for tmm in tmp_pot[:]:
# 				# 		print("ASDFASDF")
# 				# 		if tmm.name != tm.name:
# 				# 			for possible_group in tmm.getPossible():
# 				# 				if group.name == possible_group.name:
# 				# 					tmm.remove(group)
# 				# 					print("can't be in that group %s" % tmm.name)
# 				# elif len(tmp_groups) == 2:
# 				if len(tmp_groups)<=2:
# 					if len(tmp_groups) == 1:
# 						print("ONLY ONE POSSIBLE GROUP %s" % tmp_groups[0].name)
# 					else:
# 						print("Two Possible Groups", tmp_groups[0].name, tmp_groups[1].name)
# 					emergency_teams.append(tm)
# 					if len(emergency_groups) == 0:
# 						for emergency_group in tmp_groups:
# 							emergency_groups.append(emergency_group)
# 						print("added to emergency group %s" % tm.name)
# 					else:
# 						for emergency_group in tmp_groups:
# 							if emergency_group not in emergency_groups:
# 								break
# 							else:
# 								print("emergency group same as %s" % tm.name)
# 								for tmm in tmp_pot:
# 									for emergency_tmm in emergency_teams:
# 										print("EMERGENCY %s" % emergency_tmm.name)
# 										if tmm.name != emergency_tmm.name and emergency_group in tmm.getPossible():
# 											print("SAME EMERGENCY GROUPS!")
# 											# tmm.remove(emergency_group)


# 				for group in tmp_groups:
# 					tm.possible(group)

# 				for gr in tm.getPossible():
# 					print("IT IS POSSIBLE for %s" % gr.name)



						
# 			# pick random team
# 			tmp_team = random.choice(tmp_pot)
# 			print('Drawing %s' % tmp_team.name)
# 			# get possible groups
# 			tmp_possible_groups = tmp_team.getPossible()

# 			print('Choices are')
# 			for group in tmp_possible_groups:
# 				print(group.name)	
# 			# pick random group
# 			if len(tmp_possible_groups) == 1:
# 				tmp_group = tmp_possible_groups[0]
# 			else:
# 				tmp_group = random.choice(tmp_possible_groups)
# 			tmp_group.addteam(tmp_team)
# 			print('Added to Group %s' % tmp_group)
			
# 			tmp_pot.remove(tmp_team)
# 			tmp_groups = groups[:]
# 			n = n-1

# 	print '\n' + '-' * 36 + '\nDraw Complete\n' + '-' * 36 + '\n'
# 	printgroups(groups)

def draw(pots, groups):
	# 4 pots, 8 groups
	
	# create a list of all nationalities, used as index for the next list
	nations = []
	for pot in pots:
		for team in pot:
			if team.nation not in nations:
				nations.append(team.nation)
   

	# create a list of teams which countries have more than one team in top 2 pot
	nations_team = []
	multi_nations_team = []
	for nation in nations:
		tmp_list = []
		tmp_list2 = []
		for pot in pots:
			for team in pot:
				if team.nation == nation:
					tmp_list.append(team)
					if team.pot <= 2:
						tmp_list2.append(team)
		nations_team.append(tmp_list)
		if len(tmp_list2) > 1:
			multi_nations_team.append(tmp_list2)
			for team in tmp_list2:
				team.mn()
	
#	for team in nation:
#		for nation in multi_nations_team:
#			team.mn()

	
	# set same country avoidance (top/bottom half)
	for nation in nations_team:
		k = 0
		for team in nation:
			while (k+1 < len(nation)):
				if k % 2 == 0:
					nation[k].avoid(nation[k+1])
					nation[k+1].avoid(nation[k])
				k = k + 1
	
	# creat top half group and bottom half group sets			 
	tophalf = []
	bothalf = []
	for group in groups:
		if group.half == 1:
			tophalf.append(group)
		else: 
			bothalf.append(group)
			


	# reiteration - 4 pots
	i = 0
	while (i < 4):
		
		print 'Pot ' + str(i+1) + ':\n'
		
		# reiteration - 8 teams
		while (len(pots[i]) > 0):
			# before drawing team - calculating possible groups for all teams in pot
			
			# remove from teams from same country, conflict (Russia/Ukraine) already placed
			for team in pots[i]:
				for group in groups:
					for opposition in group.teams:
						if ((team.nation == opposition.nation)
							or (team.nation == 'RUS' and opposition.nation == 'UKR')
							or (team.nation == 'UKR' and opposition.nation == 'RUS')):
							team.remove(group)
#							print team.name + ' removed ' + group.name
							
			# 1st pot avoidance for same country (top/bottom half)
		   
				if i == 0:
					topplaced = []
					topnon = []
					botplaced = []
					botnon = []
					unplacedmn = []
					unplacednon = []
					for nation in nations_team:
						for mnteam in nation:
							if mnteam in nation and mnteam.placed and mnteam.pot == i:
								for group in tophalf:
									for team in group.teams:
										if mnteam == team:
											if mnteam.multi:
												topplaced.append(mnteam)
											else:
												topnon.append(mnteam)
								for group in bothalf:
									for team in group.teams:
										if mnteam == team:
											if mnteam.multi:
												botplaced.append(mnteam)
											else:
												botnon.append(mnteam)
							elif mnteam in nation and not mnteam.placed and mnteam.pot == i:
								if mnteam.multi:
									unplacedmn.append(mnteam)
								else:
									unplacednon.append(mnteam)
					if len(topplaced) == 3:
						for team in unplacedmn:
							for group in tophalf:
								team.remove(group)
								print team.name + 'must be in bot half'
					if len(botplaced) == 3:
						for team in unplacedmn:
							for group in bothalf:
								team.remove(group)
								print team.name + 'must be in top half'
					if len(topnon) == 2:
						for team in unplacednon:
							for group in tophalf:
								team.remove(group)
								print team.name + 'must be in bot half'
					if len(botnon) == 2:
						for team in unplacednon:
							for group in bothalf:
								team.remove(group)
								print team.name + 'must be in top half'
					if len(team.possiblegroups) == 1:
						print ('EMERGENCY! ' + team.name + ' has to be in group ' +
								team.possiblegroups[0].name)
						for others in pots [i]:
							if others != team:
								others.remove(team.possiblegroups[0])
				
			# avoiding yet to place same country group (top/bottom half) from same pot
			
				if team.avoiding != None:
					ctr = team.avoiding
					if ctr.placed == False and ctr.pot == i+1:
						print 'avoid issues'
						if team.toppos == []:
							for group in tophalf:
								team.avoiding.remove(group)
						elif team.botpos == []:
							for group in bothalf:
								team.avoiding.remove(group)
						elif len(team.toppos) == 1 or len(team.botpos) == 1:
							if len(team.toppos) == 1 and (ctr.toppos == [] or ctr.toppos == team.toppos):
								for others in pots[i]:
									if others != team and others != ctr:
										others.remove(team.toppos[0])
							elif len(team.botpos) == 1 and (ctr.botpos == [] or ctr.botpos == team.botpos):
								for others in pots[i]:
									if others != team and others != ctr:
										others.remove(team.botpos[0])
								
				
			# pre calculate - make sure all teams have at least one possible group
				if(team.marked == False):
					print 'checking ' + team.name
					halfkill = 0
					recheck = [team]
					fail = False
					n = 1
					while n < 8 and i != 0:
						k = 1
						halfkill = False
						fail = False
						if len(team.possiblegroups) == n:
							if n == 1:
								print ('EMERGENCY! ' + team.name + ' has to be in group ' +
									team.possiblegroups[0].name)
								for others in pots[i]:
									if others != team:
										others.remove(team.possiblegroups[0])
								break
							else: 
								for others in pots[i]:
									if others != team and others.placed == False:
										ctr = others.avoiding
										if others.posgroupissub(team.possiblegroups):
											recheck.append(others)
											print 'lol' + others.name
											printgroups(team.possiblegroups)
											printgroups(others.possiblegroups)
											k = k + 1
										elif ctr != None and ctr.placed == False and ctr.pot == i+1:
											if ((others.toppos == ctr.toppos and 
											others.posgroupissub(team.possiblegroups, 1)) 
											or (others.botpos == ctr.botpos
											and others.posgroupissub(team.possiblegroups, 2))):
												recheck.append(others)
												print 'halfkill '+ others.name
												halfkill = True
												k = k + 1
							if k < n:
								recheck = []
								fail = True
							elif k > 1 and k == n and halfkill != False:
								print team.name + ' k' + str(k) + 'n' + str(n)
								break
							elif k > n and halfkill:
								print 'halfkill'
								print team.name + ' k' + str(k) + 'n' + str(n)
								break
						n = n + 1

					print 'final k' + str(k) + 'n' + str(n) + ' halfkill' + str(halfkill) + ' len +' + str(len(recheck))
					if len(recheck) > 1:
						if (halfkill == True and k > n) or (halfkill == False and k == n):
							print 'recheck ' + team.name + ' len' + str(len(recheck))
							for tm in recheck:
								print tm.name
								tm.mark()
							printgroups(team.possiblegroups)
							for group in team.possiblegroups:
								for others in pots[i]:
									if others not in recheck and others != team:
										if group in others.possiblegroups:
											others.remove(group)
						
								
									
			# calculation complete

				
			# randomly choose a team from the pot
			tmp_team = random.choice(pots[i])
			print tmp_team.name
			
			print tmp_team.name + ' can be in group:'
			for group in tmp_team.possiblegroups:
				print group.name
					
			# randomly choose a group from the left over possible groups
			tmp_group = random.choice(tmp_team.possiblegroups)
			
			# add team to group
			tmp_group.addteam(tmp_team)
			print tmp_team.name + " added to group " + tmp_group.name
			tmp_team.place()
			
			# avoid same country team (top/bottom half)
			if tmp_team.avoiding != None:
				if tmp_group.half == 1:
					for group in tophalf:
						tmp_team.avoiding.remove(group)
				elif tmp_group.half == 2:
					for group in bothalf:
						tmp_team.avoiding.remove(group)
						
			# remove team from the pot
			pots[i].remove(tmp_team)
			
			# set this group unavailable for other teams in the same pot
			for teamm in pots[i]:
				teamm.remove(tmp_group)
				teamm.unmark()
				
		i = i + 1
		print ''
		printgroups(groups)
		
	# Drawing complete
	print '\n' + '-' * 36 + '\nDraw Complete\n' + '-' * 36 + '\n'
	printgroups(groups)

def printgroups(groups):
	for group in groups:
		print group
	print ''
		
		
def main():
	pot_1 = []
	pot_2 = []
	pot_3 = []
	pot_4 = []
	pots = [pot_1, pot_2, pot_3, pot_4]

	# nations = {}

	with open('2018.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			if row[3] == "1":
				pot_1.append(team(row[0], row[1], row[2], row[3]))
			if row[3] == "2":
				pot_2.append(team(row[0], row[1], row[2], row[3]))
			if row[3] == "3":
				pot_3.append(team(row[0], row[1], row[2], row[3]))
			if row[3] == "4":
				pot_4.append(team(row[0], row[1], row[2], row[3]))
			# if row[2] not in nations:
			# 	nations[row[2]] = [team(row[0], row[1], row[2], row[3])]
			# else:
			# 	nations[row[2]].append(team(row[0], row[1], row[2], row[3]))

	
	groups = [group('A'), group('B'), group('C'), group('D'), group('E'), group('F'), group('G'), group('H')]

	# test(pots, groups, nations)

	for pot in pots:
		for tm in pot:
			for gr in groups:
				tm.possible(gr)

	draw(pots, groups)

if __name__ == '__main__':
	main()
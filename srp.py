#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
	An implementation of the Irving Algorithm for the Stable roommates problem by:
	Vincent LIU - MAIN - Polytech Sorbonne 2017/18

	Comments are in French.
"""

from etape1 import etape1
from etape2 import etape2
from etape3 import etape3
from interface import msgStage
from easygui import msgbox

def srp(pref,argPref):
	"""
		Solve the Stable rommates problem.
	"""

	###################
	##### Etape 1 #####
	###################

	offer = etape1(pref,argPref)

	msgStage(pref, "Preference list of the participants by descending order of preference.")	
	msgStage(offer, "Phase 1: Best Offer after the stage 1 for each participant.")

	# Test 1: pour savoir si tout le monde a recu une offre ou non
	test1 = True
	for e in offer:
		if offer[e] == None:
			test1 = False
			break

	if test1 == True:

		###################
		##### Etape 2 #####
		###################
		
		# Test 2: savoir si
		stable_solution = 0 # On affiche les solutions stables
		stage3 = 1 # On passe à l'étape 3
		no_stable_solution = 2 # Il n'y a pas de solution stable
				
		prefReduit = etape2(pref,argPref,offer)

		msgStage(prefReduit,"Everyone got an offer, then go to Phase 2")
	
		test2 = stable_solution 

		for e in prefReduit:

			if len(prefReduit[e]) > 1:

				###################
				##### Etape 3 #####
				###################

				test2 = stage3 
				break

			if len(prefReduit[e]) == 0:
				test2 = no_stable_solution
				break

		if test2 == stable_solution:

			msgStage(prefReduit, "Phase 2: this matching is stable.")

		elif test2 == stage3:

			prefReduit = etape3(prefReduit)

			if prefReduit != None:
				msgStage(prefReduit,"Phase 3: this matching is stable.")

		elif test2 == 2:

			msgbox("There is no stable solution for this problem.","Stable Roommates Problem","OK :(")
		
	else:
		msgbox("There is no solution stable.","Stable Roommates Problem","OK :(")


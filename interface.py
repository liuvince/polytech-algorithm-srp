#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
	An implementation of the Irving Algorithm for the Stable roommates problem by:
	Vincent LIU - MAIN - Polytech Sorbonne 2017/18

	Comments are in French.
"""

from easygui import msgbox, integerbox, multenterbox, codebox
from random import seed, randint, shuffle	

def msgIntro():
	"""
		Genere les messages d'introduction
	"""

	title = "Stable Roommates Problem"

	# Premier Message
	start_msg = "This is a demo of the Irving Algorithm for the Stable roommates problem.\n"
	start_msg += "It was written by: Vincent LIU - MAIN - Polytech Sorbonne 2017/18.\n\n"
	start_msg += "Code is written in Python with the easygui library."

	msgbox(start_msg, title, "Start")

	# Deuxieme Message
	min_val = 4
	max_val = 18
	n = integerbox("Please enter the number of participants [{} .. {}]".format(min_val, max_val), title, 6, min_val, max_val)

	# Troisieme Message
	fieldNames = ["Name {}".format(i) for i in range(1, n+1)]
	playerNames = multenterbox("Please enter their names:", title, fieldNames)

	# make sure that none of the fields was left blank and not duplicate
	while 1:
    		if playerNames == None: 
			break
    		errmsg1 = ""
    		errmsg2 = ""	
    		for i in range(len(fieldNames)):

      			if playerNames[i].strip() == "":
        			errmsg1 = errmsg1 + ('"%s" is a required field.\n\n' % fieldNames[i])
			else:
				if playerNames.count(playerNames[i]) > 1 and errmsg2 == "":
					errmsg2 = errmsg2 + ("Pas de doublon.\n\n")

		errmsg = errmsg1 + errmsg2

    		if errmsg == "": 
			break

    		playerNames = multenterbox(errmsg, title, fieldNames, playerNames)

	return playerNames

def msgStage(D, msg):
	"""
		Genere un msg associé à un dictionnaire des preferences dans un codebox
	"""

	text = ""
	L = sorted(D.keys())

	# Parcours les élements du dictionnaire
	for i in L:
		# La clée
		text += i + "\n"
		# Les valeurs
		if D[i] is None:
			text += "None\n\n"
		else:
			for j in range(len(D[i])-1):
				text += D[i][j] + " - "
			text += D[i][-1]
			text += "\n\n"

	# On affiche tout
	codebox(msg , "Stable Roommates Problem", text)
	return None

def msgStage2(offer, msg):
	"""
		Genere un msg associé aux offres dans un codebox
	"""

	text = ""
	L = offer

	# Parcours les élements du dictionnaire
	for i in L:
		# La clée
		text += i + "\n"
		# Les valeurs
		if offer[i] is None:
			text += "None\n\n"
		else:
			text += offer[i] + "\n\n"

	# On affiche tout
	codebox(msg , "Stable Roommates Problem", text)
	return None


def randomOrder(L):
	"""
		Melange les listes de preference
	"""

	pref = dict()
	listlen = len(L)

	# Utilisation de la bibliothéque rand
	for i in L:
		pref[i] = []
		template = L[:]
		template.remove(i)
		for j in range(listlen-1):
			n = randint(0,listlen-j-2)
			pref[i].append(template.pop(n))

	return pref

def genereteArgPref(pref):
	"""
		Genere les listes de preference inverse (pour le rang de preference)
	"""

	argPref = dict((name,dict()) for name in pref.keys())

	for i in pref.keys():
		for j in range(len(pref[i])):
			argPref[i][pref[i][j]] = j

	return argPref
	



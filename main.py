#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
	An implementation of the Irving Algorithm for the Stable roommates problem by:
	Vincent LIU - MAIN - Polytech Sorbonne 2017/18

	Comments are in French.
"""

from interface import msgIntro, msgStage, randomOrder, genereteArgPref
from etape1 import etape1
from etape2 import etape2
from etape3 import etape3
from srp import srp

def main():

	# Exemple aléatoire

	playerNames = msgIntro()

	if playerNames is None:
		return

	pref = randomOrder(playerNames)

	argPref = genereteArgPref(pref)
	srp(pref, argPref)


def unit_test():

	# Exemple du PDF
	pref = dict()
	pref['A'] = ['B','C','F','E','D']
	pref['B'] = ['F','D','A','C','E']
	pref['C'] = ['F','E','B','A','D']
	pref['D'] = ['A','C','E','B','F']
	pref['E'] = ['B','A','D','C','F']
	pref['F'] = ['A','B','D','E','C']
	argPref = genereteArgPref(pref)
	offer = etape1(pref,argPref)
	print("Liste de depart:")
	print(pref)
	print("Etape 1:")
	print(offer)
	prefReduit = etape2(pref,argPref,offer)
	print("Etape 2:")
	print(prefReduit)
	prefReduit = etape3(prefReduit)
	print("Etape 3:")
	print(prefReduit)

# Execution
main()

#unit_test()


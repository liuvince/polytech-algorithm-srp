#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
	An implementation of the Irving Algorithm for the Stable roommates problem by:
	Vincent LIU - MAIN - Polytech Sorbonne 2017/18

	Comments are in French.
"""


def etape2(pref, argPref, offer):
	"""

		Effectue l'étape 2 de l'algorithme de Irving pour le problème des colocataires.

		
		:param pref: Les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères
Les valeurs sont les listes de préférences du colocataire, donc une liste des chaînes de caractères
		:param argPref: Les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères.
Les valeurs sont également des tableaux de hachage, où on accède au numéro de préférence de la clé.
		:param offer: Les clés correspondent aux noms des colocataires qui a reçu l'offre.
Les valeurs sont les noms des personnes qui ont fait l'offre.

		:type pref: dict()
		:type argPref: dict()
		:type offer: dict()


		:return: Les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères
Les valeurs sont les listes de préférences réduites du colocataire, donc une liste des chaînes de caractères

		:rtype: dict()
	
	"""

	# Copie de la table de preference
	prefReduit = pref.copy()

	i = 0

	for x in offer:

		while i < (len(pref[x])):

			# Condition de suppresion symétrique

			if argPref[x][pref[x][i]] > argPref[x][offer[x]]:

					# Suppression 1
					if x in pref[pref[x][i]]:
						prefReduit[pref[x][i]].remove(x)

					# Suppression 2
					prefReduit[x].remove(pref[x][i])
					i = i - 1
			
			i = i + 1
		i = 0

	return prefReduit



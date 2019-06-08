#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
	An implementation of the Irving Algorithm for the Stable roommates problem by:
	Vincent LIU - MAIN - Polytech Sorbonne 2017/18

	Comments are in French.
"""



def accept(new_pretender, nextchoice, argPref, offer):
	"""

		Retourne la reponse de l'individu 'nextchoice' pour l'offre de 'new_pretender'.


		:return: Retourne la réponse de l'individu par rapport à l'offre proposée par 'new_pretender'.
		On retourne également la personne qui va faire la prochaine proposition.

		:rtype: tuple (bool, str)

	"""

	## 'new_pretender' fait une proposition à 'nextchoice'

	# On va donc regarder les offres actuelles de 'nextchoice'
	current_pretender = offer[nextchoice] 

	## Qui est 'current_pretender', le prétendant actuel ?

	# Si 'nextchoice' n'a pas encore eu d'offre, alors 'current_pretender' n'existe pas
	# OU si 'current_predender' existe,
	# Si nextchoice prefere 'new_pretender' plutot que 'current_pretender'
	if current_pretender == None or argPref[nextchoice][new_pretender] < argPref[nextchoice][current_pretender] :

		## la reponse est positif
		res = True

		# 'nextchoice' accepte l'offre de 'new_pretender'
		offer[nextchoice] = new_pretender

		# 'nextchoice' rejette le prétendant actuel
		# La personne va faire la prochaine proposition
		reject = current_pretender

	# Sinon 
	else:
		## la reponse est negatif
		# l'offre de 'new_pretender' a échoué
		res = False
		
		# 'new_pretender' a donc échoué
		reject = new_pretender 
	
	return (res, reject)


def etape1(pref, argPref):
	"""	

		Effectue l'étape 1 de l'algorithme de Irving pour le problème des colocataires.

		
		:param pref: Les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères
Les valeurs sont les listes de préférences du colocataire, donc une liste des chaînes de caractères
		:param argPref: Les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères.
Les valeurs sont également des tableaux de hachage, où on accède au numéro de préférence de la clé.

		:type pref: dict()
		:type argPref: dict()


		:return: Les clés correspondent aux noms des colocataires qui a reçu l'offre.
Les valeurs sont les noms des personnes qui ont fait l'offre.

		:rtype: dict()

	"""

	# Liste des individus
	listRoommates = pref.keys()

	# Nb d'invididus
	nbRoommates = len(listRoommates)

	# On initialise les offres 'offer'
	offer = dict( (name, None) for name in listRoommates)

	# Cursor: dictionnaire qui indique le curseur sur la position du choix suivant
	cursor = dict( (name, 0) for name in listRoommates)

	## Boucle externe: Parcours de la liste des personnes
	for roommate in listRoommates:
		new_pretender = roommate

		## Boucle interne
		# Condition d'arrêt: Un des membres a vu toutes ses offres refusées
		while cursor[new_pretender] < nbRoommates-1:


			# new_pretender va faire une proposition à 'nextchoice'
			# 'nextchoice' étant la personne que désire new_pretender le plus actuellement
			nextchoice = pref[new_pretender][cursor[new_pretender]]

			cursor[new_pretender] += 1
			(res, reject) = accept(new_pretender, nextchoice, argPref, offer)

			#  Condition d'arrêt: A la boucle i, il doit avoir i individus avec une offre
			if reject == None:
				break
			else:
				new_pretender = reject

	return offer



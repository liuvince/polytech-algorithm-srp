#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
	An implementation of the Irving Algorithm for the Stable roommates problem by:
	Vincent LIU - MAIN - Polytech Sorbonne 2017/18

	Comments are in French.
"""

def cycle(pref):
	"""
		Identifie un cycle


		:param pref: Les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères
Les valeurs sont les listes de préférences du colocataire, donc une liste des chaînes de caractères.

		:type pref: dict()


		:return reject: On retourne une liste de tuple, qui correspond aux cycles.
		Ce sont les personnes que l'on va rejeter.

		:rtype: list()
	
		
	"""

	p1 = None

	# Chercher un début de cycle, trouver un p_1 qui convient
	for e in pref:
		if len(pref[e])>1:
			p1 = e
			break

	# Pas de cycle
	if p1 is None:
		return None

	p11 = []
	p11.append(p1)

	p = []
	q = []

	while p1 not in p:

	# q est la deuxieme personne prefere de p_1, donc indice 1
		q.append(pref[p1][1])
		p.append(p1)

	# le nouveau p_i est la personne la moins désirée de q_i donc indice -1
		p1 = pref[q[-1]][-1]
		if len(pref[p1]) <= 1:
			p = []
			q = []
			p1 = None
			for e in pref:
				if len(pref[e]) > 1 and e not in p11:
					p1 = e
					p11.append(p1)
					break
			# Pas de cycle
			if p1 is None:
				return None
			
	# les q{i} et les p_{i+1} vont se rejeter, on les stock dans une liste de tuple
	c = []
	for i in range(len(p)-1):
		c.append((p[i+1], q[i]))
	c.append((p[0],q[len(q)-1]))

	return c

def etape3(prefReduit):
	"""	
		Effectue l'étape 3 de l'algorithme de Irving pour le problème des colocataires.
		

		:param prefReduit: les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères
Les valeurs sont les listes de préférences réduites du colocataire, donc une liste des chaînes de caractères

		:type prefReduit: dict()


		:return: Les clés correspondent aux noms des colocataires, donc ce sont des chaînes de caractères
Les valeurs sont les listes de préférences réduites du colocataire, donc une liste des chaînes de caractères

		:rtype: dict()
	"""

	# On va chercher un cycle initial
	c = cycle(prefReduit)

	if c == None:
		return None

	# Tant qu'il existe un cycle
	while c != None:

		# Rejet symétrique des (q_{i+1}, pi)
		reject(prefReduit, c)
		test = False

		# Rejet symétrique
		for e in prefReduit:
			if len(prefReduit[e]) > 1:
				test = True
				break
			if len(prefReduit[e]) == 0:
				print("Pas de solution stable")
				return None
		if test == False:
			break

		# On cherche un nouveau cycle pour l'iteration suivante
		c = cycle(prefReduit)	

	return prefReduit

def reject(prefReduit, c):
	""" 
		Rejet des pi, qi dans l'etape 3 
	"""

	## On rejette symetriquement les (p_i, q_i):
	# Lorsqu'on rejette a dans la liste de preference de b,
	# on rejette egalement b dans la liste de preference de a.
	for (a,b) in c:
		if a in prefReduit[b]:
			prefReduit[b].remove(a)
		if b in prefReduit[a]:
			prefReduit[a].remove(b)



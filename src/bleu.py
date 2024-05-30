#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:23:57 2024

@author: guilhem
"""

#__________MODULES

import sys
import sacrebleu

#__________MAIN

path_ref = sys.argv[1]  # Chemin vers le fichier de référence
path_trad = sys.argv[2]  # Chemin vers le fichier issu de la traduction OPENNMT

# Lire les fichiers
with open(path_ref, 'r', encoding='utf-8') as ref:
    references = [ref.read().strip().split('\n')]

with open(path_trad, 'r', encoding='utf-8') as trad:
    traduction = trad.read().strip().split('\n')

# Calculer le score BLEU
bleu = sacrebleu.corpus_bleu(traduction, references)
print(bleu.score)
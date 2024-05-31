# Projet-traduction-neuronale

## Description

Dépôt Git pour le projet de groupe du cours de 
Traduction Automatique et Assistée. 

Ce projet correspond à une analyse et une évaluation à grande échelle du moteur de traduction neuronale OpenNMT.

## Compte Rendu

Pour lire le compte rendu intégral réalisé par l'équipe, rendez-vous dans le dossier `./doc`.

## Table des matières

- [Projet-traduction-neuronale](#projet-traduction-neuronale)
  - [Description](#description)
  - [Compte Rendu](#compte-rendu)
  - [Table des matières](#table-des-matières)
  - [Installation](#installation)
  - [Utilisation](#utilisation)

## Installation

Ce programme est prévu pour fonctionner sous Linux avec `Python 3.9` et `PyTorch 1.6.0`.
Téléchargez les prérequis :

```bash
$ conda install pytorch torchvision -c pytorch
$ tpip3 install --upgrade gensim
$ pip3 install numpy
$ pip3 install OpenNMT-py
$ pip install scikit-learn
$ pip install nltk
```

## Utilisation

Pour utiliser ce programme, il convient d'exécuter les Notebooks contenus dans le dossier `./src` 

**1.** Commencez par exécuter `1-crea_corpus_emea.ipynb` afin de créer le 2eme corpus *(le premier corpus est déjà sur le dépôt)*

**2.** Exécutez `2-preparation_corpus.ipynb` afin de tokeniser, normaliser et réduire le corpus

**3.** Exécutez `3-lemmatize.ipynb` pour lemmatiser le corpus

**4.** Exécutez `4-run1.ipynb` pour tester la configuration 1

**5.** Exécutez `5-run2.ipynb` pour tester la configuration 2

**6.** Exécutez `6-run3.ipynb` pour tester la configuration 3

**7.** Exécutez `7-run4.ipynb` pour tester la configuration 4

**8.** Exécutez `8-bleu.ipynb` pour calculer les scores  des 4 configurations



--------

Projet traduction neuronale. 

G. SCHLOSSER & L. BESSAC | M1 PluriTAL | 2023-2024.
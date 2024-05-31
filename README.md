# Projet-traduction-neuronale

## Description

Dépôt Git pour le projet de groupe du cours de Traduction Automatique et Assistée. Projet traduction neuronale. 2023-2024.

Ce projet correspond à une analyse et une évaluation à grande échelle du moteur de traduction neuronale OpenNMT.

## Compte Rendu

Pour lire le compte rendu intégral réalisé par l'équipe, rendez-vous dans le dossier doc.

## Table des matières

- [Projet-traduction-neuronale](#projet-traduction-neuronale)
  - [Description](#description)
  - [Compte Rendu](#compte-rendu)
  - [Table des matières](#table-des-matières)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
    - [Arguments positionnels :](#arguments-positionnels-)
    - [Arguments facultatifs :](#arguments-facultatifs-)
  - [Exemple](#exemple)
  - [Boîte à outils](#boîte-à-outils)


## Installation

Ce programme est prévu pour fonctionner sous Linux avec `Python 3.9` et `PyTorch 1.6.0`.
Téléchargez les prérequis et entrainez le modèle :

```bash
$ wget https://s3.amazonaws.com/opennmt-trainingdata/toy-ende.tar.gz
$ tar xf toy-ende.tar.gz
$ cd toy-ende
$ onmt_build_vocab -config toy_en_de.yaml -n_sample 10000
$ onmt_train -config toy_en_de.yaml
```

## Utilisation

Pour utiliser ce programme, exécutez `XXX.py` avec les arguments suivants :

```bash
$ python main.py [-p {yes,no}] [-l {yes,no}] [-v {count,tfidf,hash}] [-m {svc,multi,dtree,rforest}] file
```

### Arguments positionnels :

`file` : Chemin vers le fichier qui contient le corpus au format JSON.

### Arguments facultatifs :

`-h`, `--help` : Affiche le message d'aide et quitte le programme.

`-p` `{yes,no}`, `--preprocess` `{yes,no}` : Supprime les stopwords de l'analyse.

`-l` `{yes,no}`, `--lemmatize` `{yes,no}` : Lemmatise le texte.

`-v` `{count,tfidf,hash}`, `--vectorize` `{count,tfidf,hash}` : Choisissez le vectorizer :
        'count' pour CountVectorizer
        'tfidf' pour TfidfVectorizer
        'hash' pour HashingVectorizer

`-m` `{svc,multi,dtree,rforest}`, `--model` `{svc,multi,dtree,rforest}` : Choisissez un modèle :
        'svc' pour LinearSVC
        'multi' pour MultinomialNB
        'dtree' pour DecisionTree
        'rforest' pour RandomForest

`-t`, `--table` : Retourne un graphe comparant la valeur de la precision de chaque modèle.


## Exemple

```bash
$ python main.py -p yes -l yes -v tfidf -m svc -t ../Data/data_enrichi.json
```

## Boîte à outils

Le script principal est accompagné d'une boîte à outils composée des scripts `scrapping.py`, `enrichissement_corpus.py`, `modif_ids_data.py`.

- `scrapping.py` : sert à scrapper le web pour créer un fichier corpus au format .json, 
- `enrichissement_corpus.py` : sert à ajouter des textes (stockés en .txt) au corpus (au format .json),
- `modif_ids_data.py` : sert a  réarranger les id en cas de suppression d'un item.


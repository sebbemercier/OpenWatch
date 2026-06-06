# OpenWatch

OpenWatch est un bot Discord en Python pour monitorer et centraliser des informations de services. Il expose des commandes slash simples comme `/about` et `/github`.

## Fonctionnalites

- Bot Discord en `discord.py`
- Commandes slash
- Chargement des commandes depuis `commands.py`
- Logs de connexion et de synchronisation au demarrage

## Prerequis

- Python 3.9 ou plus
- Un bot Discord cree dans le portail Discord Developer
- Un token de bot valide

## Installation

1. Cree un environnement virtuel si besoin.
2. Installe les dependances du projet.

Exemple :

```bash
python3 -m venv bot-env
source bot-env/bin/activate
pip install discord.py python-dotenv
```

## Configuration

Copie le fichier `.env.exemple` en `.env`, puis ajoute ton token :

```env
TOKEN=ton_token_ici
```

## Lancement

```bash
python3 bot.py
```

Au demarrage, le bot affiche des logs du type :

- `Connecte en tant que ...`
- `X commande(s) synchronisee(s)`

## Commandes disponibles

- `/about` : affiche une description du bot
- `/github` : affiche le lien du depot GitHub

## Structure du projet

```text
OpenWatch/
├── bot.py
├── commands.py
├── README.md
├── .env
├── .env.exemple
└── LICENSE
```

## Remarques

- Le fichier `.env` ne doit pas etre partage.
- Les commandes sont chargees dans `commands.py` via `setup(bot)`.

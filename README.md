 YetuBank Backend

Backend API de YetuBank — une plateforme fintech moderne développée avec Django REST Framework.

 Présentation

YetuBank Backend alimente les fonctionnalités principales de l’écosystème YetuBank, notamment :

- Authentification des utilisateurs
- Autorisation sécurisée avec JWT
- Gestion des comptes bancaires
- Transferts d’argent
- Historique des transactions
- Fonctionnalités d’épargne
- API financières

Ce projet est conçu avec une architecture propre, sécurisée et évolutive afin de simuler un véritable backend de fintech moderne.

---

 Stack Technique

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Git & GitHub

---

 Structure du Projet


yetubank-backend/
│
├── core/                 # Configuration principale Django
├── accounts/             # Gestion utilisateurs & authentification
├── transactions/         # Logique des transferts et transactions
├── manage.py
├── requirements.txt
└── .gitignore
Fonctionnalités
Authentification
Inscription utilisateur
Connexion utilisateur
JWT Access & Refresh Tokens
Routes protégées
Hashage sécurisé des mots de passe
Système Bancaire
Création de comptes
Gestion du solde
Simulation de transferts d’argent
Historique des transactions
Sécurité
Authentification JWT
Stockage sécurisé des mots de passe
Gestion des variables d’environnement
Installation
Cloner le projet
git clone https://github.com/votre-username/yetubank-backend.git
cd yetubank-backend
Créer un environnement virtuel
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
Installer les dépendances
pip install -r requirements.txt
Variables d’environnement

Créer un fichier .env à la racine du projet :

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=yetubank_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
Appliquer les migrations
python manage.py migrate
Lancer le serveur de développement
python manage.py runserver

Le serveur sera accessible sur :

http://127.0.0.1:8000/
Authentification API

Le projet utilise JWT Authentication.

Exemples d’endpoints :

/api/auth/register/
/api/auth/login/
/api/auth/refresh/
Workflow de Développement

Le projet suit un workflow GitHub professionnel :

Issues
Branches par fonctionnalité
Pull Requests
Commits propres et organisés

Exemples de branches :

feature/jwt-authentication
feature/money-transfer
feature/transaction-history

Convention de commits :

feat: add transfer endpoint
fix: resolve authentication issue
refactor: improve transaction service
Roadmap
 Authentification JWT
 API Profil Utilisateur
 Gestion des Comptes Bancaires
 Système de Transfert d’Argent
 Historique des Transactions
 Système d’Épargne
 Notifications
 Docker
 CI/CD Pipeline

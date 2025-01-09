# Plateforme d'analyse prédictive pour l'aide à la prise de décision dans les institutions financières

## Description
Cette application web permet d'effectuer des prédictions de données à partir d'entrées utilisateur. Elle permet de savoir si on peut accorder ou non un prêt à un client. Cette plateforme est en cours de développement. Vous pouvez apporter vos suggestions en les envoyant à l'adresse mail tout en bas du README.

## Fonctionnalités Principales
- **Page d'accueil** : Présentation générale de l'application.
- **Dashboard** : Visualisation des statistiques clés (nombre total de prédictions, prédictions positives, etc.).
- **Page de Prédiction** : Formulaire permettant de saisir des données et d'obtenir des prédictions en temps réel.
- **Design Réactif** : Utilisation de Tailwind CSS pour un rendu moderne et responsive.
- **Formulaire de Connexion Utilisateur** : Accès à l'application via un login pour les utilisateurs.

## Technologies Utilisées
- **Backend** : Flask (Python)
- **Frontend** : HTML5, Tailwind CSS, JavaScript
- **Gestion des Dépendances** : npm pour les fichiers CSS et JavaScript, et Python pour le backend.

## Prérequis
- Python 3.x
- Node.js et npm

## Installation
### 1. Cloner le projet
Clonez le dépôt GitHub sur votre machine locale :

```bash
git clone https://github.com/CodesVibes229/Prediction.git
```

### 2. Accéder au répertoire
Accédez au répertoire du backend :

```bash
cd backend
```

### 3. Créer un environnement virtuel
Créez un environnement virtuel Python pour le backend :

```bash
python -m venv venv
```

### 4. Activer l'environnement virtuel
- **Sur Windows** :
  ```bash
  venv\Scripts\activate
  ```
- **Sur Mac/Linux** :
  ```bash
  source venv/bin/activate
  ```

### 5. Installer les dépendances Python
Installez les dépendances backend nécessaires avec pip :

```bash
pip install -r requirements.txt
```

### 6. Installer les dépendances frontend avec npm
Accédez au répertoire `frontend` (si vous avez séparé les fichiers frontend et backend) et installez les dépendances npm, y compris Tailwind CSS :

```bash
cd frontend
npm install
```

Si vous n'avez pas encore installé Tailwind CSS dans votre projet, voici les étapes pour le faire (si vous ne l'avez pas déjà fait) :

1. **Initialiser npm dans le répertoire frontend** :
    ```bash
    npm init -y
    ```

2. **Installer Tailwind CSS, PostCSS et Autoprefixer** :
    ```bash
    npm install tailwindcss postcss autoprefixer
    ```

3. **Initialiser Tailwind CSS** :
    ```bash
    npx tailwindcss init
    ```

4. **Configurer le fichier `tailwind.config.js`** (exemple) :
    ```javascript
    module.exports = {
      content: [
        "./templates/**/*.html",  // Ajouter vos templates HTML ici
        "./static/js/**/*.js",
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    };
    ```

5. **Créer un fichier de configuration PostCSS `postcss.config.js`** (exemple) :
    ```javascript
    module.exports = {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    };
    ```

6. **Créer un fichier CSS pour inclure Tailwind (par exemple `static/css/styles.css`)** :
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

7. **Construire le fichier CSS avec Tailwind** :
    ```bash
    npm run build
    ```

Cela générera le fichier `tailwind.css` dans `static/css`.

### 7. Vérifier le fichier `.gitignore`
Assurez-vous d'ajouter les fichiers suivants à votre fichier `.gitignore` pour ne pas inclure les fichiers de configuration dans votre dépôt Git :

```
# Node.js
node_modules/
package-lock.json
package.json

# Tailwind CSS
tailwindcss.txt
tailwind.config.js
postcss.config.js
```

### 8. Configurations supplémentaires
- Si vous avez un fichier `.env` ou des configurations de variables d'environnement spécifiques à Flask, assurez-vous de les configurer en fonction de votre environnement.

## Exécution de l'Application
1. **Lancer l'application Flask** :
   Dans le répertoire `backend`, exécutez la commande suivante pour démarrer l'application Flask :

   ```bash
   python app.py
   ```

2. **Accéder à l'application** :
   Une fois l'application lancée, ouvrez votre navigateur et accédez à l'URL suivante :

   ```
   http://127.0.0.1:5000
   ```

## Informations supplémentaires
Ce projet a été développé dans le cadre d'un mémoire académique.

### Contact
Si vous avez des suggestions ou des questions concernant le projet, vous pouvez m'envoyer un email à [pascalaurel589@gmail.com].
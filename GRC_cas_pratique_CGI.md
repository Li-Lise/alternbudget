🔐 GRC — Cas Pratique CGI Bordeaux

Notion : Gestion des Accès Privilégiés (PAM)

Rapport FinOps : Coût de productivité — Jour 1



📚 1. La notion PAM expliquée simplement

PAM = Privileged Access Management

= Gestion des Accès Privilégiés

Pour un RH :

C'est la politique qui répond à 4 questions :



Qui a accès à quoi ?

Pourquoi cet accès est-il nécessaire ?

Pendant combien de temps ?

Qui surveille ce qui est fait avec cet accès ?



Pour un Administrateur Systèmes \& Réseaux junior :

C'est l'ensemble des règles techniques et organisationnelles qui encadrent

les comptes à hauts privilèges (admin, root, API) pour éviter les abus,

les fuites de données et les accès non autorisés.



🏗️ 2. Ce que j'ai mis en place aujourd'hui — Application PAM

Action 1 — Externalisation des secrets dans .env

Ce que j'ai fait :

Plutôt que d'écrire le mot de passe et l'URL du serveur 3CX directement

dans le code Python, je les ai stockés dans un fichier .env séparé,

exclu du versioning GitHub via .gitignore.

Principe PAM appliqué : Séparation des secrets

Pourquoi c'est important :

Si le mot de passe est dans le code et que le code est publié sur GitHub,

n'importe qui dans le monde peut lire le mot de passe et accéder au serveur 3CX.

Analogie RH :

C'est comme ne pas écrire le code du coffre-fort sur la porte du bureau.



Action 2 — Authentification OAuth Bearer (token temporaire)

Ce que j'ai fait :

Mon script Python envoie les identifiants à 3CX une seule fois

pour obtenir un token valable 60 secondes.

Après 60 secondes, le token expire automatiquement.

Principe PAM appliqué : Moindre durée d'exposition

Pourquoi c'est important :

Si quelqu'un intercepte le token pendant la communication,

il ne peut l'utiliser que pendant 60 secondes maximum.

Après, il est inutilisable.

Analogie RH :

C'est comme un badge visiteur qui se désactive automatiquement

après 1 heure — même si quelqu'un le vole, il devient inutile rapidement.

Lien avec l'expérience terrain :

Même principe que les tokens RSA SecurID utilisés pour les VPN

des collaborateurs itinérants en 2007-2008. La futur alternante a utilisé cette technologie en tant que technicien helpdesk niveau 1, pour IBM-Brno.

La technologie a évolué, mais la logique de sécurité est identique.



Action 3 — Traçabilité des actions (Logging)

Ce que j'ai mis en place :

pythonimport logging

from datetime import datetime



logging.basicConfig(

&nbsp;   filename="audit\_appels.log",

&nbsp;   level=logging.INFO,

&nbsp;   format="%(asctime)s - %(message)s"

)



def logger\_appel(recruteur, numero\_candidate):

&nbsp;   logging.info(f"Appel initie par {recruteur} vers {numero\_candidate}")

Principe PAM appliqué : Piste d'audit

Pourquoi c'est important :

Si un recruteur passe 200 appels frauduleux, le fichier log permet

d'identifier qui, quand, vers quel numéro. Sans log, impossible de prouver quoi que ce soit.

Analogie RH :

C'est le registre d'entrées et sorties d'un bâtiment sécurisé.



Action 4 — Principe du moindre privilège

Ce que j'ai identifié comme amélioration en production :

Mon script actuel utilise un seul compte pour tous les recruteurs.

En production chez CGI avec 300 recruteurs, chaque recruteur devrait

avoir son propre token nominatif, limité aux appels sortants uniquement.

Principe PAM appliqué : Moindre privilège

Règle simple :



Chaque utilisateur a exactement les droits dont il a besoin,

ni plus, ni moins.





💶 3. Rapport FinOps — Coût de productivité Jour 1

Hypothèses de calcul

Taux horaire junior alternante (base SMIC 2026) = 11,88 €/heure

Durée totale de travail aujourd'hui             = 4 heures

Coût horaire plateforme Claude (abonnement Pro) = 20 € / mois

&nbsp;                                              = 20 / 30 / 8 = 0,083 €/heure

Coût Python, Git, GitHub                        = 0 € (gratuit)

Coût 3CX SMB                                    = 0 € (gratuit)



Calcul du coût par action

Action 1 — Installation et configuration de l'environnement

Durée estimée        : 45 minutes = 0,75 heure

Coût main d'oeuvre   : 0,75 × 11,88 = 8,91 €

Coût outils          : 0 €

─────────────────────────────────────────────

Coût total Action 1  : 8,91 €

Ce qui a été produit :



Python 3.13 installé

Bibliothèques requests et python-dotenv installées

Dossier de travail alternbudget créé





Action 2 — Premier appel API REST (test\_api.py)

Durée estimée        : 20 minutes = 0,33 heure

Coût main d'oeuvre   : 0,33 × 11,88 = 3,92 €

Coût outils          : 0 €

─────────────────────────────────────────────

Coût total Action 2  : 3,92 €

Ce qui a été produit :



Compréhension du cycle requête/réponse HTTP

Lecture d'une réponse JSON

Gestion des codes de statut (200, 404, 500)





Action 3 — Sécurisation des secrets (auth\_securisee.py + .env + .gitignore)

Durée estimée        : 30 minutes = 0,50 heure

Coût main d'oeuvre   : 0,50 × 11,88 = 5,94 €

Coût outils          : 0 €

─────────────────────────────────────────────

Coût total Action 3  : 5,94 €

Risque financier évité :

Une clé API exposée sur GitHub peut générer une fraude téléphonique

estimée entre 5 000 € et 50 000 € pour une entreprise de 300 salariés.

Coût de la sécurisation    :      5,94 €

Risque financier évité     : 27 500,00 € (moyenne basse/haute)

─────────────────────────────────────────

ROI sécurité               : x 4 628



Pour 5,94 € investis, on protège potentiellement 27 500 € d'actifs.





Action 4 — Appel API authentifié (appel\_authentifie.py)

Durée estimée        : 25 minutes = 0,42 heure

Coût main d'oeuvre   : 0,42 × 11,88 = 4,99 €

Coût outils          : 0 €

─────────────────────────────────────────────

Coût total Action 4  : 4,99 €

Ce qui a été produit :



Requête HTTP avec headers d'authentification

Gestion des erreurs (Timeout, HTTPError)

Extraction de données JSON structurées





Action 5 — Connexion réelle à 3CX (connexion\_3cx.py)

Durée estimée        : 45 minutes = 0,75 heure

Coût main d'oeuvre   : 0,75 × 11,88 = 8,91 €

Coût outils          : 0 €

─────────────────────────────────────────────

Coût total Action 5  : 8,91 €

Ce qui a été produit :



Authentification OAuth Bearer sur API 3CX réelle

Token Bearer récupéré et validé

Base technique pour déclencher des appels VoIP





Action 6 — Versioning GitHub (Git init, commits, push, merge)

Durée estimée        : 45 minutes = 0,75 heure

Coût main d'oeuvre   : 0,75 × 11,88 = 8,91 €

Coût outils          : 0 €

─────────────────────────────────────────────

Coût total Action 6  : 8,91 €

Ce qui a été produit :



Dépôt GitHub public opérationnel

3 commits documentés

Résolution autonome d'un conflit Git (git pull + merge)

README professionnel publié





Tableau récapitulatif FinOps

ActionDuréeCoût MOCoût outilsTotalInstallation environnement45 min8,91 €0 €8,91 €Premier appel API REST20 min3,92 €0 €3,92 €Sécurisation secrets30 min5,94 €0 €5,94 €Appel API authentifié25 min4,99 €0 €4,99 €Connexion 3CX réelle45 min8,91 €0 €8,91 €Versioning GitHub45 min8,91 €0 €8,91 €TOTAL3h3041,58 €0 €41,58 €



Valeur produite vs coût investi

Coût total Jour 1                    :     41,58 €

Risque financier évité (fraude API)  : 27 500,00 €

Livrables GitHub publiés             :  4 fichiers + 1 README

Compétences documentées              :  API REST, OAuth, Git, PAM, FinOps



ROI global Jour 1 = 27 500 / 41,58 = x 661



Pour 41,58 € de temps investi, la valeur produite et le risque évité représentent plus de 660 fois le coût initial.





Lecture pour un RH



Cette future alternante a produit en une demi-journée un environnement de développement sécurisé, une connexion API fonctionnelle à un système

téléphonique d'entreprise, et une documentation GitHub professionnelle.

Le coût total est de 41,58 € pour un risque sécurité évité estimévà 27 500 €. 

Le rapport coût/valeur est exceptionnel pour un profil junior.





Lecture pour un Administrateur Systèmes \& Réseaux junior



Les 3 règles PAM appliquées aujourd'hui sont non négociables en production :



Jamais de secret dans le code → fichier .env + .gitignore

Token temporaire → OAuth Bearer 60 secondes

Tout logger → piste d'audit obligatoire en GRC



Ces 3 règles s'appliquent à n'importe quel service que tu administres :

VPN, Active Directory, API, serveur SSH, base de données.





📎 Références



ANSSI — Guide de gestion des comptes privilégiés

NIST SP 800-53 — Contrôle AC-6 (Least Privilege)

ISO 27001 — A.9.2 (Gestion des accès utilisateurs)

3CX API Documentation — OAuth 2.0 Bearer Token





Document rédigé dans le cadre du projet AlternBudget

Simulation professionnelle — Mission CGI Bordeaux

Auteure : Li-Lise — Bachelor Systèmes \& Réseaux, Cloud et Cybersécurité — Sup de Vinci 2026


# Rapport du projet de BD

## Énonciation du problème et des exigences

### Contexte
À la suite des délibérations de l’équipe, il a été décidé que l’application créée dans le cadre du projet de session du cours GLO-2005 de l’Université Laval est une application de prise de notes. Elle peut être utilisée pour la prise de notes ou la rédaction de tout autre texte simple. Les notes en soit sont des chaînes de caractères écrites et affichées en respectant le standard MarkDown (.md) afin d’offrir la possibilité aux usagers de réaliser un minimum de formatage. Le nom de l’application produite est Notepad+++, un clin d’œil au légendaire logiciel de traitement de code Notepad++.

### Utilisateurs cibles
Les utilisateurs cibles sont potentiellement toutes les personnes munies d’un ordinateur et d’un clavier, mais les utilisateurs clés («power users») qui utiliseront toutes les fonctionnalités offertes seront les gens possédant de bonnes connaissances en technologie, spécifiquement le langage MarkDown.

### Avantages de notre solution
L’application développée offre plusieurs avantages par rapport au bon vieux bloc note de Windows. D’abord, les notes peuvent être regroupées en carnets de notes afin de respecter une hiérarchie conviviale. De plus, il est possible de partager une note avec d’autres utilisateurs, qui pourront eux aussi modifier cette note. Finalement, un historique des versions précédentes des notes est conservé pour consultation, au besoin.


### Exigences
L’équipe a convenu des exigences suivantes : 
- Un utilisateur peut créer un compte à l’aide de son adresse courriel et d’un mot de passe
- Un utilisateur peut se connecter à son compte à l’aide de son adresse courriel et d’un mot de passe
- Un utilisateur peut créer un nouveau carnet de note et le nommer. Il peut renommer ce carnet de note à tout moment.Il peut supprimer ce carnet de note, ce qui aura pour effet de supprimer toutes les notes contenues dans ce carnet.
- Un utilisateur peut créer une nouvelle note et la nommer (ce nom sera immuable par la suite). Il peut supprimer cette note : s’il est le seul utilisateur à y avoir accès (cas 1), elle est supprimée définitivement ainsi que toutes les versions archivées de cette note; si d’autres utilisateurs ont accès à cette note (cas 2), il en perd simplement l’accès.
- Un utilisateur (1) peut partager une note avec n’importe quel utilisateur (2) (excepté lui-même). L’utilisateur 2 obtient l’accès à cette note dans un carnet spécial « notes partagées » ainsi qu’à toutes les versions archivées. Il peut désormais la modifier. Une modification effectuée par n’importe quel utilisateur ayant accès à cette note crée une nouvelle version de cette note qui est disponible à tous les utilisateurs y ayant accès.
- Un utilisateur peut consulter l’historique des versions d’une note auquel il a accès.

### Bases architecturales
Dans cette application, le niveau client sert principalement à afficher une interface graphique conviviale pour l’utilisateur et récupérer ses actions et saisies de données (« inputs »). Du traitement très simple, comme la vérification du format d’une entrée de données ou le hachage du mot de passe est aussi effectué. Le framework Vue est utilisé. Cinq pages sont nécessaires : la page de connexion, le profil utilisateur, la liste des notes, la page d’édition de notes et l’historique d’une note.

Le serveur d’application récupère les informations envoyées par le client, effectue des vérifications et envoie des requêtes à la base de données. Le serveur est réalisé avec la libraire Python Flask et consiste en un API JSON respectant la convention REST.

La base de données MySQL stocke toutes les informations nécessaires sur les utilisateurs et les notes.

## Modélisation des données
TODO

### Modèle entité-relation
TODO

### Modèle relationnel
TODO

## Création de la base de données

## Création des requêtes et des routines

## Indexation et optimisation du système

## Normalisation des relations

## Sécurité de la BD

## Implémentation de la logique d’affaire
TODO Ramy

## Implémentation de l’interface utilisateur
TODO Diamond 💎💎💎

## Tests du système

## Accessibilité du système

## Gestion de l’équipe et organisation du travail
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
Le modèle entité-relation de la base de données contient quatre ensembles d’entités et cinq ensembles de relations.

Des utilisateurs (**User**) possèdent chacun un nom, un mot de passe (la version stockée sera hachée), une bio (un court texte descriptif), un courriel et sont identifiés par un id, qui sert de clé primaire. 

Des carnets de notes (**Notebook**) sont composés d’un titre, d’une date de création et sont identifiés par un id, qui sert de clé primaire.

Un utilisateur possède (**Owns**) un nombre arbitraire de carnets de notes. Il peut en créer et en supprimer à sa guise. Cependant, un carnet de notes doit appartenir à un seul utilisateur.

Une note (**Note**) est identifiée par un id, sa clé primaire; ainsi que d’un titre. Une note ne possède pas de contenu en soit, celui-ci est enregistré en tant que version.

Un carnet de notes peut contenir (**Contains**) un nombre indéterminé de notes ou être vide. Une note peut flotter librement dans la collection d’un utilisateur, elle n’est pas nécessairement dans un carnet de notes. Une note peut être dans plus d’un carnet de notes.

Un utilisateur a accès (**Has access**) à un nombre indéterminé de notes. Une note doit obligatoirement être accessible à un ou plusieurs utilisateurs, sans quoi elle est supprimée car inutilisable. Il est à noter qu’une note peut encore exister malgré sa suppression par son créateur si elle avait préalablement été partagée à un autre utilisateur.

La version d’une note (**Version**) représente l’état du contenu textuel d’une note enregistré à un moment précis. Par défaut, le contenu d’une note est celui de sa plus récente version, mais il est possible en tout temps de récupérer d’anciennes versions. Une version est composée d’une date (date et heure précise, clé discriminante) et d’un contenu textuel. Puisqu’une version ne peut exister sans appartenir à une note (**Historique Note**), c’est un ensemble d’entité faible. Sa clé primaire est une concaténation de l’id de la note et de la date de la version. Il est à noter qu’une note possède au minimum une version, soit son état à sa création.

Une nouvelle version d’une note a été rédigée (**Edited**) par un utilisateur, qui peut être le créateur de la note ou tout autre utilisateur disposant de l’accès à la suite du partage de la note.


### Modèle relationnel
Le modèle relationnel est composé de six relations.
La relation **users** contient les informations sur les utilisateurs de l’application. Ils sont identifiés par un id unique (clé primaire). Cet id est un entier auto incrémental défini par MySQL.

La relation **notebooks** contient les informations sur les carnets de notes, identifiés par un id unique (clé primaire). Un carnet de notes peut être relié à son propriétaire grâce au champ owner_id.

La relation **notes** contient les informations sur les notes, identifiées par un id unique (clé primaire).

La relation **versions** contient les informations sur toutes les versions historiques des notes existantes. Le champ note_id permet de relier une note à ses versions. Le champ editor_id associe la version à l’utilisateur qui l’a éditée. Le champ content est probablement le plus important de la base de données : il s’agit du contenu d’une version précise d’une note. Ce champ utilise le type de données MySQL mediumtext, permettant de stocker des chaînes de caractères d’une taille allant jusqu’à 16 MB. 

La relation **notebook_contains** permet de savoir quelles notes sont à l’intérieur d’un carnet de notes.

La relation **user_has_access** permet de savoir quelles notes sont accessibles à un utilisateur précis.


## Création de la base de données
TODO Loïc🐬

## Création des requêtes et des routines
TODO Xavier + Ramy

## Indexation et optimisation du système
TODO Loïc🐬

## Normalisation des relations
🕉️🪦🗿🪬

## Sécurité de la BD
TODO Ramy

## Implémentation de la logique d’affaire
TODO Ramy

## Implémentation de l’interface utilisateur
TODO Diamond 💎💎💎

## Tests du système
TODO Loïc🐬

## Accessibilité du système
TODO Loïc🐬

## Gestion de l’équipe et organisation du travail
TODO Loïc🐬
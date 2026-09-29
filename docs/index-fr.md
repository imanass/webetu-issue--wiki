# WebEtu 2.5.0 : problèmes d'installation sur Android

## Symptômes

Lors de l'ouverture de l'application WebEtu 2.5.0 installée, l'un des messages suivants peut apparaître :

- message plein écran : "L'application installée n'est pas reconnue. Veuillez la télécharger depuis Google Play"
- dans le Play Store : "Non compatible avec votre appareil" lors de l'installation ou de la mise à jour
- lors du chargement d'un fichier XAPK depuis une source externe : le même message de non-reconnaissance apparaît

Ce message ne signifie pas forcément un défaut du matériel ou du ROM. Le problème vient souvent du filtre de compatibilité appliqué par Google Play, ainsi que de la vérification de l'origine de l'installation.

## Avertissement de sécurité

N'entrez pas les identifiants de votre université dans une application provenant d'une source non vérifiée.

Les fichiers téléchargés depuis des sources externes peuvent avoir été modifiés. L'auteur a utilisé APKure comme source de test. Il est recommandé de vérifier la source avant l'installation.

## Méthodes de dépannage

Choisissez la méthode adaptée à votre appareil :

- [Method 1 - Appareil rooté : contournement du gestionnaire d'installation](method-1-rooted-fr.md)
- [Method 2 - Sans root : App Manager via ADB sans fil](method-2-adb-wireless-fr.md)
- [Method 3 - Sans root : ordinateur avec ADB](method-3-pc-adb-fr.md)
- [Method 4 - Lien direct vers le Play Store](method-4-play-store-link-fr.md)
- [Method 5 - Lancement hors ligne](method-5-offline-launch-fr.md)
- [Method 6 - Alternative via le portail web](method-6-web-portal-fr.md)

## Limites connues

- Les résultats dépendent du modèle d'appareil, de la version Android et du ROM (stock ou personnalisé)
- Le comportement peut changer dans les futures mises à jour de WebEtu
- Ce wiki est maintenu par la communauté et n'est pas officiel

## Signaler un résultat

Si vous avez testé l'une de ces méthodes, veuillez ouvrir une issue sur GitHub avec les informations suivantes :

- modèle de l'appareil
- version Android
- type de ROM (stock ou personnalisé)
- appareil rooté ou non
- méthode utilisée
- version WebEtu
- source du fichier XAPK
- résultat
- capture d'écran si possible

Lien vers les issues :
https://github.com/imanass/webetu-issue--wiki/issues

## Langues

- [English](index.md)
- [Français](index-fr.md)
- [العربية](index-ar.md)

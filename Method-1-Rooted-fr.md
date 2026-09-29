Status: Tested

# Méthode 1 - Appareil rooté : usurpation de la source d'installation avec App Manager

## Configuration testée

- Appareil : Redmi Note 10 5G
- Android : 14
- ROM : ROM personnalisée
- App Manager : mode root
- Source du XAPK : APKure
- Application : WebEtu 2.5.0

## Étapes

1. Installez [App Manager](https://github.com/MuntashirAkon/AppManager) et accordez-lui l'accès root.
2. Dans App Manager, ouvrez Settings, puis la section Installer. Définissez Google Play Store (`com.android.vending`) comme source d'installation.
3. Ouvrez le fichier `.xapk` avec App Manager et installez-le.
4. Lancez WebEtu.

[SCREENSHOT: source d'installation Google Play Store sélectionnée dans App Manager]

## Résultat et limites

Sur l'appareil testé, WebEtu s'est lancé et la connexion a réussi. Il s'agit du résultat obtenu sur un seul appareil ; ne le généralisez pas à d'autres appareils ou ROM.

Play Integrity Fix n'était pas nécessaire. Il ne pouvait pas non plus être utilisé sur cette ROM sans reverrouiller le bootloader.
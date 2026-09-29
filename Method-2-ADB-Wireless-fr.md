Status: Under testing (not verified).

# Méthode 2 - Sans root : App Manager en mode ADB (débogage sans fil)

## Principe

Utiliser le même réglage de source d'installation que pour la méthode 1, mais faire fonctionner App Manager avec ADB via le débogage sans fil d'Android plutôt qu'avec root. Cette méthode n'a pas été vérifiée.

## Consignes pour les testeurs

- Le débogage sans fil nécessite une connexion Wi-Fi locale, pas un accès à Internet. Le point d'accès d'un téléphone suffit.
- Dans App Manager, définissez manuellement **Mode of operation** sur **ADB**, et non sur **Auto**. Sur un téléphone rooté, le mode Auto peut utiliser root sans le signaler, ce qui invalide le test.
- Activez le débogage sans fil dans les options pour les développeurs d'Android et connectez App Manager en mode ADB. Définissez ensuite Google Play Store (`com.android.vending`) comme source d'installation, ouvrez le `.xapk` dans App Manager, installez-le et testez le lancement de WebEtu.

[SCREENSHOT: mode de fonctionnement App Manager défini manuellement sur ADB]

## Résultat

Aucun résultat vérifié n'est disponible pour le moment. Indiquez l'appareil et le mode exact utilisés lorsque vous partagez un résultat.
Status: Under testing (not verified).

# Méthode 3 - Sans root : ordinateur avec ADB

## Étapes

1. Renommez le fichier `.xapk` en `.zip`, puis extrayez-le.
2. Activez le débogage USB sur l'appareil Android et connectez-le à un ordinateur où ADB est disponible.
3. Dans le dossier extrait, exécutez :

   ```sh
   adb install-multiple -i com.android.vending *.apk
   ```

4. Testez le lancement de WebEtu.

[SCREENSHOT: dossier extrait du XAPK et commande ADB install-multiple]

## Résultat

Cette méthode n'est pas vérifiée. Signalez le résultat de la commande et les détails de l'appareil ; ne déduisez pas la réussite de la seule commande.
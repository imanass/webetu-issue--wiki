Status: Tested

# Method 1 - Rooted device: App Manager installer spoof

## Tested setup

- Device: Redmi Note 10 5G
- Android: 14
- ROM: custom ROM
- App Manager: root mode
- XAPK source: APKure
- App: WebEtu 2.5.0

## Steps

1. Install [App Manager](https://github.com/MuntashirAkon/AppManager) and grant it root access.
2. In App Manager, open Settings, then the Installer section. Set the installer source to Google Play Store (`com.android.vending`).
3. Open the `.xapk` file with App Manager and install it.
4. Launch WebEtu.

[SCREENSHOT: App Manager installer source set to Google Play Store]

## Result and limits

On the tested device, WebEtu launched and logged in successfully. This is a single-device result and must not be generalized to other devices or ROMs.

Play Integrity Fix was not needed. It also could not be used on this ROM without relocking the bootloader.
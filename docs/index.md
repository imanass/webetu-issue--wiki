# WebEtu 2.5.0: installation problems on Android

## Symptoms

When opening the installed WebEtu 2.5.0 app, one of the following messages may appear:

- full-screen message: "The installed app is not recognized. Please get it from Google Play"
- in the Play Store: "Not compatible with your device" while installing or updating
- when loading a XAPK from an external source: the same recognition failure appears

This message does not necessarily mean a hardware or ROM problem. The issue is usually the compatibility filter used by Google Play, plus the app's verification of the installation source.

## Security warning

Do not enter your university credentials into an app from an unknown or unverified source.

Files downloaded from external sources may be modified. The author used APKure as the source for the test files. It is recommended to verify the source before installing.

## Fix methods

Choose the method that matches your device:

- [Method 1 - Rooted device: installer spoofing](method-1-rooted.md)
- [Method 2 - No root: App Manager over ADB wireless](method-2-adb-wireless.md)
- [Method 3 - No root: PC with ADB](method-3-pc-adb.md)
- [Method 4 - Play Store deep link](method-4-play-store-link.md)
- [Method 5 - Offline launch](method-5-offline-launch.md)
- [Method 6 - Web portal alternative](method-6-web-portal.md)

## Known limitations

- Results depend on device model, Android version, and ROM type (stock or custom)
- Behavior may change in later WebEtu updates
- This guide is community-maintained and is not official

## Reporting a result

If you test one of these methods, please open an Issue on GitHub with the following details:

- device model
- Android version
- ROM type (stock or custom)
- root yes/no
- method used
- WebEtu version
- XAPK source
- result
- screenshot if available

Issue page:
https://github.com/imanass/webetu-issue--wiki/issues

## Languages

- [English](index.md)
- [Français](index-fr.md)
- [العربية](index-ar.md)

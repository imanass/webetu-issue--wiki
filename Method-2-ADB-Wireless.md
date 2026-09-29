Status: Under testing (not verified).

# Method 2 - No root: App Manager in ADB mode (Wireless debugging)

## Idea

Use the same installer-source setting as Method 1, but have App Manager use ADB through Android Wireless debugging instead of root. This method has not been verified.

## Tester notes

- Wireless debugging requires a local Wi-Fi connection, not internet access. A phone hotspot is enough.
- In App Manager, manually set **Mode of operation** to **ADB**, not **Auto**. On a rooted phone, Auto may silently use root, making the test invalid.
- Enable Wireless debugging in Android Developer options and connect App Manager using its ADB mode. Then set the installer source to Google Play Store (`com.android.vending`), open the `.xapk` in App Manager, install, and test launching WebEtu.

[SCREENSHOT: App Manager Mode of operation set manually to ADB]

## Result

No verified result is available yet. Report the device and exact mode used when sharing a test result.
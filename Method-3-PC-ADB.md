Status: Under testing (not verified).

# Method 3 - No root: PC with ADB

## Steps

1. Rename the `.xapk` file to `.zip` and extract it.
2. Enable USB debugging on the Android device and connect it to a computer with ADB available.
3. In the extracted folder, run:

   ```sh
   adb install-multiple -i com.android.vending *.apk
   ```

4. Test launching WebEtu.

[SCREENSHOT: extracted XAPK folder and ADB install-multiple command]

## Result

This method is unverified. Report the command result and device details; do not assume success from the command alone.
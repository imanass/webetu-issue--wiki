Status: Under testing (not verified).

# الطريقة 3 - دون root: حاسوب مع ADB

## الخطوات

1. غيّر امتداد ملف `.xapk` إلى `.zip` ثم فك ضغطه.
2. فعّل تصحيح USB على جهاز Android وصِله بحاسوب يتوفر عليه ADB.
3. من المجلد الذي فُك ضغطه، نفّذ:

   ```sh
   adb install-multiple -i com.android.vending *.apk
   ```

4. اختبر تشغيل WebEtu.

[SCREENSHOT: مجلد XAPK بعد فك الضغط وأمر ADB install-multiple]

## النتيجة

لم يتم التحقق من هذه الطريقة. أبلغ عن نتيجة الأمر وتفاصيل الجهاز؛ ولا تعتبر تنفيذ الأمر وحده دليلًا على نجاح التثبيت.
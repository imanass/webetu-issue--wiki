Status: Tested

# الطريقة 1 - جهاز بصلاحيات root: تغيير مصدر التثبيت عبر App Manager

## بيئة الاختبار

- الجهاز: Redmi Note 10 5G
- Android: الإصدار 14
- ROM: مخصصة
- App Manager: وضع root
- مصدر XAPK: APKure
- التطبيق: WebEtu 2.5.0

## الخطوات

1. ثبّت [App Manager](https://github.com/MuntashirAkon/AppManager) وامنحه صلاحيات root.
2. في App Manager، افتح Settings ثم قسم Installer. اضبط مصدر التثبيت على Google Play Store (`com.android.vending`).
3. افتح ملف `.xapk` باستخدام App Manager وثبّته.
4. شغّل WebEtu.

[SCREENSHOT: مصدر التثبيت Google Play Store محدد في App Manager]

## النتيجة والقيود

على الجهاز الذي خضع للاختبار، اشتغل WebEtu وتم تسجيل الدخول بنجاح. هذه نتيجة لجهاز واحد فقط، ولا ينبغي تعميمها على أجهزة أو ROM أخرى.

لم تكن أداة Play Integrity Fix مطلوبة. كما تعذّر استخدامها على هذا الـ ROM دون إعادة قفل محمّل الإقلاع.
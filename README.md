# Instagram SSL pinning


![IG](./ig.png)

Bypassing Instagram SSL pinning `ARM and X86` and signing requests to instagram API

---

***Note**: First request may be displayed after a minute delay*

***Warning**: After using this patch anyone can intercept your requests*

---

#### Signing requests:

All requests to instagram API must be signed. Signing happens in `com.instagram.api.d.a.a` using the native method`com.instagram.strings.StringBridge.getSignatureString` from lib `resources/lib/x86/libstrings.so`. [Script](./request-body-signer.py) repeats the functionality of the native method and allows you to independently send requests to instagram API.

1. Install python3
2. Run python3 request-body-signer.py

---

#### Root Method:

1. Download Instagram APK from Apkmirror (*Versions must be equal**)
2. Choose your architecture and follow the instructions
3. Replace libliger.so file in **/data/data/com.instagram.android/lib/**

[ARM](https://github.com/pouyadarabi/Instagram_SSL_Pinning/tree/master/arm) | [X86](https://github.com/pouyadarabi/Instagram_SSL_Pinning/tree/master/x86)

---

#### Non-Root Method:

- Uninstall Instagram app from device

- Download and install modified apk suitable for your architecture


~ | File | Version
--- | --- | ---
ARM | [Download](./arm/com.instagram.android_35.0.0.20.96_minAPI16(arm).apk) | 35.0.0.20.96
X86 | [Download](./x86/com.instagram.android_35.0.0.20.96_minAPI16(x86).apk) | 35.0.0.20.96
Signer | [Download](./request-body-signer.py) | 1.0

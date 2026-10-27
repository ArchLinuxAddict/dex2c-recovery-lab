# Fixtures

All fixtures are self-created and MIT-licensed.

- `synthetic/Fixture.smali` — source for one class with `<init>()V`,
  `add(II)I`, and `answer()I`.
- `synthetic/Fixture.dex` — 592-byte DEX assembled from the smali source.
- `synthetic/AndroidManifest.xml` — minimal manifest for the synthetic APK.
- `synthetic/Fixture.apk` — 1,113-byte APK containing the DEX and manifest.
- `synthetic/metadata.json` — hashes, sizes, package, expected methods, and
  build commands.

No target application code, Android framework code, embedded payload, or
proprietary native library is included.

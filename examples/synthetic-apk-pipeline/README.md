# Synthetic APK static pipeline

## Purpose

Run the toolkit's full static pipeline on a self-created APK containing one DEX
with three methods and no native libraries.

## Fixture

`fixtures/synthetic/Fixture.apk` (self-created; manifest/DEX/source included).

## Command

```bash
python examples/synthetic-apk-pipeline/run.py --check
```

## Expected result

- Ingested package: `dev.dex2c.fixture`
- 1 DEX, 1 class, 3 methods, 0 native libraries
- DEX validation: valid 1, invalid 0
- Report and provenance files exist
- Exit code 0

## What it proves

The public toolkit can ingest, parse, analyze, report, and validate a safe
synthetic APK end-to-end.

## What it does not prove

It does not prove native/JNI recovery, behavioral equivalence, or behavior on a
Dex2C-protected application.

## Compatibility

Toolkit v1.0.0.

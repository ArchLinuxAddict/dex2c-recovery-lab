# Basic DEX analysis

## Purpose

Parse a known synthetic DEX with the toolkit and display its classes, methods,
and header checks.

## Fixture

`fixtures/synthetic/Fixture.dex` (self-created; source and SHA-256 in
`fixtures/synthetic/`).

## Command

```bash
python examples/basic-dex-analysis/run.py --check
```

## Expected result

- One class: `Ldex2c_recover/Fixture;`
- Methods: `<init>()V`, `add(II)I`, `answer()I`
- Header checksum/signature valid
- Exit code 0

## What it proves

The toolkit parses a valid DEX and reports its structure.

## What it does not prove

It does not prove DEX recovery, behavioral equivalence, or native mapping.

## Compatibility

Toolkit v1.0.0.

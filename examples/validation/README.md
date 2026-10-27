# Validation and malformed-input rejection

## Purpose

Validate the synthetic DEX and confirm that a tampered copy is rejected.

## Command

```bash
python examples/validation/run.py --check
```

## Expected result

- Original fixture: `valid: true`
- Tampered fixture: `valid: false` with checksum/signature or bounds errors
- Exit code 0 when both checks match

## What it proves

Structural validation detects a modified DEX fixture.

## What it does not prove

It does not prove semantic correctness or that every malformed input is caught.

## Compatibility

Toolkit v1.0.0.

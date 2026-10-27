# Walkthrough 1: first static analysis

## Prerequisite

An APK you own or are authorized to analyze. No APK is included in this lab.

## Install

```bash
python3 -m venv .venv
.venv/bin/pip install "git+https://github.com/ArchLinuxAddict/dex2c-recovery-toolkit.git@v1.0.0"
```

## Run

```bash
.venv/bin/dex2c-recover analyze \
  --apk /path/to/authorized.apk \
  --out output/analysis
```

## Inspect

1. `inventory/inputs.json` — input hash, DEX/native inventory, embedded artifacts.
2. `inventory/discovery-summary.json` — transformed/native/loader/ambiguous counts.
3. `native/method-mappings.jsonl` — method-to-function evidence and confidence.
4. `native/function-analysis.jsonl` — JNIEnv calls, instruction counts, CFG.
5. `recovery/exact/manifest.json` — supplied artifact candidates and validation.
6. `recovery/unresolved.jsonl` — methods without a defensible translation.
7. `reports/report.json` — consolidated summary.

## Validate

```bash
.venv/bin/dex2c-recover validate --apk /path/to/authorized.apk --out output/analysis
```

## What this proves

The toolkit parsed and structurally validated the artifacts it analyzed.

## What it does not prove

It does not prove behavioral equivalence, exact original recovery, or complete
method recovery. Read `research/findings/evidence-classes.md` before drawing
conclusions.

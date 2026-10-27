# Examples

These examples use the public toolkit's generic API and a self-created synthetic
DEX fixture. They do not use a target APK or proprietary code.

## Prerequisites

```bash
python3 -m venv .venv
.venv/bin/pip install "git+https://github.com/ArchLinuxAddict/dex2c-recovery-toolkit.git@v1.0.0"
```

For local development, install the toolkit from a checkout instead.

## Run

```bash
.venv/bin/python examples/basic-dex-analysis/run.py --check
.venv/bin/python examples/validation/run.py --check
.venv/bin/python examples/synthetic-apk-pipeline/run.py --check
```

Each example prints deterministic JSON and exits non-zero if the expected
result is not observed.

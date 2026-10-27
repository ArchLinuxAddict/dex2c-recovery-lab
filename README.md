# Dex2C Recovery Lab

Research, sanitized findings, reproducible examples, and tutorials for the
[Dex2C Recovery Toolkit](https://github.com/ArchLinuxAddict/dex2c-recovery-toolkit).

This repository is **not** a second toolkit. It contains methodology and
redistributable examples. The toolkit is the canonical implementation and
release source.

## Why this lab exists

Recovery research needs context that does not belong in a reusable tool
release: evidence-class definitions, campaign methodology, sanitized results,
tutorials, and small synthetic fixtures. Keeping them separate keeps the
toolkit focused and prevents target APKs, recovered third-party code, or
target-specific research drivers from leaking into the public implementation.

## What is here

- `research/` — methodology, sanitized findings, evidence classes, limitations,
  and Phase IV–VII notes.
- `results/sanitized/` — a machine-readable final-campaign summary and its
  verification trail.
- `examples/` — runnable examples using the toolkit's generic API and a
  self-created synthetic DEX fixture.
- `fixtures/synthetic/` — smali source, DEX fixture, and metadata/provenance.
- `tutorials/` — walkthroughs for static analysis and report interpretation.
- `compatibility/` — toolkit version mapping.

## Reference campaign findings

Verified against preserved research manifests:

- **103** behavioral reconstructions
- **8** partial reconstructions
- **225** native-analyzed methods remaining untranslated
- **0** exact recoveries
- **0** proven universal semantic equivalences
- **336** canonical candidates

The target APK and recovered DEX/code are not distributed. The full campaign is
not a one-command public reproduction; the public toolkit covers the generic
pipeline, and these are findings from a specific target/evidence set.

Tests: the recorded campaign result was 100 passed / 0 failed / 1 skipped. A
publication-environment rerun produced 99 passed / 0 failed / 2 skipped because
no authorized ADB device was attached. The difference is environmental, not a
failure.

See [`research/findings/campaign-summary.md`](research/findings/campaign-summary.md)
and [`results/sanitized/verification.md`](results/sanitized/verification.md).

## Run the examples

```bash
python3 -m venv .venv
.venv/bin/pip install "git+https://github.com/ArchLinuxAddict/dex2c-recovery-toolkit.git@v1.0.0"

.venv/bin/python examples/basic-dex-analysis/run.py --check
.venv/bin/python examples/validation/run.py --check
.venv/bin/python examples/synthetic-apk-pipeline/run.py --check
```

For toolkit development, install from a checkout with
`pip install -e /path/to/dex2c-recovery-toolkit`.

## Fixtures

The only binary fixture is a 592-byte DEX assembled from
[`fixtures/synthetic/Fixture.smali`](fixtures/synthetic/Fixture.smali). It is
self-created, contains no application code, and is MIT-licensed. Its SHA-256 and
expected methods are in `fixtures/synthetic/metadata.json`.

## Validation

```bash
python scripts/validate_lab.py
```

The CI workflow validates fixture metadata, sanitized counts, compatibility,
prohibited content, and both examples. It installs toolkit v1.0.0 from GitHub.

## What this lab does not claim

- No exact original bytecode recovery.
- No universal semantic equivalence.
- No complete recovery of all methods.
- No redistribution of the target APK, embedded payload, or recovered
  third-party code.
- No guarantee that the full research campaign drivers will be published.

See [`research/findings/limitations.md`](research/findings/limitations.md).

## Compatibility

Lab 1.0.0 targets toolkit v1.0.0. See
[`compatibility/toolkit-versions.md`](compatibility/toolkit-versions.md).

## License

MIT; see [LICENSE](LICENSE). The toolkit is separately licensed and maintained.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Do not
submit target APKs, proprietary DEX/native files, device data, or personal paths.

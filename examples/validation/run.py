#!/usr/bin/env python3
"""Validate the fixture and confirm a tampered copy is rejected."""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

from dex2c_recover.validation import validate_dex

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "fixtures" / "synthetic" / "Fixture.dex"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    original = validate_dex(FIXTURE, run_external=False)
    with tempfile.TemporaryDirectory() as tmp:
        tampered_path = Path(tmp) / "tampered.dex"
        data = bytearray(FIXTURE.read_bytes())
        data[120] ^= 0xFF
        tampered_path.write_bytes(data)
        tampered = validate_dex(tampered_path, run_external=False)
    result = {
        "original": {"valid": original["valid"], "errors": original["errors"]},
        "tampered": {"valid": tampered["valid"], "errors": tampered["errors"]},
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.check:
        return 0
    ok = original["valid"] is True and original["errors"] == [] and tampered["valid"] is False and bool(tampered["errors"])
    if not ok:
        print("example check failed", file=sys.stderr)
        return 1
    print("example check passed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

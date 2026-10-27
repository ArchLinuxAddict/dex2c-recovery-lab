#!/usr/bin/env python3
"""Parse the synthetic fixture with the public toolkit."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from dex2c_recover.dexparse import load_dex, parse_header
from dex2c_recover.validation import validate_dex

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "fixtures" / "synthetic" / "Fixture.dex"
EXPECTED_SHA256 = "b30683587f01623dd03865a77c7f4221250d57fe61b404482ac5ada5e4b397f6"


def collect() -> dict:
    data = FIXTURE.read_bytes()
    header = parse_header(data)
    dex = load_dex(data)
    classes = []
    for cls in sorted(dex.get_classes(), key=lambda c: c.get_name()):
        methods = [
            {"name": m.get_name(), "descriptor": m.get_descriptor(), "code": m.get_code() is not None}
            for m in sorted(cls.get_methods(), key=lambda m: (m.get_name(), m.get_descriptor()))
        ]
        classes.append({"name": cls.get_name(), "methods": methods})
    validation = validate_dex(FIXTURE, run_external=False)
    return {
        "fixture_sha256": hashlib.sha256(data).hexdigest(),
        "dex_version": header.version,
        "checksum_ok": header.checksum_ok,
        "signature_ok": header.signature_ok,
        "classes": classes,
        "validation_valid": validation["valid"],
        "validation_errors": validation["errors"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if the expected result is not observed")
    args = parser.parse_args()
    result = collect()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.check:
        return 0
    expected_methods = {("<init>", "()V"), ("add", "(I I)I"), ("answer", "()I")}
    observed_methods = {(m["name"], m["descriptor"]) for c in result["classes"] for m in c["methods"]}
    ok = (
        result["fixture_sha256"] == EXPECTED_SHA256
        and result["validation_valid"] is True
        and result["validation_errors"] == []
        and [c["name"] for c in result["classes"]] == ["Ldex2c_recover/Fixture;"]
        and observed_methods == expected_methods
    )
    if not ok:
        print("example check failed", file=sys.stderr)
        return 1
    print("example check passed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Run the public static pipeline on the synthetic APK fixture."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from pathlib import Path

from dex2c_recover.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "fixtures" / "synthetic" / "Fixture.apk"
EXPECTED_SHA256 = "e88e234c773d6384251062720210aa4e324c15d1ce99014d876525fbb08eff1e"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    before = hashlib.sha256(FIXTURE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "workspace with spaces"
        result = Pipeline(FIXTURE, out, ghidra="off", runtime="none").run_static(command="lab-example")
        stages = result["stages"]
        report = json.loads((out / "reports" / "report.json").read_text(encoding="utf-8"))
        observed = {
            "fixture_sha256": before,
            "package": stages["ingest"]["package"],
            "dex_files": stages["dex"]["dex_files"],
            "classes": stages["dex"]["classes"],
            "methods": stages["dex"]["methods"],
            "native_libraries": stages["native"]["libraries"],
            "dex_valid": report["validation"]["dex"]["valid"],
            "dex_invalid": report["validation"]["dex"]["invalid"],
            "report_exists": (out / "reports" / "report.json").exists(),
            "provenance_exists": (out / "provenance" / "SHA256SUMS").exists(),
        }
    after = hashlib.sha256(FIXTURE.read_bytes()).hexdigest()
    observed["input_unchanged"] = before == after
    print(json.dumps(observed, indent=2, sort_keys=True))
    if not args.check:
        return 0
    ok = (
        observed["fixture_sha256"] == EXPECTED_SHA256
        and observed["package"] == "dev.dex2c.fixture"
        and observed["dex_files"] == 1
        and observed["classes"] == 1
        and observed["methods"] == 3
        and observed["native_libraries"] == 0
        and observed["dex_valid"] == 1
        and observed["dex_invalid"] == 0
        and observed["report_exists"] is True
        and observed["provenance_exists"] is True
        and observed["input_unchanged"] is True
    )
    if not ok:
        print("example check failed", file=sys.stderr)
        return 1
    print("example check passed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate lab fixtures, sanitized results, links, and prohibited content."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "synthetic" / "Fixture.dex"
METADATA = ROOT / "fixtures" / "synthetic" / "metadata.json"
SUMMARY = ROOT / "results" / "sanitized" / "final-campaign-summary.json"
FORBIDDEN_SUFFIXES = {".apk", ".apks", ".xapk", ".odex", ".vdex", ".so", ".jar"}
ALLOWED_DEX = {"fixtures/synthetic/Fixture.dex"}
ALLOWED_APK = {"fixtures/synthetic/Fixture.apk"}
LOCAL_PATTERNS = [re.compile(r"/home/[A-Za-z0-9_.-]+/"), re.compile(r"/tmp/kilo/"), re.compile(r"\bRZ[0-9A-Z]{8,}\b")]


def check_links() -> list[str]:
    errors = []
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path = (md.parent / target.split("#", 1)[0]).resolve()
            if not path.exists():
                errors.append(f"broken relative link in {md.relative_to(ROOT)}: {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    if not FIXTURE.exists():
        return fail(["fixture missing"])
    data = FIXTURE.read_bytes()
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    if hashlib.sha256(data).hexdigest() != metadata["sha256"]:
        errors.append("fixture SHA-256 does not match metadata")
    if len(data) != metadata["size"]:
        errors.append("fixture size does not match metadata")
    apk = ROOT / "fixtures" / "synthetic" / "Fixture.apk"
    if not apk.exists():
        errors.append("APK fixture missing")
    elif hashlib.sha256(apk.read_bytes()).hexdigest() != metadata["apk_sha256"]:
        errors.append("APK fixture SHA-256 does not match metadata")
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    final = summary["final"]
    if final["behavioral_reconstructions"] + final["partial_reconstructions"] + final["native_analyzed_untranslated"] != final["canonical_total"]:
        errors.append("sanitized counts do not reconcile to canonical total")
    if final["exact_recoveries"] != 0 or final["semantic_equivalent_proven"] != 0:
        errors.append("unsupported exact/semantic claim")
    if summary["toolkit"]["compatibility"] != "1.0.0":
        errors.append("compatibility must target toolkit 1.0.0")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in FORBIDDEN_SUFFIXES and rel not in ALLOWED_DEX | ALLOWED_APK:
            errors.append(f"forbidden binary: {rel}")
        if path.name.lower() in {"protected.apk", "original.apk"}:
            errors.append(f"forbidden target artifact: {rel}")
        if rel.startswith("assets/"):
            errors.append(f"embedded asset path present: {rel}")
        if path.stat().st_size > 2 * 1024 * 1024:
            errors.append(f"oversized file: {rel}")
        if rel == "scripts/validate_lab.py":
            continue
        if path.suffix.lower() in {".py", ".md", ".json", ".yml", ".yaml", ".toml", ".txt"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in LOCAL_PATTERNS:
                if pattern.search(text):
                    errors.append(f"local path/device pattern in {rel}")
                    break
    errors.extend(check_links())
    if errors:
        return fail(errors)
    print(f"lab validation passed: {len(list(ROOT.rglob('*')))} paths")
    return 0


def fail(errors: list[str]) -> int:
    print("lab validation failed:")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

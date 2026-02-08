#!/usr/bin/env python
"""
Generate / verify SHA256 checksums for dataset package files.

Usage:
  python scripts/make_checksums.py
  python scripts/make_checksums.py --check
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKSUM_FILE = ROOT / "checksums.sha256"

# What to checksum:
INCLUDE_DIRS = ["data", "docs", "examples"]
INCLUDE_FILES = ["README.md", "LICENSE", "requirements.txt", "CHANGELOG.md", "CITATION.cff"]

# What to exclude:
EXCLUDE_DIRS = {".git", ".github", "scripts", "__pycache__"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_files() -> list[Path]:
    files: list[Path] = []

    for d in INCLUDE_DIRS:
        p = ROOT / d
        if not p.exists():
            continue
        for fp in p.rglob("*"):
            if fp.is_file():
                files.append(fp)

    for f in INCLUDE_FILES:
        fp = ROOT / f
        if fp.exists() and fp.is_file():
            files.append(fp)

    # Filter exclusions & make relative
    out: list[Path] = []
    for fp in files:
        rel = fp.relative_to(ROOT)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        out.append(fp)

    # Stable order
    out.sort(key=lambda x: str(x.relative_to(ROOT)).lower())
    return out


def write_checksums() -> None:
    lines = []
    for fp in iter_files():
        rel = fp.relative_to(ROOT).as_posix()
        digest = sha256_file(fp)
        lines.append(f"{digest}  {rel}")

    CHECKSUM_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"✅ Wrote {CHECKSUM_FILE.name} ({len(lines)} entries)")


def parse_checksums(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        digest, rel = line.split(None, 1)
        rel = rel.strip()
        out[rel] = digest
    return out


def check_checksums() -> None:
    if not CHECKSUM_FILE.exists():
        raise SystemExit(f"Missing {CHECKSUM_FILE.name}. Run without --check to generate it.")

    expected = parse_checksums(CHECKSUM_FILE.read_text(encoding="utf-8"))
    current: dict[str, str] = {}

    for fp in iter_files():
        rel = fp.relative_to(ROOT).as_posix()
        current[rel] = sha256_file(fp)

    # Compare
    missing = sorted(set(expected) - set(current))
    extra = sorted(set(current) - set(expected))
    mismatched = sorted([k for k in expected.keys() & current.keys() if expected[k] != current[k]])

    if missing or extra or mismatched:
        print("❌ Checksum verification failed")
        if missing:
            print(f"- Missing files (listed in checksums but not found): {missing}")
        if extra:
            print(f"- New files (not listed in checksums): {extra}")
        if mismatched:
            print(f"- Mismatched digests: {mismatched}")
        raise SystemExit(1)

    print("✅ Checksums verified")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verify checksums.sha256 instead of generating it.")
    args = parser.parse_args()

    if args.check:
        check_checksums()
    else:
        write_checksums()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

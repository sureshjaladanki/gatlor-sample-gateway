# SPDX-FileCopyrightText: 2026 Suresh Jaladanki
# SPDX-License-Identifier: Apache-2.0
"""Write sha256:<hex> of release/1.4.2/sbom.cdx.json into release-hash.txt."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SBOM = ROOT / "release" / "1.4.2" / "sbom.cdx.json"
OUT = ROOT / "release" / "1.4.2" / "release-hash.txt"


def main() -> None:
    digest = hashlib.sha256(SBOM.read_bytes()).hexdigest()
    OUT.write_text(f"sha256:{digest}\n", encoding="utf-8")
    print(OUT.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()

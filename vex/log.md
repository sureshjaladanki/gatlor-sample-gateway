This is a sample, made-up, nothing was filed.

# VEX decision log

Same KEV id on every row: **CVE-2024-1086** (Linux kernel nf_tables use-after-free; CISA KEV, listed since 2024-05-30). Keep all three. Do not delete a row. A later status supersedes; it does not replace the file.

The CLI output `dist/gatlor/vex.cdx.json` stays `in_triage` until a human records a decision. This log is that decision. OSV returned the Debian record `DEBIAN-CVE-2024-1086` (upstream CVE-2024-1086) because the frozen SBOM uses an OSV-queryable Linux purl.

| When | Status | Who | Note |
|---|---|---|---|
| Hour 0 (2026-09-22 09:00 Europe/Berlin) | under investigation | Ines Vogel | Match seen on release 1.4.2; not yet decided |
| Hour 6 (2026-09-22 15:00 Europe/Berlin) | affected | Ines Vogel | Confirmed present in 1.4.2 |
| Day 10 (2026-10-02) | fixed | Ines Vogel | 1.4.3 supersedes; the 1.4.2 record remains |

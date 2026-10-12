# Repo conventions

Owner: Suresh Jaladanki. Design date: 10 October 2026.

This repository is an evidence pack for a fictional product. It is not the Gatlor product.

## Layout

| Path | Owns |
|---|---|
| `README.md` | Write-up outline, later the article |
| `NOTICE.md` | Sample disclaimer |
| `LICENSE` | Apache-2.0 |
| `SECURITY.md` | Fictional disclosure route |
| `SUPPORT.md` | `support_period_end: YYYY-MM-DD` |
| `product/` | Fictional maker and product |
| `build/` | Buildroot config and how the SBOM was produced |
| `release/<version>/` | Frozen SBOM and release hash |
| `vex/` | Human decision log (supersede, never delete) |
| `clock/` | Report drafts, marked DRAFT |
| `drill/` | Hour-by-hour log |
| `gaps.md` | Honest misses |
| `.github/workflows/` | Runs `gatlor scan --sbom` on the frozen SBOM |
| `dist/` | CLI output, gitignored |

No Python workspace. No firmware or Linux image build in CI.

## Forbidden

- Claims that the product meets, passes, or is approved under the CRA, or other forbidden claim terms
- Filing or posting to ENISA; exploit detail
- Real company names, prices, internal plans
- Backdating, or deleting a VEX record
- Secrets

This is a sample, made-up, nothing was filed.

# The first 24 hours: an Article 14 early warning on a sample embedded Linux product

Fictional QG-1 gateway from fictional Quayline GmbH. Evidence pack for a Gatlor write-up. Nothing was sent to ENISA. Reporting for actively exploited vulnerabilities has applied since 11 September 2026.

## 1. Hook (reporting since 11 September 2026)

- Article 14 of Regulation (EU) 2024/2847: 24-hour early warning, 72-hour notification, 14-day final report after a fix is available.
- The maker files. Gatlor drafts. A named human confirms, edits, and files.
- This tree is the hour-one picture for a Linux gateway already in the field. See `NOTICE.md`.
- It is not a statement that QG-1 or any product meets the Cyber Resilience Act.

## 2. The sample (QG-1, made-up, nothing filed; Buildroot, same path as Yocto)

- Persona: `product/brief.md` — MQTT + Modbus TCP, default category (maker's view, not a legal opinion).
- Owner of the clock: Ines Vogel. Channels: work email and `#firmware-oncall`.
- Build: public Buildroot `qemu_aarch64_virt_defconfig` plus `build/local.fragment`. How-to: `build/README.md`.
- Same evidence path as a Yocto image: `gatlor scan --sbom` on the frozen release SBOM. Not Zephyr. CI does not build a Linux image.
- Licence: Apache-2.0 (`LICENSE`).

## 3. Step 0: SBOM exists

- Frozen release: `release/1.4.2/sbom.cdx.json` (product name `qg-1`, version `1.4.2`).
- Binding: `release/1.4.2/release-hash.txt` (`sha256:` of those bytes). Do not repair in place.
- How it was produced, and that a later rootfs generate is a new directory: `release/1.4.2/README.md`.
- Support end the CLI can parse: `SUPPORT.md` (`support_period_end: 2031-10-10`).
- Scan command: `gatlor scan --sbom release/1.4.2/sbom.cdx.json --out-dir dist/gatlor --repo-root .`

## 4. Step 1: known-exploited match

- KEV id: **CVE-2024-1086** (Linux kernel nf_tables). CISA KEV, listed since 2024-05-30.
- Component is in the frozen SBOM (Linux). OSV listed `DEBIAN-CVE-2024-1086` as the query id.
- CLI writes `dist/gatlor/vex.cdx.json` with every match `in_triage`. It does not decide.
- Checklist: `dist/gatlor/readiness-checklist.md`. Expect `vex-decided` to fail while matches exist.
- `dist/` is not committed. Get it from the `gatlor-sample-gateway-scan` CI artifact or a local run. OSV is queried live, so a later run can differ.

## 5. Step 2: hour 0–1, named confirmation starts the clock

- Timeline: `drill/timeline.md` (Europe/Berlin, 22 September 2026).
- T+0: match visible; alerts to email **and** `#firmware-oncall`.
- T+25 min: Ines confirms awareness in writing. **That** starts the legal clock. The CLI does not.
- Disclosure route for this sample: `SECURITY.md`.

## 6. Step 3: hours 1–24, early-warning draft; Gatlor does not file

- Draft: `clock/24h-early-warning.draft.md`.
- Every clock file starts: not filed, not sent to ENISA, a named human would file.
- Known at hour 20: product, release 1.4.2, component, CVE-2024-1086, awareness confirmed at T+25 min.
- Gatlor does not file. The maker edits, then files.

## 7. Step 4: VEX supersede

- Human log: `vex/log.md` — under investigation → affected → fixed.
- Same id on all three rows. Keep all three. Never delete.
- Day 10: 1.4.3 supersedes; the 1.4.2 record remains.
- CLI file stays `in_triage` until a human records a decision. The log is that decision.

## 8. Step 5: hour 24–72

- Draft: `clock/72h-notification.draft.md`.
- By hour 48: status **affected**, a mitigation note, next update pointed at 1.4.3.
- Still a draft. Nothing posted.

## 9. Step 6: day 3–14

- Draft: `clock/14d-final-report.draft.md`.
- After 1.4.3 is available: what changed, how users get the update.
- New release directory for 1.4.3. Do not rewrite 1.4.2's hash.

## 10. What went wrong in the exercise

- Honest list: `gaps.md`.
- Named owner existed here; many makers have none.
- Only email was watched until hour 3; `#firmware-oncall` sat idle.
- Vendored C and board-support blobs never made the SBOM.
- Out of hours: Gatlor is not 24/7. The maker still owns the clock.

## 11. What we do not do

- Do not file, auto-submit, or post to ENISA from this tree or from the CLI.
- Do not delete VEX. Do not backdate. Do not call the sample approved under the CRA.
- Do not build a Linux image in GitHub Actions. Do not treat a container as firmware.
- Do not pretend the CLI started the reporting clock.

## 12. What to do next: run the free CLI on your own build; or a review

- Local scan (product repo adjacent): `uv run --project ../project-gatlor gatlor scan --sbom release/1.4.2/sbom.cdx.json --out-dir dist/gatlor --repo-root .` — see `.github/workflows/README.md`.
- Point `--sbom` at **your** release CycloneDX, not this fictional file.
- Read the checklist. Record VEX as a human. Confirm awareness in writing.
- A paid review is a separate conversation. This sample is not an offer.

This is a sample, made-up, nothing was filed.

# Release 1.4.2

The hash in `release-hash.txt` binds `sbom.cdx.json` bytes. Do not repair the SBOM in place. A changed build is a new release directory.

## How this file was made

Declared-package CycloneDX 1.6, product name `qg-1`, version `1.4.2`. Package versions from Buildroot tag [2024.02.10](https://github.com/buildroot/buildroot/tree/2024.02.10) `.mk` files (`openssl` 3.2.3, `libcurl` 8.11.1, OpenSSH 9.7p1, busybox 1.36.1, mosquitto 2.0.20). Not a Syft scan of a built rootfs. CI does not run `make`. See `build/README.md`.

Generic purls for those userland packages are not OSV-recognisable. Linux uses `pkg:deb/debian/linux@6.1.38-4?arch=source&distro=bookworm` so OSV returns `DEBIAN-CVE-2024-1086`. Buildroot's defconfig kernel is `6.1.44`. That mismatch is recorded in `gaps.md`.

## KEV selection

- Catalogue: CISA Known Exploited Vulnerabilities, listed since 2024-05-30. This sample does not pin a catalogVersion.
- Rule: live row whose component name is in this SBOM; one id; confirm OSV returns it (or an alias) from `gatlor scan --sbom`.
- Pick: **CVE-2024-1086** (Linux kernel nf_tables). Firmware leads know this id. OSV id on this purl: `DEBIAN-CVE-2024-1086` (upstream CVE-2024-1086).

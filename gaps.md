This is a sample, made-up, nothing was filed.

# Gaps this exercise showed

- Named owner was listed in `product/brief.md`; many real makers have none.
- Only one channel was watched for the first hours. Email was read; `#firmware-oncall` sat idle until hour 3.
- C/C++ vendored code and board-support blobs the SBOM did not list.
- Out of hours: Gatlor does not run 24/7; the maker still owns the clock.
- CLI does not decide VEX and does not file.
- Generic Buildroot / `pkg:generic/...` purls returned no OSV hits. This week's frozen SBOM uses `pkg:deb/debian/linux@6.1.38-4?arch=source&distro=bookworm` so OSV can return `DEBIAN-CVE-2024-1086` (upstream CVE-2024-1086). That Debian version string is not the Buildroot kernel version `6.1.44`. A later rootfs generate is a new release directory, not a patch in place.
- That Debian Linux purl also returns an `in_triage` flood of at least 1000 rows. OSV caps one batch query at 1000 results, and the CLI does not fetch further pages, so the true count is higher. The drill follows one KEV id. The CLI does not filter to KEV.

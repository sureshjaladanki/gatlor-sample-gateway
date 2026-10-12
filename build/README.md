This is a sample, made-up, nothing was filed.

# How this SBOM was produced

Frozen Buildroot tag: [2024.02.10](https://github.com/buildroot/buildroot/tree/2024.02.10).
Public defconfig: [`qemu_aarch64_virt_defconfig`](https://github.com/buildroot/buildroot/blob/2024.02.10/configs/qemu_aarch64_virt_defconfig).
Extra packages: `local.fragment`.

## Reproduce locally (not in CI)

1. Check out Buildroot `2024.02.10`.
2. `make qemu_aarch64_virt_defconfig`.
3. Merge `local.fragment` into `.config` (`make olddefconfig`).
4. `make`.
5. Build a CycloneDX file from Buildroot legal-info/SBOM output, or `syft dir:output/target -o cyclonedx-json`.
6. Commit the JSON under a **new** `release/<version>/` directory. Do not repair a hashed SBOM in place.

This week's frozen file in `release/1.4.2/` is a **declared-package** CycloneDX: versions taken from that tag's package `.mk` files, plus an OSV-queryable Linux purl (see `release/1.4.2/README.md`). It is not a Syft scan of a built rootfs. CI must not run `make`.

A Yocto image uses the same evidence path: `gatlor scan --sbom` on the release SBOM. This sample is Buildroot so the tree stays small. It is not a claim that Buildroot and Yocto are the same product.

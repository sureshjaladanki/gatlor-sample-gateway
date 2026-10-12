This is a sample, made-up, nothing was filed.

# CI

`gatlor-scan.yml` calls the product-repo action `sureshjaladanki/project-gatlor/.github/actions/gatlor@v0.1.1` with `sbom: release/1.4.2/sbom.cdx.json`. Syft is skipped. The action uploads `dist/gatlor` as the `gatlor-sample-gateway-scan` artifact. This sample does not store a token.

Run the same scan locally from this directory, with `project-gatlor` adjacent:

```text
uv run --project ../project-gatlor gatlor scan --sbom release/1.4.2/sbom.cdx.json --out-dir dist/gatlor --repo-root .
```

`--project` keeps this directory as the working tree so the SBOM path resolves. `uv run --directory` would look for the SBOM inside `project-gatlor`.

Pin a release tag, not a branch. Do not add a `make` / Yocto / Docker firmware job.

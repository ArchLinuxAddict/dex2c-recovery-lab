# Toolkit compatibility

| Lab release | Toolkit release | Status |
|---|---|---|
| 1.0.0 | `dex2c-recovery-toolkit` v1.0.0 | Examples validated locally; CI installs the toolkit tag |

## Convention

- The toolkit is authoritative for implementation releases.
- Lab examples pin a toolkit tag or commit.
- A lab release does not imply compatibility with every toolkit version.
- The final campaign findings are research results from a private workspace;
  they are not a guarantee that the public toolkit reproduces every phase.

## Example compatibility

`examples/basic-dex-analysis` and `examples/validation` use only the public
generic DEX parsing/validation API and are expected to work with v1.0.0.

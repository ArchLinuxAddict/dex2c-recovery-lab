# Methodology

## Scope

The campaign analyzed one authorized Dex2C-protected Android application at a
recorded package/version/hash. The target APK and recovered code are not
redistributed.

## Evidence path

1. Inventory the unchanged APK, DEX files, native libraries, and embedded
   artifacts (embedded content is not treated as authoritative).
2. Parse protected DEX declarations and identify methods with native
   declarations and no code items.
3. Analyze ELF exports and registration tables; map Java methods to native
   functions.
4. Disassemble and, where available, decompile mapped native functions.
5. Trace JNI argument, field, `jvalue`, receiver, and superclass data flow.
6. Generate Dalvik only when every required value is resolved and legal.
7. Validate the DEX structurally and with external disassemblers.
8. Run finite native-vs-generated comparisons where a safe harness exists.
9. Record provenance, tested inputs, and limitations per method.

## Classification discipline

- Structural validity is not behavioral equivalence.
- A finite differential test covers only tested inputs.
- A behavioral reconstruction is not the original instruction sequence.
- Exact recovery requires an authoritative reference artifact.
- Unknown/ambiguous values are never replaced by guesses.

## Reproducibility

The final counts are verifiable from the research workspace manifests cited in
`results/sanitized/verification.md`. The public toolkit covers the generic
pipeline; target-specific Phase IV–VII drivers are not included. The lab
therefore distinguishes verified findings from one-command reproduction.

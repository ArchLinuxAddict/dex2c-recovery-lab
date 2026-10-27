# Limitations

- No original code items, IR, debug data, or source survived for the transformed
  methods.
- Native decompilation does not uniquely determine original register allocation,
  debug metadata, exception tables, or instruction order.
- 225 methods remain native-analyzed untranslated.
- 10 high-priority constructors remain partial and 1 is rejected.
- Direct native comparison is limited to three methods plus one partial
  constructor observation.
- The device environment used for the recorded differential tests is no longer
  attached; the publication re-run has two environment skips.
- Target-specific campaign drivers and target artifacts are not published.
- The public toolkit is the generic pipeline, not the full research campaign.
- The target package/version/hash identifies the case study but does not grant
  rights to redistribute the APK or recovered code.

## Needed for further progress

- Authoritative original DEX/code items or original build artifacts.
- A stable dependency/class-loader harness for constructors.
- Additional symbolic/alias analysis for allocations and helper semantics.

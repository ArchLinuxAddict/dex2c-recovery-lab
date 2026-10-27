# Verification trail

The sanitized counts were checked against the preserved final campaign
manifest in the private research workspace:

- Final counts: behavioral 103, partial 8, native 225, exact 0, total 336.
- High-priority dispositions: 41 applied, 10 partial, 1 rejected.
- Field assignments: 86 = 81 source-parameter + 5 explicit-constant.
- Final DEX method inventory: 103 with code; no baseline method removed.
- Structural/invoke checks: 108 invokes, 116 field operations, 0 issues.
- Recorded tests: 100 passed / 0 failed / 1 skipped.
- Publication re-run: 99 passed / 0 failed / 2 skipped because no authorized
  ADB device was attached. No failure was hidden by this discrepancy.

The source manifest, recovered DEX, target APK, and per-method target records
are not published. Therefore the figures are **verified against preserved
private artifacts**, but the full campaign is not a one-command public
reproduction. The public toolkit's generic pipeline and synthetic examples are
separately reproducible.

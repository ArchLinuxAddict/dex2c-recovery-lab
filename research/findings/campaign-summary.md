# Final campaign summary

## Reference target

- Package: `com.dpkay.apps.developer_options_toggler`
- Version: `2.87 (198)`
- APK SHA-256: `076666770f4649f2df86fa896c1e35bf7a2a5ca8f03a29e8b486bd468a88c7e9`

The APK is not redistributed.

## Final verified counts

| Classification | Count |
|---|---:|
| Exact recovered | 0 |
| Semantically equivalent (proven) | 0 |
| Behaviorally reconstructed | 103 |
| Partial | 8 |
| Native analyzed untranslated | 225 |
| Unresolved at summary level | 0 |
| Canonical total | 336 |

High-priority constructors: 41 applied, 10 partial, 1 rejected (52 total).
Value-flow constructor field assignments: 86 (81 source-parameter, 5 explicit
constant).

## What the campaign added

Relative to the verified on-disk Phase VII state (86 behavioral), the final
campaign added 17 behavioral reconstructions: 10 constructors and 7 leaf
methods. Ten further constructors were already present on disk but were
re-audited and validated in the campaign rather than counted as new.

## Validation

- Final DEX: 103 methods with code, structurally valid, 108 invokes and 116
  field operations checked with 0 issues.
- Direct native-vs-generated checks: `hidden`, `sensitiveKey`, and the KeyEvent
  mapping passed on the available rooted device.
- Generated constructor harnesses passed for the recorded constructor and the
  v2 rule harness.
- One constructor had a partial native field observation.
- 10 constructors and other dependency-heavy methods were not directly
  native-tested.

## Tests

- Recorded campaign run: 100 passed, 0 failed, 1 skipped (device-gated).
- Publication-environment re-run: 99 passed, 0 failed, 2 skipped, because no
  authorized ADB device was attached. This is an environment discrepancy, not a
  test failure.

See `results/sanitized/verification.md` for the verification trail.

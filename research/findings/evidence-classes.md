# Evidence classes

| Class | Meaning | Public evidence |
|---|---|---|
| Exact recovered | Original method bytecode recovered and verified against an authoritative reference | 0 in this campaign |
| Semantically equivalent | Proven equivalent to the original for all behaviors | 0 proven |
| Behaviorally reconstructed | Selected behavior represented by generated Dalvik | 103 final |
| Partial | Only some behavior/operations represented | 8 final |
| Native analyzed untranslated | Native details analyzed; no complete translated DEX | 225 final |
| Unresolved | Insufficient evidence | 0 final at the campaign summary level |

The 336 canonical candidates reconcile as 103 + 8 + 225.

No exact or universal semantic-equivalence claim is made. Structural validation
and finite tests do not establish either.

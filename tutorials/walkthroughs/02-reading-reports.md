# Walkthrough 2: reading reports without overclaiming

## Separate the fields

When inspecting a method record, keep these distinct:

- **status**: what the pipeline decided
- **evidence**: why
- **confidence**: mapping certainty
- **validation**: structural checks
- **behavioral test**: finite observed inputs, if any

## Interpreting common outcomes

| Outcome | Safe interpretation |
|---|---|
| `EXACT_DEX` with independent validation | A supplied artifact was present and structurally valid; inspect provenance |
| `BEHAVIOR_RECONSTRUCTED` | A generated implementation represents selected behavior |
| `PARTIALLY_RECONSTRUCTED` | Only some behavior/operations are represented |
| `NATIVE_ANALYZED` | Native evidence exists; no complete translation |
| `UNRESOLVED` | Insufficient evidence |
| `AMBIGUOUS` mapping | Multiple or incomplete identities; not confirmed |

## Unsafe interpretations

- "The DEX parses, therefore the method is correct."
- "One test passed, therefore the behavior is universally equivalent."
- "A native function was mapped, therefore the original bytecode is known."
- "A method count proves recovery quality."

## Recommended report sequence

1. Read limitations and environment.
2. Check input and artifact hashes.
3. Review mapping confidence and alternatives.
4. Review recovery classification and evidence.
5. Review validation separately.
6. Treat behavioral tests as finite evidence.
7. Report unresolved methods explicitly.

## Synthetic sample

The examples in `examples/` print JSON for a self-created fixture. They exercise
parsing and validation only; they are not a campaign result.

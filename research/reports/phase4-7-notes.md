# Phase IV–VII research notes (sanitized)

## Phase IV — re-baseline

Rebuilt the native evidence and recovery worklist for the reference target,
verified 336 canonical candidates, and separated pre-existing native methods,
loader infrastructure, ambiguous registrations, and transformed methods.
Differential testing was introduced for methods with a safe harness.

## Phase V — source-informed model

Documented the Dex2C transformation model and performed controlled round-trip
experiments. Exact original instruction recovery is not possible from target
metadata alone; the source model informs evidence interpretation, not guessing.

## Phase VI — opportunity mining

Added evidence-backed rules for discard-result/null-return wrappers and a small
KeyEvent action mapping. Introduced direct native-vs-generated comparisons for
three methods.

## Phase VII — constructor value flow

Resolved field identities from native resolver calls, traced parameter and
constant origins, and applied constructors only when every field assignment had
a complete origin. Later campaign work added reference assignability, direct
parameter values, `jvalue` slot reconstruction, and an explicit
`Objects.requireNonNull` helper contract.

The final closure extended the worklist to 103 behavioral reconstructions while
preserving all prior verified methods.

## Non-claims

These notes do not publish target-specific campaign drivers, class inventories,
raw manifests, or recovered application code. They summarize evidence and
limitations only.

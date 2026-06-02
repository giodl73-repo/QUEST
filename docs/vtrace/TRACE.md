# QUEST Trace

## Scope

Repo: QUEST

VTRACE stage: Trace

Baseline date: 2026-06-01

## Trace Matrix

| Trace ID | Mission / CONOPS | Requirements | Specs | Architecture | Interfaces | Verification | Validation | Status |
|---|---|---|---|---|---|---|---|---|
| TR-QST-001 | NEED-QST-001, CON-QST-001 | REQ-QST-001, REQ-QST-002 | SPEC-QST-001 | ARCH-QST-001 | IF-QST-001 | VER-QST-001 | VAL-QST-001 | traced_with_work_package_needed |
| TR-QST-002 | NEED-QST-002, CON-QST-002 | REQ-QST-003, REQ-QST-004 | SPEC-QST-002 | ARCH-QST-002 | IF-QST-002, IF-QST-003 | VER-QST-002, VER-QST-003, VER-QST-004, VER-QST-005 | VAL-QST-002, VAL-QST-003 | traced_with_work_package_needed |
| TR-QST-003 | NEED-QST-003, NEED-QST-004, CON-QST-003, CON-QST-004 | REQ-QST-005, REQ-QST-006, REQ-QST-007 | SPEC-QST-003, SPEC-QST-004 | ARCH-QST-003 | IF-QST-004 | VER-QST-006 | VAL-QST-004 | traced_with_work_package_needed |
| TR-QST-004 | NEED-QST-005, CON-QST-005 | REQ-QST-008 | SPEC-QST-005 | ARCH-QST-004 | IF-QST-005 | VER-QST-007 | VAL-QST-005 | traced_with_work_package_needed |

## Open Trace Gaps

| Gap ID | Gap | Disposition |
|---|---|---|
| GAP-QST-001 | Complete-session checklist needs VTRACE-indexed artifact rows. | Create work package for closeout checklist lock. |
| GAP-QST-002 | Engine recovery tests need selected command proof. | Create work package for checkpoint/recovery verification. |
| GAP-QST-003 | MUDDLE interface rows need fixture execution evidence. | Create work package for MUDDLE surface proof. |

Deferred specification visibility: SPEC-QST-UNK-001, SPEC-QST-UNK-002, and
SPEC-QST-UNK-003 are intentionally dispositioned through later validation,
verification, interfaces, and work-package rows rather than treated as accepted
implementation specs.

## Role Review Summary

Role lenses applied from `.roles/`. No critical or major actionable trace gaps
remain outside the listed work-package candidates.

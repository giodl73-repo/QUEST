#!/usr/bin/env bash
# build-guides.sh — Compile guides from src/guides/ to docs/guides/
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKSPACE_TARGET="${REPO_ROOT}/../target"
PROOF="${WORKSPACE_TARGET}/debug/proof"
[ ! -f "${PROOF}" ] && [ ! -f "${PROOF}.exe" ] && PROOF="${REPO_ROOT}/../proof/target/debug/proof"
[ ! -f "${PROOF}" ] && [ ! -f "${PROOF}.exe" ] && { echo "proof binary not found. Run: cd C:/src && cargo build"; exit 1; }
SRC_DIR="${REPO_ROOT}/src/guides"
OUT_DIR="${REPO_ROOT}/docs/guides"
mkdir -p "${OUT_DIR}"
echo ""; echo "guide build: $(basename ${REPO_ROOT})"; echo "  source: ${SRC_DIR}"; echo "  output: ${OUT_DIR}"; echo ""
if [ "${1:-}" = "--check" ]; then
  "${PROOF}" compile --check --root "${REPO_ROOT}" "${SRC_DIR}" 2>&1
else
  "${PROOF}" compile --root "${REPO_ROOT}" --output-dir "${OUT_DIR}" "${SRC_DIR}" 2>&1
  echo "compiled → ${OUT_DIR}"
fi

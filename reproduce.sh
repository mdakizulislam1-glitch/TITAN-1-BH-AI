#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/content/TITAN1_ENGINEERING_WORKSPACE"
TEST_FILE="$WORKSPACE/tests/test_model.py"

echo "=== TITAN-1 reproducibility check ==="

if [[ ! -f "$TEST_FILE" ]]; then
echo "ERROR: regression test file not found: $TEST_FILE" >&2
exit 1
fi

cd "$WORKSPACE"

echo "Running automated regression tests..."
python -m pytest -q "$TEST_FILE"

echo
echo "PASS: automated regression tests completed."
echo "SCOPE: checkpoint loading and basic inference tests only."
echo "LIMITATION: scientific benchmark reproduction and Docker validation are not included."

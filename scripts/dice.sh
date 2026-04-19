#!/usr/bin/env bash
# dice.sh — fair RNG dice roller for the marathon workshop.
# Usage:
#   ./dice.sh "1d20+5"           → rolls=[14] mod=5 total=19
#   ./dice.sh "1d20+3 adv"       → rolls=[7, 18] (adv → 18) mod=3 total=21
#   ./dice.sh "2d6+2"            → rolls=[4 3] mod=2 total=9
#   DICE_SEED=20260418 ./dice.sh "1d20"  → reproducible
#
# Output contract (one line):
#   rolls=[<ints>] mod=<int> total=<int> [CRIT|FUMBLE]

set -euo pipefail

expr_raw="${1:-1d20}"
expr="$(echo "$expr_raw" | tr '[:upper:]' '[:lower:]')"

# Seed RNG if DICE_SEED is set
if [[ -n "${DICE_SEED:-}" ]]; then
  # bash $RANDOM is seeded by setting RANDOM
  # Use a stable derivation from DICE_SEED
  RANDOM=$(( ${DICE_SEED//[^0-9]/} % 32767 ))
  # Advance a few steps so consecutive calls differ
  : $(( RANDOM )); : $(( RANDOM ))
fi

# Detect advantage / disadvantage mode
mode="normal"
if [[ "$expr" =~ (^|[[:space:]])(adv|advantage)([[:space:]]|$) ]]; then
  mode="adv"
fi
if [[ "$expr" =~ (^|[[:space:]])(dis|disadvantage)([[:space:]]|$) ]]; then
  mode="dis"
fi

# Strip mode words from the expression
core="$(echo "$expr" | sed -E 's/(^|[[:space:]])(adv|advantage|dis|disadvantage)([[:space:]]|$)/\1\3/gi' | tr -d '[:space:]')"

# Parse NdS+M / NdS-M / NdS
if [[ "$core" =~ ^([0-9]+)d([0-9]+)([+\-][0-9]+)?$ ]]; then
  num="${BASH_REMATCH[1]}"
  sides="${BASH_REMATCH[2]}"
  mod_raw="${BASH_REMATCH[3]:-+0}"
  mod="$mod_raw"
else
  echo "error: cannot parse dice expression '$expr_raw'" >&2
  exit 1
fi

roll_one() {
  # Usage: roll_one N S → prints "total roll1 roll2 ..."
  local n="$1" s="$2"
  local total=0
  local rolls=""
  local i r
  for ((i = 0; i < n; i++)); do
    r=$(( RANDOM % s + 1 ))
    rolls+="$r "
    total=$(( total + r ))
  done
  echo "$total $rolls"
}

# Detect crit/fumble on d20s
crit_fumble_tag() {
  local rolls="$1"
  local die_size="$2"
  if [[ "$die_size" != "20" ]]; then
    echo ""
    return
  fi
  for r in $rolls; do
    if [[ "$r" == "20" ]]; then echo "CRIT"; return; fi
  done
  for r in $rolls; do
    if [[ "$r" == "1" && "$rolls" != *"20"* ]]; then echo "FUMBLE"; return; fi
  done
  echo ""
}

if [[ "$num" == "1" && "$sides" == "20" && "$mode" != "normal" ]]; then
  # d20 adv/dis: two rolls, pick one
  read -r t1 r1 _ <<< "$(roll_one 1 20)"
  read -r t2 r2 _ <<< "$(roll_one 1 20)"
  r1="${r1%% *}"
  r2="${r2%% *}"
  if [[ "$mode" == "adv" ]]; then
    if (( r1 >= r2 )); then pick="$r1"; else pick="$r2"; fi
    label="adv"
  else
    if (( r1 <= r2 )); then pick="$r1"; else pick="$r2"; fi
    label="dis"
  fi
  total=$(( pick + mod ))
  tag="$(crit_fumble_tag "$pick" 20)"
  if [[ -n "$tag" ]]; then tag=" $tag"; fi
  printf 'rolls=[%s, %s] (%s → %s) mod=%s total=%s%s\n' "$r1" "$r2" "$label" "$pick" "$mod" "$total" "$tag"
else
  read -r dice_total dice_rolls <<< "$(roll_one "$num" "$sides")"
  # Trim trailing space
  dice_rolls="$(echo "$dice_rolls" | sed 's/[[:space:]]*$//')"
  total=$(( dice_total + mod ))
  tag="$(crit_fumble_tag "$dice_rolls" "$sides")"
  if [[ -n "$tag" ]]; then tag=" $tag"; fi
  printf 'rolls=[%s] mod=%s total=%s%s\n' "$dice_rolls" "$mod" "$total" "$tag"
fi

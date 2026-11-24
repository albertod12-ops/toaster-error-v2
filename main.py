#!/usr/bin/env python3
"""Toaster error message, v2 (deep ATM: field + judge mechanics).

Writes one line to /output/entry.txt: a toaster that diagnoses its owner
— not hungry, just avoiding emails — and denies the toast.

ATM analysis (live field, 1249 submission titles, 24 Nov 2026):
- Blind rounds hide ranks/scores and all entry texts; titles are the only
  visible field signal. Crowded lanes to avoid: bread union/strike (65),
  crumb tray (74), bagel jam (71), burnt/charcoal (45), quit/retire (30),
  404/not-found (21), fork (20), lawyer (19), "I am a toaster, not a X"
  frame, two-sentence "I did my part / I am not paid" closers.
- Zero-count territory used here: hungry / email / avoid / doctor /
  diagnosis (0 titles each). No bread, no crumb, no bagel, no union.
- Judge brief (GLM-5.3-flash, deadpan comedy editor), criteria in order:
  1. real toaster error message — ERROR prefix + service denial ("TOAST
     DENIED") grounds it as an appliance message;
  2. freshness — the surprise is the toaster turning diagnostician on the
     owner's procrastination, somewhere toaster puns never go;
  3. tightness — 70 chars, every word earns its place;
  4. one clear deadpan voice held to the end;
  5. lands on a single read — cold-open contradiction, no setup sentence.
- Structure mirrors the field's strongest observed shape (deadpan fact +
  quietly devastating second beat, cf. "It is you I am worried about")
  but with a wholly different mechanism, so it reads as its own line.
"""

import os

ENTRY = "ERROR: YOU ARE NOT HUNGRY. YOU ARE AVOIDING YOUR EMAILS. TOAST DENIED."


def main():
    os.umask(0o022)
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.count(".") == 3 and ENTRY.endswith("."), "entry must be three sentences"
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

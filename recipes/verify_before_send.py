"""Verify a list of emails in batches of 100. Print verified, hold and invalid piles.

Run: export LEADSETS_KEY=ls_live_…   then  python recipes/verify_before_send.py emails.txt
"""

from __future__ import annotations

import sys

from leadsets import Leadsets


def load(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python recipes/verify_before_send.py emails.txt", file=sys.stderr)
        return 2
    emails = load(sys.argv[1])
    ls = Leadsets()
    piles = {"verified": [], "hold": [], "invalid": [], "not_checked": []}
    for i in range(0, len(emails), 100):
        batch = emails[i : i + 100]
        res = ls.emails.verify(batch)
        for r in res.results:
            row = (r.email, r.status, r.confidence, r.checked_at, r.reason)
            if r.status == "verified":
                piles["verified"].append(row)
            elif r.status == "invalid":
                piles["invalid"].append(row)
            elif r.status is None:
                piles["not_checked"].append(row)
            else:
                piles["hold"].append(row)
        print("batch summary:", res.summary, "request_id:", res.request_id)
    for name, rows in piles.items():
        print(f"\n# {name} ({len(rows)})")
        for row in rows:
            print("\t".join("" if x is None else str(x) for x in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

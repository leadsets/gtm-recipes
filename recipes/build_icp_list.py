"""Build a small ICP list with match reasons and verified emails.

Run: export LEADSETS_KEY=ls_live_…   then  python recipes/build_icp_list.py

At public launch on 10 December 2026, the free plan will be 1,000 enrichments plus 100 search records, no card, one time. Until then, join the waitlist.
Records only count when data comes back. Catch-all and unknown are held, not treated as verified.
"""

from __future__ import annotations

import os
import sys

from leadsets import Leadsets

# Edit these filters for your ICP.
FILTERS = dict(
    function=["revenue"],
    seniority=["vp", "head"],
    employees="20-200",
    country="US",
    industry="saas",
    limit=10,
)


def main() -> int:
    if not (os.environ.get("LEADSETS_KEY") or os.environ.get("LEADSETS_API_KEY")):
        print("Set LEADSETS_KEY first. Join the waitlist: https://www.leadsets.ai/signup (public launch 10 December 2026)", file=sys.stderr)
        return 2

    ls = Leadsets()
    usage = ls.usage.get()
    print("plan:", usage.plan)
    print("usage snapshot:", usage.usage)

    res = ls.people.search(**FILTERS)
    print("search counted:", res.usage)
    people = list(res.items)
    emails = [p.email.address for p in people if p.email and p.email.address]

    status_by = {}
    if emails:
        verified = ls.emails.verify(emails)
        for r in verified.results:
            status_by[r.email] = r

    print("\nname | title | company | reasons | email | status | checked_at")
    for p in people:
        company = p.company.name if p.company else "?"
        address = p.email.address if p.email else ""
        v = status_by.get(address)
        status = v.status if v else (p.email.status if p.email else "")
        checked = v.checked_at if v else (p.email.checked_at if p.email else "")
        reasons = ", ".join(p.match_reasons or [])
        flag = ""
        if status and status != "verified":
            flag = "  [hold or drop]"
        print(f"{p.full_name} | {p.title} | {company} | {reasons} | {address} | {status} | {checked}{flag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Leadsets GTM recipes

Copy-and-run recipes for [Leadsets](https://www.leadsets.ai/): build an ICP list, verify emails before you send, and prompt Claude or Cursor to do the same over MCP.

Leadsets is Unlimited B2B Contact Data for AI Agents, Starting from $29/mo (paid plans; fair-use rate limits apply).

[Join the waitlist](https://www.leadsets.ai/signup) (public launch 10 December 2026). At launch, the free plan will include 1,000 enrichments plus 100 search records, no card. Keys start with `ls_live_`. The official SDKs read `LEADSETS_KEY` or `LEADSETS_API_KEY`. Do not commit a real key.

## Contents

| Path | What it is |
| --- | --- |
| [recipes/build_icp_list.py](recipes/build_icp_list.py) | Python: search, verify, print match reasons and email status |
| [recipes/build_icp_list.ts](recipes/build_icp_list.ts) | TypeScript version of the same list builder |
| [recipes/verify_before_send.py](recipes/verify_before_send.py) | Python: verify a text file of emails in batches of 100 |
| [prompts/claude-find-leads.md](prompts/claude-find-leads.md) | A precise Claude prompt once MCP is connected |
| [prompts/cursor-gtm.md](prompts/cursor-gtm.md) | A Cursor prompt that writes a verified markdown table |
| [configs/cursor-mcp.json](configs/cursor-mcp.json) | Cursor MCP snippet for `https://mcp.leadsets.ai` |

## Setup

```bash
# Python
pip install leadsets
export LEADSETS_KEY=ls_live_…
python recipes/build_icp_list.py

# TypeScript
npm install @leadsetsai/sdk
export LEADSETS_KEY=ls_live_…
npx tsx recipes/build_icp_list.ts
```

At public launch on 10 December 2026, the free plan will be 1,000 enrichments plus 100 search records, no card, one time. Until then, join the waitlist. Paid plans are a flat monthly price with fair-use limits per five hours and per week. Call `ls.usage.get()` (or the `get_usage` MCP tool) before a large run. See [pricing](https://www.leadsets.ai/pricing) and [How Leadsets fair-use limits work](https://telegra.ph/How-Leadsets-fair-use-limits-work-5-hour-and-weekly-windows-11-20).

Email statuses are verified, catch-all, unknown and invalid. Uncertain results are not rounded up. Keep the receipt fields (`match_reasons`, `status`, `checked_at`, `request_id`) in your output.

## Related

- [n8n workflows](https://github.com/leadsets/n8n-workflows)
- [Job intent agent](https://github.com/leadsets/job-intent-agent)
- [Official Python SDK](https://github.com/leadsets/sdk-python) and [TypeScript SDK](https://github.com/leadsets/sdk)
- [MCP connection repo](https://github.com/leadsets/leadsets-mcp)
- [How to find leads with Claude](https://telegra.ph/How-to-find-B2B-leads-with-Claude-and-Leadsets-11-20)
- [Using Leadsets MCP lead data inside Cursor](https://telegra.ph/Using-Leadsets-MCP-lead-data-inside-Cursor-11-20)
- [How to read a Leadsets receipt](https://telegra.ph/How-to-read-a-Leadsets-receipt-match-reasons-verification-status-and-checked-at-11-20)

## License

MIT. See [LICENSE](LICENSE).

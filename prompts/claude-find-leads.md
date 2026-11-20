# Claude prompt: find leads with Leadsets

Use after you connect the Leadsets MCP server (`https://mcp.leadsets.ai`). Written guide: https://telegra.ph/How-to-find-B2B-leads-with-Claude-and-Leadsets-11-20

```
Using the Leadsets tools, first call get_usage.

Then find 10 VPs or heads of revenue at US SaaS companies with 20 to 200 employees.
For each person, include name, title, company, match reasons, email, verification status and checked_at.

Verify every email with verify_email. Do not treat catch-all or unknown as verified.
Return three lists: verified, hold (catch-all or unknown), invalid.

If a promising person has no email, try enrich_person with their name and company domain.
If usage is too low for this run, stop and tell me what is left instead of guessing.
```

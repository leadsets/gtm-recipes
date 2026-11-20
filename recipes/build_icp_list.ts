// Build a small ICP list with match reasons and verified emails.
// Run: export LEADSETS_KEY=ls_live_…   then  npx tsx recipes/build_icp_list.ts
import { Leadsets } from '@leadsetsai/sdk'

const FILTERS = {
  function: ['revenue'],
  seniority: ['vp', 'head'],
  employees: '20-200',
  country: 'US',
  industry: 'saas',
  limit: 10,
}

const ls = new Leadsets(process.env.LEADSETS_KEY)
const usage = await ls.usage.get()
console.log('plan:', usage.plan)

const res = await ls.people.search(FILTERS)
const emails = res.items.map((p) => p.email?.address).filter((x): x is string => Boolean(x))
const statusBy = new Map<string, { status?: string | null; checked_at?: string | null }>()
if (emails.length) {
  const verified = await ls.emails.verify(emails)
  for (const r of verified.results) statusBy.set(r.email, r)
}

console.log('name | title | company | reasons | email | status | checked_at')
for (const p of res.items) {
  const address = p.email?.address ?? ''
  const v = statusBy.get(address)
  const status = v?.status ?? p.email?.status ?? ''
  const checked = v?.checked_at ?? p.email?.checked_at ?? ''
  const flag = status && status !== 'verified' ? '  [hold or drop]' : ''
  console.log(
    `${p.full_name} | ${p.title} | ${p.company?.name ?? '?'} | ${(p.match_reasons ?? []).join(', ')} | ${address} | ${status} | ${checked}${flag}`,
  )
}

## Request and scope

Ben requested a permanent ERP mock server so a third party can test the dashboard from GitHub, plus a README tutorial. This separate stacked PR adds that runnable local demo without changing application features, presentation or financial calculations.

- Maintained loopback Business Central contract mock for the real scraper's NTLM/OData subset, with deterministic fictional companies and histories.
- Explicit isolated launcher composes the existing pg-mem fixture, real compiled scraper job and dashboard. Three snapshots import at startup; terminal `import` runs another actual import; restart resets everything.
- Allowlisted child environment, blocked legacy DB/config modules and socket restriction prevent use of old database/ERP credentials. No new public network exposure or deployment.
- README has verified clone/install/build/start/roles/import/reset instructions and limitations.
- Restrict scraper compiler input to `src` so `.cjs` tests no longer shift job output into `dist/src`.

## Try it

```sh
git clone --branch feat/erp-demo-server https://github.com/hosakb/bachelor-thesis.git
cd bachelor-thesis
npm --prefix dashboard ci --ignore-scripts
npm --prefix scraper ci --ignore-scripts
npm --prefix scraper run build
node demo/start.cjs
```

Open http://127.0.0.1:3407 and choose a fictional role. Node 26.12.1/npm 12.0.2 were exercised. No private credentials, PostgreSQL install, VPN or `.env` setup is needed.

## Verification

- Four focused mock/import/launcher tests pass, independently rerun by a read-only technical reviewer with no must-fix findings.
- Actual GitHub clean clone at `0246e13b61b505c8d253287abe98832a44adc800`: literal README install/build path, all four tests and all twelve browser cases pass again.
- Twelve browser cases cover four roles at desktop 1440, tablet 834 and mobile 390 widths; zero recorded console/page/HTTP/external-request errors. Real Chart.js series and navigation/reload persistence verified.
- Existing 21 server tests, isolated model test, scraper NTLM contract, TypeScript and ESLint pass. Existing full browser suites pass 19 steps plus remaining onboarding/patent/fund CRUD flows and eight role-picker checks. Stress includes four roles with five concurrent reloads each and a 153-row SQL portfolio fixture.
- Actual desktop/mobile startup, admin, fund and stakeholder screenshots inspected; existing colors, layout and intentional table/timeline scrolling preserved.
- Details and limitations: [demo/qa/verification.md](https://github.com/hosakb/bachelor-thesis/blob/feat/erp-demo-server/demo/qa/verification.md).

## Screenshots

![Imported startup financial history, desktop](https://raw.githubusercontent.com/hosakb/bachelor-thesis/feat/erp-demo-server/demo/qa/startup-1440.png)
![Imported financial history, mobile](https://raw.githubusercontent.com/hosakb/bachelor-thesis/feat/erp-demo-server/demo/qa/startup-390.png)

## Dependency and limitations

Stacked on open modernization PR #3, which itself depends on role-picker PR #2. Base is `style/pr1-frontend-modernization`; only ERP/tutorial/build changes belong to this diff. PR #1 is already merged and is not recreated or changed. Do not merge out of dependency order.

This is a narrow NTLM/OData contract mock, not Dynamics emulation or real password authentication. pg-mem is not a live PostgreSQL deployment. No live ERP/database integration, deployment or cross-browser compatibility is claimed. Existing dependency audit warnings remain, and no unrelated audit upgrades were made. No merge or user-service restart performed. GitHub has no configured checks on the existing stack; local results are not a claim of green CI.
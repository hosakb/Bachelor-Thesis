## Request and scope

Separate follow-up for the recorded dashboard Gantt HTML, server-validation and session-configuration findings. Based on the reviewed frontend branch, not a replay of merged PR #1. No financial formulas, dashboard features, palette or role semantics changed.

- Encode both Frappe Gantt SVG labels and custom popup fields for Startup and Fund/Stakeholder views. Preserve literal names through save/cancel and reload, without double encoding.
- Wrap and confine long popups inside the visible chart container. Actual mobile visual inspection found clipping; the fix has browser bounding-box assertions.
- Validate Gantt progress/dates, milestone add/update batches, TRL add/edit and onboarding before writes. Reject malformed types, non-finite/range-invalid numbers, invalid calendar dates, reversed periods, blank names and malformed batches. Preserve existing ownership checks.
- Remove the fixed session secret. Production requires an explicit secret of at least 32 characters after trimming; local/test processes get ephemeral random secrets when none is configured. HttpOnly/SameSite=Lax cookies and Secure in production; resave is false.
- Document production implications in [dashboard/SESSION_CONFIGURATION.md](https://github.com/hosakb/bachelor-thesis/blob/fix/dashboard-hardening/dashboard/SESSION_CONFIGURATION.md). No deployed settings or credentials were changed.

## Verification

- Original browser regression reproduced unsafe HTML parsing on the unchanged branch.
- 27 server/unit tests pass, including six new hardening tests; the separate isolated model test passes. ESLint, TypeScript and diff whitespace checks pass.
- Six new stored-markup browser cases cover Startup, Fund and Stakeholder at desktop 1440 and mobile 390. Literal label/popup text, absent image nodes/payload execution, saved progress readback, cancelled progress non-persistence, reload and popup geometry verified. Zero recorded console/page errors.
- Existing full browser suite passes 19 steps, 16 screenshots and zero issue groups, including actual repeated Gantt drag/save and four roles with five concurrent reloads each.
- Existing remaining browser suite passes full onboarding, admin fund/stakeholder CRUD and patent lifecycle; role-picker suite passes eight checks. Large SQL portfolio fixture returns all 153 rows.
- Parent inspected actual affected desktop/mobile screenshots. Independent read-only technical review approved with no must-fix findings, independently ran all 27 server/unit tests and type/lint/syntax checks, and inspected representative screenshots. A non-blocking test-assertion gap was strengthened and rerun without production-code changes.

Exact commands, boundaries and test setup corrections are in [dashboard/qa/hardening/verification.md](https://github.com/hosakb/bachelor-thesis/blob/fix/dashboard-hardening/dashboard/qa/hardening/verification.md).

## Screenshots

The markup shown below is an intentionally malicious-looking fictional test name rendered as literal text, not executed HTML.

![Literal Gantt text and contained popup, mobile](https://raw.githubusercontent.com/hosakb/bachelor-thesis/fix/dashboard-hardening/dashboard/qa/hardening/startup-390.png)
![Fund-role safe Gantt popup, desktop](https://raw.githubusercontent.com/hosakb/bachelor-thesis/fix/dashboard-hardening/dashboard/qa/hardening/fund-1440.png)

## Dependency and limitations

Stacked on modernization PR #3 with base `style/pr1-frontend-modernization`. ERP/tutorial PR #4 is a separate sibling and not part of this diff. PR #1 is already merged and is not recreated. No merge or deployment performed.

This is scoped hardening, not a full security audit. Existing dependency vulnerabilities, other HTML paths, general CSRF policy, database transactions and a production session store remain separate work. Production HTTPS/proxy/secret configuration requires a later approved operator change; this PR does not change those settings. All test data is fictional. No live PostgreSQL or Dynamics endpoint was used, and passing local tests are not a claim of green CI.
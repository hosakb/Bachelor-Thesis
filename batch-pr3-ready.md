## Summary

This pull request modernizes the existing dashboard presentation while keeping the established colors, page contents, charts/data, calculations, routes, permissions and feature set unchanged.

- Align cards, page sections, headers, forms and navigation consistently.
- Improve table spacing, headings, numeric alignment and responsive overflow behavior.
- Improve chart and Gantt axis/legend readability while preserving series colors and data.
- Fix overlapping onboarding cards and improve tablet/mobile layouts using local system fonts and the existing palette.
- Respect keyboard focus and reduced-motion preferences.

## Verification

The implementation report in `dashboard/qa/modernization/README.md` records 21/21 server tests, successful typecheck/lint, three passing browser suites and a 53-screen visual sweep at desktop, tablet and mobile widths. It reports zero overflow/unreachable-control pages, page errors or outside network requests after the changes. Actual before/after screenshots are in `dashboard/qa/modernization/before/` and `after/`.

Known trade-off: wide data tables remain horizontally scrollable inside their cards on narrow screens so words and dates do not break mid-cell. The report records the resulting count of controls initially outside the viewport.

## Dependency and review status

This branch is stacked on role-picker PR #2 (`feat/demo-role-picker`). PR #1 is already merged and is not recreated or changed. The reviewed final head is `08954c0366c1dd5aa5bce50a68725498addb9a15`; the independent technical and visual review described below supersedes the old pending-review status of `267cfb4`. This finished PR is ready for Ben's review. Review dependencies in order. No live database or ERP was contacted.

## Before/after screenshots

Startup overview, before:
![Startup overview before modernization](https://raw.githubusercontent.com/hosakb/bachelor-thesis/style/pr1-frontend-modernization/dashboard/qa/modernization/before/startup-overview-desktop.png)

Startup overview, after:
![Startup overview after modernization](https://raw.githubusercontent.com/hosakb/bachelor-thesis/style/pr1-frontend-modernization/dashboard/qa/modernization/after/startup-overview-desktop.png)

Gantt, before and after:
![Gantt before modernization](https://raw.githubusercontent.com/hosakb/bachelor-thesis/style/pr1-frontend-modernization/dashboard/qa/modernization/before/startup-gantt-year-desktop.png)
![Gantt after modernization](https://raw.githubusercontent.com/hosakb/bachelor-thesis/style/pr1-frontend-modernization/dashboard/qa/modernization/after/startup-gantt-year-desktop.png)

Mobile startup view:
![Startup overview after modernization at mobile width](https://raw.githubusercontent.com/hosakb/bachelor-thesis/style/pr1-frontend-modernization/dashboard/qa/modernization/after/startup-overview-mobile.png)


---

## Reviewed sidebar, Gantt and credential-login corrections

Published head: `08954c0366c1dd5aa5bce50a68725498addb9a15` on `style/pr1-frontend-modernization`. This updates existing PR #3 only; PR #1 and PR #2 branches are unchanged. Prior sections above are preserved as historical context; this section supersedes their pending-review status and 53-screen wording.

- Sidebar paints the full app-shell height while navigation stays sticky and reachable.
- Populated Gantt has zero top inset and an actually reachable horizontal timeline.
- Credential login has visible labels, autocomplete, responsive centering and full-width submit. Authentication and the protected demo role picker are unchanged.
- Bounded TRL-table scrolling fixes expanded-mobile-sidebar overflow; palette fidelity uses original tokens without changing series values, calculations or routes.

Independent regression and read-only visual review approved the exact source bytes: 108 source/test SHA256 entries were reverified by the publisher. Three independent final captures passed 159/159 cases each (53 distinct page/UI states x 3 viewports, 15 route URLs), with zero geometry/browser errors. The correction baseline reproduced 100 sidebar-gap cases, 33 Gantt-inset cases and 1 document-overflow case; final counts are zero in each category (categories overlap).

Upstream QA: all 10 regression/verification commands passed, including 21 server tests, local model/scraper contracts, typecheck/lint/format, three browser suites and supplemental visual capture. Publisher additionally reran 21/21 server tests, typecheck, lint, the 19-step E2E suite (zero issue groups), and 8 role-picker viewport checks (zero errors).

[Independent report](https://github.com/hosakb/bachelor-thesis/blob/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/REPORT.txt) | [Paired image index (download directory and open locally)](https://github.com/hosakb/bachelor-thesis/blob/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/index.html) | [Source hashes](https://github.com/hosakb/bachelor-thesis/blob/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/source-manifest.json) | [Raw upstream verification](https://github.com/hosakb/bachelor-thesis/blob/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/upstream-verification.txt)

Evidence includes 159 correction pairs and 51 original-baseline pairs. Correction-before uses frozen old CSS with current credential labels; it is not an untouched remote-head login comparison. The publisher repaired original-baseline portable filename collisions using unique state/viewport filenames and verified all 420 image references against source bytes.

### Reviewed correction screenshots

Credential login, mobile, before / after:
![Login before](https://raw.githubusercontent.com/hosakb/bachelor-thesis/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/images/pairs/before/login-mobile.png)
![Login after](https://raw.githubusercontent.com/hosakb/bachelor-thesis/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/images/pairs/after/login-mobile.png)

Gantt, desktop, before / after:
![Gantt before](https://raw.githubusercontent.com/hosakb/bachelor-thesis/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/images/pairs/before/startup-gantt-year-desktop.png)
![Gantt after](https://raw.githubusercontent.com/hosakb/bachelor-thesis/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/images/pairs/after/startup-gantt-year-desktop.png)

Expanded-navigation fund detail, mobile, after:
![Fund detail after](https://raw.githubusercontent.com/hosakb/bachelor-thesis/08954c0366c1dd5aa5bce50a68725498addb9a15/dashboard/qa/pr3-reviewed/images/pairs/after/fund-detail-nav-toggle-mobile.png)

Wide tables and Gantt deliberately scroll internally. Validation used fictional local data, not live ERP/database; not a cross-browser or exhaustive accessibility audit. PR is ready for review and remains unmerged. GitHub reports no configured checks; absence of checks is not CI green.

## Finished handoff, November 13

No additional modernization code or branch push was needed. Reverified all 108 committed source/test manifest entries against the exact reviewed head with zero mismatches, the saved 159-case matrix with zero defects/problems, and three committed remote PNG assets byte-for-byte. Existing regression suites were rerun during the separate follow-ups: server/model tests, lint/typecheck, the 19-step E2E suite, complete onboarding/patent/admin lifecycle checks and eight role-picker viewport checks passed. Actual current rendered desktop/mobile pages were inspected without changing the established design.

The permanent ERP demo/tutorial is separate PR #4, and scoped Gantt/input/session hardening is separate PR #5. Both have independent technical reviews and their own test/evidence reports. Neither changes this modernization branch or recreates PR #1. No merge, deployment or user-service restart occurred.
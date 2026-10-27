# Project notes

## Data freshness
- Card data (FRED) current through Q2 2026. Unemployment through Sep 2026.

## Decisions
- 2026-10-25: Saved each FRED series as its own raw file, because frequencies differ (quarterly vs monthly).

## Learnings
- Delinquency is a leading indicator of losses. Only part of it rolls to charge-off, about 2 quarters later.

## Lender Choice
- Affirm, Sezzle and Klarna
- 2026-10-26: BNPL composite uses Affirm, Sezzle and Klarna (public, mainly BNPL, report risk metrics).
- 2026-10-26: Each BNPL number is tagged US or Global, because Klarna reports some metrics only globally.
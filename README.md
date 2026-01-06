# Project Story — Why This Project Exists

Cricket analytics often rely on headline statistics such as total runs or batting average. While useful, those metrics alone fail to capture the full quality of T20 batting, where efficiency, consistency, and risk management are equally important.

This project answers a focused question:

Who was the best batsman of IPL 2025 when evaluated objectively using ball-by-ball data?

Rather than relying on reputation or subjective match impact, the analysis decomposes batting performance into first principles and evaluates players across multiple, transparent dimensions.

## Analytical Philosophy

Batting quality in T20 cricket is measured across four independent dimensions:

- **Scoring Efficiency:** How quickly a batsman converts balls into runs.
- **Aggression:** Ability to score boundaries without excessive stagnation.
- **Consistency of Scoring:** Control over dot balls and regular run contribution.
- **Sustainability:** Ability to score runs while preserving the wicket.

Each dimension is measured using metrics derived purely from ball-by-ball data, with no contextual or subjective adjustments.

## Methodology Overview

1. Parse raw IPL 2025 match data (Cricsheet YAML) using `Python`.
2. Engineer and validate match-level and ball-level datasets.
3. Build a clean star-schema data model in `Power BI`.
4. Create base and derived batting metrics using `DAX`.
5. Apply eligibility filters to avoid small-sample bias.
6. Normalise metrics using min–max scaling.
7. Combine normalised metrics into an equally weighted composite batting score.
8. Rank players using the reproducible scoring system.

No player names, teams, or outcomes are hard-coded in the logic.

## Key Outcome

The final deliverable is an objective ranking of IPL 2025 batsmen. The top-ranked player represents the best balance of:

- Run-scoring efficiency
- Boundary impact
- Consistency
- Wicket preservation

The methodology ensures no single metric dominates the result and that players are evaluated fairly across the season.

## Why This Project Matters

This project demonstrates:

- **End-to-end data ownership:** raw data → engineered datasets → insights.
- **Real-world data engineering:** handling schema inconsistencies and wicket events.
- **Power BI modelling discipline:** clean star schema and transparent DAX.
- **Interview-ready DAX patterns:** reproducible, explainable measures.
- **Analytical rigor:** evaluation beyond surface-level statistics.

The framework is adaptable to other seasons, leagues, or sports.

## Tools Used

- `Python` — YAML parsing and data engineering
- `Power BI Desktop` — modelling and reporting
- `DAX` — derived measures and scoring
- `GitHub` — version control
- Cricsheet IPL data — raw match source

## Notes

This project prioritises explainability and reproducibility rather than prediction or subjective impact analysis.
All assumptions and thresholds are explicitly documented.
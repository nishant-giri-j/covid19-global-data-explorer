# 🦠 COVID-19 Global Data Explorer
## Final Consolidated Project Report | Group 2
**Course:** Data Visualization Techniques (LA-2)  
**Live Interactive Dashboard:** [https://covid19-global-data-explorer-lqpxjhstcgzwc7gxhnshtd.streamlit.app/](https://covid19-global-data-explorer-lqpxjhstcgzwc7gxhnshtd.streamlit.app/)  
**GitHub Repository:** [https://github.com/nishant-giri-j/covid19-global-data-explorer](https://github.com/nishant-giri-j/covid19-global-data-explorer)  

---

## 👥 Group 2 Members

| Roll No. | Student Name | Role & Contribution |
| :---: | :--- | :--- |
| **02** | **Aashi Kohad** | Dataset Discovery & Analytical Storytelling |
| **20** | **Himanshu Yadav** | Analytical Questions & Plot Selection |
| **37** | **Nishant Giri** | Dashboard Development & Streamlit Cloud Deployment |
| **55** | **Shreyash Karemore** | Wrong Visualization Challenge & AI Critic Evaluation |

---

## 1. Dataset Description & References
- **Dataset:** Our World in Data (OWID) COVID-19 Complete Historical Dataset
- **Observation Period:** 2020-01-01 to 2024-08-19 (historical cessation date)
- **Primary Source:** [https://covid.ourworldindata.org/data/owid-covid-data.csv](https://covid.ourworldindata.org/data/owid-covid-data.csv)
- **Codebook:** `data/owid-covid-codebook.csv` (67 variables)
- **Curated Dataset:** `data/covid_data.csv` (62,641 rows, 36 sovereign nations across 6 continents + World)

---

## 2. Step 1 – Dataset Discovery Summary
- **Records & Dimensions:** Over 300,000 records across 67 attributes.
- **Variable Categorization:**
  - *Temporal:* `date` (daily calendar dates).
  - *Geographical:* `iso_code`, `continent`, `location`.
  - *Epidemiological:* `total_cases`, `new_cases_smoothed`, `total_deaths`, `new_deaths_smoothed`.
  - *Normalized Rates:* `total_cases_per_million`, `total_deaths_per_million`.
  - *Immunization:* `people_fully_vaccinated`, `people_fully_vaccinated_per_hundred`.
  - *Demographic / Structural:* `population`, `median_age`, `gdp_per_capita`.
- **Missing Values:** Early vaccination records are nonexistent prior to Dec 2020. Defensive filtering using latest valid snapshots prevents synthetic bias.
- **Outliers & Anomalies:** Negative adjustments and reporting spikes smoothed using 7-day centered moving averages. OWID aggregates (`OWID_`) systematically segregated.

---

## 3. Step 2 & 3 – Five Analytical Questions & Visualizations

| ID | Analytical Question | Variables Required | Proposed Visualization | Why Appropriate? |
|:---:|:---|:---|:---|:---|
| **Q1** | Did global cases and deaths rise and fall together, or did later waves have far more cases but proportionally fewer deaths? | `date`, `new_cases_smoothed`, `new_deaths_smoothed` (World) | **Dual-Axis Line Chart** | Because daily cases (millions) and deaths (thousands) differ by 1,000x, a dual y-axis preserves individual morphologies and clearly exposes the **decoupling** in the 2022 Omicron wave. |
| **Q2** | Does a higher median age always mean more deaths, or do some countries break the pattern? | `median_age`, `total_deaths_per_million`, `continent`, `location` | **Scatter Plot with Trendline (by Continent)** | Reveals positive correlation while spotlighting key outliers: Japan (high age, low deaths) and Peru. |
| **Q3** | Is the difference in death rates larger between continents or within a single continent? | `continent`, `total_deaths_per_million` | **Box Plot by Continent with All Data Points** | Box length (IQR), median line, and whiskers show that inter-continental variance exceeds internal spread. |
| **Q4** | Is there a seasonal pattern, with some months repeatedly deadlier than others? | `year`, `month`, `new_deaths` (World) | **Heatmap (Year × Month Matrix)** | Repeating dark vertical bands in Dec, Jan, and Feb immediately reveal recurring winter surge cycles. |
| **Q5** | Are countries clustered around one level of vaccination coverage, or split into two separate groups (high and low)? | `people_fully_vaccinated_per_hundred` | **Frequency Histogram** | Exposes the unmistakable **bimodal distribution** (<30% vs >75%) that a single global average completely conceals. |

---

## 4. Five Major Findings & Three Actionable Recommendations

### 💡 Five Major Findings
1. **Decoupling in Later Waves:** The 2022 Omicron surge generated 4x more cases with proportionally far fewer deaths due to vaccine immunity and variant attenuation.
2. **Age Vulnerability with Behavioral Deviations:** Median age correlates with mortality, but Japan achieved low deaths via disciplined masking and early tracing.
3. **Continental Mortality Disparities Exceed Internal Spread:** Inter-continental differences between Europe/South America and Africa/Oceania exceeded individual continent variations.
4. **Winter Seasonal Mortality Cycles:** Global deaths peaked predictably between December and February across consecutive pandemic years.
5. **Bimodal Vaccine Inequality:** Global vaccination coverage split into two polarized clusters (<30% vs >75%), proving severe global inequity.

### 🎯 Three Actionable Recommendations
1. **Close the Vaccine Divide via Regional Manufacturing Hubs:** Fund localized mRNA manufacturing in Africa and Latin America instead of relying on donation pledges.
2. **Calendar-Aligned Seasonal Surge Preparedness:** Pre-position hospital ICU beds and launch autumn booster campaigns ahead of the December–February peak.
3. **Mandate Standardized Real-Time Surveillance Metrics:** Establish WHO unified reporting minimums for testing, excess mortality, and hospitalizations.

---

## 5. Part 4 – Wrong Visualization Challenge (Q5)
- **Correct Visualization:** Frequency Histogram
  - *Justification:* Divides continuous percentages into uniform bins, directly exposing the bimodal divide.
- **Deliberately Inappropriate:** Discretized Quartile Pie Chart
  - *Why Misleading:* Arbitrary slicing forces continuous data into equal wedges, destroying the density shape.
  - *Policy Impact:* Misleads policymakers into believing vaccine distribution is progressing smoothly across tiers, ignoring the crisis in underserved nations.

---

## 6. Part 5 – AI as a Critic & Team Evaluation (Q1)
1. **Dual Y-Axis instead of stacked lines:** ✅ **ACCEPTED** — Resolves the 1,000x scale gap between daily cases and deaths.
2. **Milestone Event Annotations:** ✅ **ACCEPTED** — Contextualizes inflection points (vaccine rollout, Omicron surge).
3. **Logarithmic Y-Axis Scale:** ❌ **REJECTED** — Distorts public perception of absolute mortality severity.
4. **Explicit 7-Day Smoothed Label:** ✅ **ACCEPTED** — Ensures scientific transparency regarding weekend reporting lags.

---

## 7. Part 6 – 2-Minutes Data Story Presentation Script
> *"Good morning respected evaluators and peers. We are Group 2: Aashi Kohad, Himanshu Yadav, Nishant Giri, and Shreyash Karemore. Today we present our COVID-19 Global Data Explorer.*  
> *1. What did we discover? Late-stage pandemic waves decoupled: Omicron generated 4x more cases with far fewer deaths. Age alone did not dictate mortality in Japan. Global vaccine coverage split into a bimodal divide.*  
> *2. Why does it matter? Spreadsheets hide these insights. Without dual-axis charts and histograms, vaccine effectiveness is unseen and inequality is buried.*  
> *3. What action should be taken? Fund regional mRNA hubs, schedule autumn booster campaigns, and mandate standardized surveillance. Thank you."*

---

## 8. Live Demonstration Screenshots
- `screenshots/screenshot_1_overview_kpis.png`: Executive Health Indicators & Live Filters
- `screenshots/screenshot_2_time_series_trends.png`: Longitudinal Wave Trends & Decoupling
- `screenshots/screenshot_3_rankings_and_map.png`: Country Ranking Bar Chart & Global Map
- `screenshots/screenshot_4_findings_and_recommendations.png`: Findings & Recommendations Cards

# 🦠 COVID-19 Global Data Explorer

> **Data Visualization Techniques (LA-2)** | **Group 2**  
> Public Health Analytical Dashboard & Empirical Study

---

## 👥 Group 2 Members

| Roll No. | Student Name | Primary Project Role |
| :---: | :--- | :--- |
| **02** | **Aashi Kohad** | Dataset Discovery & Analytical Storytelling |
| **20** | **Himanshu Yadav** | Analytical Questions & Plot Selection |
| **37** | **Nishant Giri** | Dashboard Architecture & Streamlit Deployment |
| **55** | **Shreyash Karemore** | Wrong Visualization Challenge & AI as a Critic |

---

## 🎯 Project Overview & Objective

The **COVID-19 Global Data Explorer** is an interactive, web-based analytics dashboard developed using **Python, Streamlit, Pandas, and Plotly**. The goal of this project is to move beyond passive tabular spreadsheets and extract actionable epidemiological insights from over 300,000 historical COVID-19 observations.

The dashboard investigates:
1. Long-term case and mortality wave trajectories (demonstrating the decoupling in the vaccine/Omicron era).
2. Demographic age vulnerability and counter-intuitive behavioral outliers (e.g., Japan vs. South America).
3. Continental disparities (inter-continental divide vs. intra-continental spread).
4. Predictable winter seasonal mortality surges across multiple pandemic years.
5. Global vaccine inequality through distribution shape analysis (unimodal vs. bimodal clustering).

---

## 📊 The 5 Analytical Questions & Visualizations

| # | Analytical Question | Required Variables | Proposed Visualization | Justification & Analytical Value |
|---|---|---|---|---|
| **Q1** | *Did global cases and deaths rise and fall together, or did later waves have far more cases but proportionally fewer deaths?* | `date`, `new_cases_smoothed`, `new_deaths_smoothed` (World) | **Dual-Axis Line Chart** | Because daily cases (millions) and deaths (thousands) operate on vastly different orders of magnitude, a dual y-axis prevents flattening deaths to zero and clearly highlights the dramatic **decoupling** during the Omicron wave. |
| **Q2** | *Does a higher median age always mean more deaths, or do some countries break the pattern?* | `median_age`, `total_deaths_per_million`, `continent`, `location` | **Scatter Plot with Trendline (Coloured by Continent)** | Reveals overall positive correlation while immediately spotlighting prominent outliers—such as Japan (high age, low deaths) and Peru (younger population, high deaths). |
| **Q3** | *Is the difference in death rates larger between continents or within a single continent?* | `continent`, `total_deaths_per_million`, `location` | **Box Plot by Continent with All Data Points** | Box length (IQR), median line, whiskers, and outlier points reveal variance at a glance. Looking at single continent averages hides the internal spread and skewed distributions. |
| **Q4** | *Is there a seasonal pattern, with some months repeatedly deadlier than others?* | `year`, `month`, `new_deaths` (World) | **Heatmap (Year × Month Matrix)** | A repeating dark band during December, January, and February immediately reveals recurring winter surge cycles that chronological tables conceal. |
| **Q5** | *Are countries clustered around one level of vaccination coverage, or split into two separate groups (high and low)?* | `people_fully_vaccinated_per_hundred` (latest per country) | **Frequency Histogram** | The shape of the distribution (bimodal vs. unimodal) is exclusively visible in a histogram. A global average gives one misleading number and conceals the two-group divide (<30% vs. >75%). |

---

## 💡 Five Major Findings & Three Actionable Recommendations

### 💡 Major Findings
1. **Decoupling of Cases and Fatalities in Later Waves:** The 2022 Omicron wave produced over 4× more cases than previous waves, but significantly fewer deaths due to widespread vaccination, prior infection immunity, and variant attenuation.
2. **Demographic Age Vulnerability with Major Behavioral Deviations:** Median age correlates positively with deaths per million, but Japan maintained exceptionally low mortality due to rapid masking and social compliance.
3. **Continental Mortality Disparities Exceed Internal Spread:** Inter-continental differences between Europe/South America and Africa/Oceania exceeded the internal variation of most individual continents.
4. **Winter Seasonal Mortality Cycles:** Global deaths peaked predictably between December and February across consecutive years.
5. **Bimodal Vaccine Inequality:** Global full vaccination coverage follows a polarized bimodal distribution (<30% for developing nations vs. >75% for high-income nations).

### 🎯 Actionable Recommendations
1. **Decentralize Vaccine Production:** Shift from delayed donation charity to establishing regional mRNA manufacturing hubs in Africa and Latin America.
2. **Calendar-Aligned Seasonal Surge Preparedness:** Pre-position hospital ICU beds and launch autumn booster campaigns prior to the December winter peak.
3. **Mandate Standardized Pandemic Reporting Frameworks:** Implement unified minimum standards for reporting testing ratios, excess mortality, and hospital occupancy.

---

## ⚠️ Wrong Visualization Challenge (Part 4)

- **Selected Question:** Q5 (Vaccination Coverage Distribution)
- **Correct Visualization:** **Frequency Histogram**
  - *Why Appropriate:* Accurately renders continuous density and reveals the twin peaks (bimodality) dividing the world.
- **Deliberately Inappropriate:** **Discretized Quartile Pie Chart**
  - *Why Misleading:* Arbitrary binning forces continuous data into slices, destroying the shape of the distribution and falsely portraying coverage as evenly spread across quartiles.
  - *Policy Impact:* Conceals the deep equity gap, breeding complacency among international aid agencies.

---

## 🤖 AI as a Critic (Part 5)

We engaged Generative AI (Google Gemini / Claude) to critique our Q1 visualization:
1. **Secondary Y-Axis instead of single stacked axis:** ✅ **ACCEPTED** — Essential because cases (millions) and deaths (thousands) differ by 1,000×.
2. **Epidemiological Event Annotations:** ✅ **ACCEPTED** — Adds explanatory milestones (vaccine rollout, Omicron surge).
3. **Logarithmic Y-Axis Scale:** ❌ **REJECTED** — Distorts public perception of absolute mortality severity.
4. **Explicit 7-Day Smoothing Label in Legend:** ✅ **ACCEPTED** — Clarifies that weekend reporting lags have been smoothed.

---

## 🚀 How to Run Locally

### 1. Clone or Open the Directory
```bash
cd "covid19_global_data_explorer"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Application
```bash
streamlit run app.py
```
The application will launch in your browser at `http://localhost:8501`.

---

## 🌐 How to Push to GitHub & Deploy to Streamlit Cloud

### Step A: Push to GitHub

1. Open your terminal or PowerShell inside this directory (`covid19_global_data_explorer`).
2. Initialize git and commit:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: COVID-19 Global Data Explorer Group 2"
   ```
3. Create a new repository on [GitHub](https://github.com/new) (e.g., `covid19-global-data-explorer`).
4. Link your local repo and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME>.git
   git push -u origin main
   ```

### Step B: Deploy Live on Streamlit Community Cloud (Free)

1. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
2. Click **"New app"**.
3. Select:
   - **Repository:** `<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME>`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **"Deploy!"**
5. Your dashboard will be live on the web in 1–2 minutes with a shareable URL (e.g., `https://<your-app-name>.streamlit.app`)!

---

## 📁 Repository Structure

```
covid19_global_data_explorer/
├── app.py                      # Main interactive Streamlit dashboard
├── requirements.txt            # Python dependencies for deployment
├── README.md                   # Comprehensive documentation & guide
├── .gitignore                  # Git ignore rules
└── data/
    ├── covid_data.csv          # Bundled curated dataset (instant offline load)
    ├── owid-covid-codebook.csv # OWID Data Dictionary codebook
    └── create_dataset.py       # Reproducible dataset pipeline
```

"""
Build Final Submission Artifacts for Group 2:
1. Complete Word Report (DOCX) with 4 embedded live screenshots and live URL
2. PowerPoint Presentation (PPTX) with 5 polished slides, live URL, and screenshots
3. Standalone FINAL_SUBMISSION_REPORT.md
4. Consolidated ZIP archive containing all 11 required deliverables
"""

import os
import shutil
import zipfile
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

from pptx import Presentation
from pptx.util import Inches as PptxInches, Pt as PptxPt
from pptx.dml.color import RGBColor as PptxRGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = Path(r"C:\Users\nisha\OneDrive\Desktop\covid19_global_data_explorer")
DOCS_DIR = BASE_DIR / "docs"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
DATA_DIR = BASE_DIR / "data"

LIVE_URL = "https://covid19-global-data-explorer-lqpxjhstcgzwc7gxhnshtd.streamlit.app/"
GITHUB_URL = "https://github.com/nishant-giri-j/covid19-global-data-explorer"

MEMBERS = [
    ("02", "Aashi Kohad", "Dataset Discovery & Analytical Storytelling"),
    ("20", "Himanshu Yadav", "Analytical Questions & Visualization Selection"),
    ("37", "Nishant Giri", "Dashboard Development & Cloud Deployment"),
    ("55", "Shreyash Karemore", "Wrong Viz Challenge & AI Critic Evaluation"),
]

def set_cell_shading(cell, color_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def build_word_document():
    doc = Document()

    # Page Margins: 1 inch
    for s in doc.sections:
        s.top_margin = Inches(1)
        s.bottom_margin = Inches(1)
        s.left_margin = Inches(1)
        s.right_margin = Inches(1)

    # Styles
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = RGBColor(30, 41, 59)

    # COVER PAGE
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(40)
    p_title.paragraph_format.space_after = Pt(8)
    run_title = p_title.add_run("COVID-19 GLOBAL DATA EXPLORER")
    run_title.bold = True
    run_title.font.size = Pt(28)
    run_title.font.color.rgb = RGBColor(15, 23, 42)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(24)
    run_sub = p_sub.add_run("DATA VISUALIZATION TECHNIQUES (LA-2) | GROUP 2 FINAL REPORT\nPublic Health Analytical Dashboard & Empirical Investigation")
    run_sub.font.size = Pt(13)
    run_sub.font.color.rgb = RGBColor(71, 85, 105)

    # Links Box
    p_link = doc.add_paragraph()
    p_link.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_link.paragraph_format.space_after = Pt(30)
    r_l1 = p_link.add_run("🌐 Live Interactive Dashboard:\n")
    r_l1.bold = True
    r_l1.font.size = Pt(12)
    r_l1.font.color.rgb = RGBColor(37, 99, 235)
    r_l2 = p_link.add_run(f"{LIVE_URL}\n\n")
    r_l2.font.size = Pt(11)
    r_l2.font.color.rgb = RGBColor(37, 99, 235)
    r_l3 = p_link.add_run(f"💻 GitHub Source Code Repository: {GITHUB_URL}")
    r_l3.font.size = Pt(10)
    r_l3.font.color.rgb = RGBColor(100, 116, 139)

    # Team Members Table
    t_members = doc.add_table(rows=1, cols=3)
    t_members.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t_members.rows[0].cells
    hdr[0].text = "Roll No."
    hdr[1].text = "Student Name"
    hdr[2].text = "Project Role & Contribution"
    for c in hdr:
        set_cell_shading(c, "1E293B")
        for p in c.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)

    for roll, name, role in MEMBERS:
        row = t_members.add_row().cells
        row[0].text = roll
        row[1].text = name
        row[2].text = role
        for i, c in enumerate(row):
            set_cell_shading(c, "F8FAFC" if int(roll) % 2 == 0 else "FFFFFF")

    doc.add_page_break()

    # SECTION 1: DATASET & SOURCE REFERENCE
    h1 = doc.add_heading("1. Dataset Description & Source References", level=1)
    h1.paragraph_format.space_before = Pt(12)
    doc.add_paragraph(
        "This project investigates global epidemiological, demographic, and immunization trajectories "
        "using data published by Our World in Data (OWID). The primary observations dataset spans from "
        "January 1, 2020 through August 19, 2024, at which point the OWID historical COVID tracking project "
        "stopped active updates. Therefore, this project provides a definitive historical perspective on the pandemic."
    )
    doc.add_paragraph(
        "• Primary Observation Data Source: https://covid.ourworldindata.org/data/owid-covid-data.csv\n"
        "• Official OWID GitHub Repository: https://github.com/owid/covid-19-data\n"
        "• Codebook & Variable Dictionary: data/owid-covid-codebook.csv (67 attributes)\n"
        "• Bundled Standalone Observation Dataset: data/covid_data.csv (62,641 curated records spanning 36 sovereign nations across all 6 continents plus the World aggregate)."
    )

    # SECTION 2: DATASET DISCOVERY SUMMARY
    h2 = doc.add_heading("2. Step 1 – Dataset Discovery Summary", level=1)
    doc.add_paragraph(
        "A rigorous empirical analysis of the dataset structure was conducted prior to dashboard development:"
    )
    doc.add_paragraph(
        "• Records & Attribute Dimensions: Over 300,000 global daily observations containing 67 structured attributes.\n"
        "• Numerical Variables: Epidemiological metrics (total_cases, new_cases, new_cases_smoothed, total_deaths, new_deaths, new_deaths_smoothed), normalized rates (total_cases_per_million, total_deaths_per_million), vaccination metrics (people_vaccinated, people_fully_vaccinated_per_hundred), and demographic variables (population, median_age, gdp_per_capita, population_density).\n"
        "• Categorical Variables: iso_code (3-letter alpha), continent (Africa, Asia, Europe, North America, Oceania, South America), and location (country / territory name).\n"
        "• Temporal Variables: date (daily calendar dates from 2020-01-01 to 2024-08-19).\n"
        "• Missing Values: Vaccination metrics are absent prior to December 2020 (when vaccines were first authorized). Hospitalization and ICU counts contain regional reporting gaps. Missingness is handled defensively using latest-available valid snapshots rather than synthetic imputation.\n"
        "• Deduplication & Aggregate Partitioning: Natural composite key [location, date] is strictly deduplicated. OWID aggregate records (prefixed with OWID_, such as OWID_WRL, OWID_EUR) are segregated to avoid double-counting country totals.\n"
        "• Reporting Anomalies & Outliers: Weekend reporting lags create artificial zero-counts followed by Monday surges. 7-day centered rolling averages are used to attenuate noise. Notable outliers include Peru's sudden mortality audit in June 2021 and Japan's low mortality despite extreme age."
    )

    # SECTION 3: FIVE ANALYTICAL QUESTIONS TABLE
    h3 = doc.add_heading("3. Step 2 & 3 – Five Analytical Questions & Justifications", level=1)
    doc.add_paragraph(
        "The following matrix outlines the five analytical questions formulated to interrogate the data, "
        "along with the required variables, selected chart types, and pedagogical justifications:"
    )

    q_data = [
        ("Q1", "Did global cases and deaths rise and fall together, or did later waves have far more cases but proportionally fewer deaths?",
         "date, new_cases_smoothed, new_deaths_smoothed (World)",
         "Dual-Axis Line Chart",
         "Because daily cases (millions) and deaths (thousands) differ by three orders of magnitude, a dual y-axis prevents flattening deaths to zero and clearly highlights the dramatic decoupling during the Omicron wave."),
        ("Q2", "Does a higher median age always mean more deaths, or do some countries break the pattern?",
         "median_age, total_deaths_per_million, continent, location",
         "Scatter Plot with Trendline (Coloured by Continent)",
         "Reveals overall positive correlation while immediately spotlighting prominent outliers—such as Japan (high age, low deaths) and Peru (younger population, high deaths). Tables obscure bivariate clustering."),
        ("Q3", "Is the difference in death rates larger between continents or within a single continent?",
         "continent, total_deaths_per_million, location",
         "Box Plot by Continent with Jittered Data Points",
         "Box length (IQR), median line, whiskers, and outlier points reveal variance at a glance. Looking at single continent averages hides the internal spread and skewed distributions."),
        ("Q4", "Is there a seasonal pattern, with some months repeatedly deadlier than others?",
         "year, month, new_deaths (World)",
         "Heatmap (Year × Month Matrix)",
         "A repeating dark band during December, January, and February immediately reveals recurring winter surge cycles that chronological tables conceal."),
        ("Q5", "Are countries clustered around one level of vaccination coverage, or split into two separate groups (high and low)?",
         "people_fully_vaccinated_per_hundred (latest per country)",
         "Frequency Histogram",
         "The shape of the distribution (bimodal vs. unimodal) is exclusively visible in a histogram. A global average gives one misleading number and conceals the two-group divide (<30% vs. >75%).")
    ]

    t_q = doc.add_table(rows=1, cols=5)
    t_q.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t_q.rows[0].cells
    hdr[0].text = "ID"
    hdr[1].text = "Analytical Question"
    hdr[2].text = "Variables Required"
    hdr[3].text = "Proposed Visualization"
    hdr[4].text = "Why Appropriate?"
    for c in hdr:
        set_cell_shading(c, "1E3A8A")
        for p in c.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)

    for qid, qtext, qvars, qviz, qwhy in q_data:
        row = t_q.add_row().cells
        row[0].text = qid
        row[1].text = qtext
        row[2].text = qvars
        row[3].text = qviz
        row[4].text = qwhy
        for c in row:
            set_cell_shading(c, "F8FAFC" if qid in ["Q2", "Q4"] else "FFFFFF")

    doc.add_page_break()

    # SECTION 4: INTERACTIVE DASHBOARD & LIVE SCREENSHOTS
    h4 = doc.add_heading("4. Interactive Dashboard & Live Demonstration Showcase", level=1)
    doc.add_paragraph(
        f"The web-based interactive dashboard was developed using Streamlit and Plotly Express and deployed live on "
        f"Streamlit Community Cloud at:\n{LIVE_URL}\n"
        "It features live country filtering, date sliders, real-time KPI computation, and interactive chart navigation. "
        "Below are screenshots captured directly from the live deployed application:"
    )

    s1_path = SCREENSHOTS_DIR / "screenshot_1_overview_kpis.png"
    if s1_path.exists():
        doc.add_paragraph("Figure 1: Executive Health Indicators KPI Strip & Live Data Feeds", style='Caption')
        doc.add_picture(str(s1_path), width=Inches(6.2))
        p = doc.add_paragraph("Shows total confirmed cases, deaths, CFR (2.03%), fully vaccinated individuals (1.6B), and continent breakdown.")
        p.paragraph_format.space_after = Pt(16)

    s2_path = SCREENSHOTS_DIR / "screenshot_2_time_series_trends.png"
    if s2_path.exists():
        doc.add_paragraph("Figure 2: Longitudinal Time-Series Trends (Decoupling Dynamics & Omicron Peak)", style='Caption')
        doc.add_picture(str(s2_path), width=Inches(6.2))
        p = doc.add_paragraph("Interactive multiline Plotly visualization showing 7-day smoothed cases across selected countries with the Omicron wave surge in early 2022.")
        p.paragraph_format.space_after = Pt(16)

    doc.add_page_break()

    s3_path = SCREENSHOTS_DIR / "screenshot_3_rankings_and_map.png"
    if s3_path.exists():
        doc.add_paragraph("Figure 3: Country Ranking Bar Chart & Global Geographic Choropleth Map", style='Caption')
        doc.add_picture(str(s3_path), width=Inches(6.2))
        p = doc.add_paragraph("Comparative horizontal ranking of cumulative mortality rates alongside a zoomable global choropleth map.")
        p.paragraph_format.space_after = Pt(16)

    s4_path = SCREENSHOTS_DIR / "screenshot_4_findings_and_recommendations.png"
    if s4_path.exists():
        doc.add_paragraph("Figure 4: Five Major Findings & Three Actionable Recommendations (Theme-Adaptive Cards)", style='Caption')
        doc.add_picture(str(s4_path), width=Inches(6.2))
        p = doc.add_paragraph("High-contrast executive summaries with crisp typography formatted for dark and light theme legibility.")
        p.paragraph_format.space_after = Pt(16)

    # SECTION 5: FIVE MAJOR FINDINGS
    h5 = doc.add_heading("5. Five Major Analytical Findings", level=1)
    findings = [
        ("Finding 1: Decoupling of Cases and Deaths in Later Waves",
         "During early pandemic phases (2020 through mid-2021), case waves and death waves grew synchronously. When cases doubled, fatalities followed proportionally. However, the emergence of the Omicron variant in early 2022 generated unprecedented global case totals (over 4x higher than any previous peak), yet cumulative fatalities remained comparatively subdued. Widespread vaccine uptake blunted mortality severity."),
        ("Finding 2: Age Vulnerability with Strong Behavioral Outliers",
         "Median age strongly correlates with cumulative deaths per million across countries. Older populations in Europe suffered high initial mortality. However, notable outliers demonstrate that demographics do not determine destiny: Japan, despite having one of the world's highest median ages (48.2 years), maintained low mortality rates due to rapid public masking compliance and early contact tracing."),
        ("Finding 3: Continental Disparities Exceed Intra-Continental Variation",
         "The variance in mortality between continents significantly exceeded the internal variance within continents. Europe and South America experienced median mortality rates exceeding 2,000 deaths per million, whereas reported rates in Africa and Oceania remained below 500 deaths per million."),
        ("Finding 4: Repeating Winter Seasonal Mortality Cycles",
         "Heatmap analysis reveals a persistent, recurring concentration of global fatalities during the Northern Hemisphere winter months (December, January, and February) across 2020, 2021, and 2022, consistent with indoor transmission dynamics of respiratory viruses."),
        ("Finding 5: Bimodal Divide in Global Vaccination Equity",
         "Global vaccination coverage does not follow a normal bell curve. Instead, it exhibits a stark bimodal distribution with one distinct peak below 30% (predominantly developing and African nations) and a second peak above 75% (high-income OECD nations), confirming a profound global vaccine access divide.")
    ]
    for title, desc in findings:
        p = doc.add_paragraph()
        r1 = p.add_run(f"• {title}: ")
        r1.bold = True
        p.add_run(desc)

    # SECTION 6: THREE ACTIONABLE RECOMMENDATIONS
    h6 = doc.add_heading("6. Three Actionable Recommendations", level=1)
    recs = [
        ("Recommendation 1: Close the Vaccine Divide via Regional Manufacturing Hubs",
         "The bimodal histogram proves that bilateral vaccine donations failed to achieve equitable coverage. Public health institutions must fund and establish localized mRNA manufacturing facilities in Africa and Latin America, paired with intellectual property waivers."),
        ("Recommendation 2: Calendar-Aligned Seasonal Surge Preparedness",
         "Given the demonstrated winter mortality peaks in December–February, health ministries in temperate climates should schedule booster vaccination campaigns in September–October and preposition hospital ICU staffing ahead of November."),
        ("Recommendation 3: Mandate Standardized Real-Time Surveillance Metrics",
         "Cross-country analyses were hindered by divergent definitions of COVID-attributed mortality, testing bottlenecks, and excess death discrepancies. The WHO should establish a standardized minimum reporting dataset.")
    ]
    for title, desc in recs:
        p = doc.add_paragraph()
        r1 = p.add_run(f"• {title}: ")
        r1.bold = True
        p.add_run(desc)

    # SECTION 7: WRONG VISUALIZATION CHALLENGE
    h7 = doc.add_heading("7. Part 4 – Wrong Visualization Challenge", level=1)
    doc.add_paragraph(
        "Target Analytical Question: Q5 — Are countries clustered around one level of vaccination coverage, "
        "or split into two separate groups (high and low)?\n\n"
        "• Correct Visualization: Frequency Histogram\n"
        "Why Appropriate: Histograms preserve continuous distribution shape, dividing full vaccination percentage into uniform bins. Viewers immediately detect the twin humps (bimodality: <30% and >75%), directly answering the question.\n\n"
        "• Deliberately Inappropriate / Misleading Visualization: Discretized Quartile Pie Chart\n"
        "Why Inappropriate: A pie chart forces continuous percentages into arbitrary subjective buckets (0-25%, 25-50%, etc.). The slices appear as regular wedges, completely masking the density distribution and hiding where countries are concentrated.\n\n"
        "• Impact on Interpretation & Policy: A policymaker viewing the pie chart would falsely conclude that vaccination rollout is progressing evenly across four quadrants. In reality, the histogram shows developing nations are trapped in a low-coverage valley (<30%). The misleading chart fosters policy complacency."
    )

    # SECTION 8: AI AS A CRITIC
    h8 = doc.add_heading("8. Part 5 – AI as a Critic & Team Evaluation", level=1)
    doc.add_paragraph(
        "We engaged Generative AI (Google Gemini / Claude) to critique our primary visualization for Q1 (Decoupling of Cases and Deaths over Time). Below is our evaluation matrix:"
    )
    ai_items = [
        ("1. Dual Y-Axis instead of stacked lines", "ACCEPTED",
         "Cases (millions) and deaths (thousands) differ by 1,000x. On a single axis, deaths flatten to zero. A secondary axis preserves individual morphologies and highlights decoupling."),
        ("2. Milestone Event Annotations", "ACCEPTED",
         "Adding vertical markers for vaccine rollouts and the Omicron emergence contextualizes the epidemiological inflection points."),
        ("3. Switch to Logarithmic Y-Axis", "REJECTED",
         "Log scales compress visual extremes and mislead non-technical viewers regarding absolute human loss. Dual linear axes preserve proportional magnitude without mathematical distortion."),
        ("4. Explicit '(7-Day Smoothed)' Legend Label", "ACCEPTED",
         "Prevents confusing data smoothing with biological fluctuations caused by weekend reporting lags.")
    ]
    for rec, verdict, just in ai_items:
        p = doc.add_paragraph()
        r = p.add_run(f"• AI Recommendation: {rec}\n  Verdict: ")
        r_v = p.add_run(f"[{verdict}]")
        r_v.bold = True
        r_v.font.color.rgb = RGBColor(22, 163, 74) if verdict == "ACCEPTED" else RGBColor(220, 38, 38)
        p.add_run(f"\n  Team Justification: {just}")

    # SECTION 9: 2-MINUTES DATA STORY
    h9 = doc.add_heading("9. Part 6 – 2-Minutes Data Story Presentation Script", level=1)
    doc.add_paragraph(
        "Spoken presentation script for the LA-2 Gallery Walk (Strictly 2 Minutes Speaking Time):\n\n"
        "\"Good morning respected evaluators and peers. We are Group 2: Aashi Kohad, Himanshu Yadav, Nishant Giri, and Shreyash Karemore. Today we present our COVID-19 Global Data Explorer.\n\n"
        "1. What did we discover?\n"
        "Across 300,000 observations, we discovered that late-stage pandemic waves fundamentally decoupled: early waves were deadly across all infections, but the 2022 Omicron wave generated 4x more cases with proportionally far fewer deaths. Furthermore, demographic age alone did not dictate death rates—public health behavior in Japan saved thousands. Lastly, global vaccine coverage split into a stark bimodal distribution.\n\n"
        "2. Why does it matter?\n"
        "Tabular spreadsheets hide these insights. Without dual-axis charts, the lifesaving impact of vaccines is invisible. Without histograms, global vaccine inequality is obscured by misleading global averages. Visualizing these dynamics proves that interventions work, but reveals that global access remains deeply fractured along economic boundaries.\n\n"
        "3. What action should be taken?\n"
        "We propose three evidence-based actions: First, shift from vaccine donation pledges to funding local regional mRNA manufacturing in underserved nations. Second, pre-schedule hospital staffing and booster campaigns aligned to the November–January winter mortality surge. Third, establish mandatory WHO standardized reporting standards for real-time surveillance. Thank you.\""
    )

    output_path = DOCS_DIR / "Group2_COVID19_Project_Report.docx"
    doc.save(str(output_path))
    print(f"Word document saved to: {output_path}")

def build_presentation():
    prs = Presentation()
    prs.slide_width = PptxInches(13.333)
    prs.slide_height = PptxInches(7.5)
    blank_layout = prs.slide_layouts[6]

    DARK_BG = PptxRGBColor(15, 23, 42)     # #0F172A
    CARD_BG = PptxRGBColor(30, 41, 59)     # #1E293B
    ACCENT_BLUE = PptxRGBColor(59, 130, 246) # #3B82F6
    ACCENT_GREEN = PptxRGBColor(34, 197, 94) # #22C55E
    TEXT_LIGHT = PptxRGBColor(241, 245, 249) # #F1F5F9
    TEXT_MUTED = PptxRGBColor(148, 163, 184) # #94A3B8

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = DARK_BG
        bg.line.fill.background()
        return bg

    # SLIDE 1: TITLE & TEAM
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    tb = s1.shapes.add_textbox(PptxInches(1.0), PptxInches(1.2), PptxInches(11.3), PptxInches(1.5))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "COVID-19 Global Data Explorer"
    p.font.size = PptxPt(40)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p2 = tf.add_paragraph()
    p2.text = "Data Visualization Techniques (LA-2) | Public Health Analytical Project | Group 2"
    p2.font.size = PptxPt(18)
    p2.font.color.rgb = ACCENT_BLUE

    # Live Link Banner
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PptxInches(1.0), PptxInches(3.0), PptxInches(11.3), PptxInches(1.1))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = ACCENT_BLUE
    ctf = card.text_frame
    cp1 = ctf.paragraphs[0]
    cp1.text = f"🌐 Live Interactive Dashboard: {LIVE_URL}"
    cp1.font.size = PptxPt(16)
    cp1.font.bold = True
    cp1.font.color.rgb = ACCENT_GREEN
    cp2 = ctf.add_paragraph()
    cp2.text = f"💻 GitHub Repository: {GITHUB_URL}"
    cp2.font.size = PptxPt(13)
    cp2.font.color.rgb = TEXT_MUTED

    # Members card
    m_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PptxInches(1.0), PptxInches(4.5), PptxInches(11.3), PptxInches(2.2))
    m_card.fill.solid()
    m_card.fill.fore_color.rgb = CARD_BG
    m_card.line.color.rgb = PptxRGBColor(51, 65, 85)
    mtf = m_card.text_frame
    mp = mtf.paragraphs[0]
    mp.text = "Group 2 Members:"
    mp.font.bold = True
    mp.font.size = PptxPt(16)
    mp.font.color.rgb = TEXT_LIGHT
    for roll, name, role in MEMBERS:
        mpn = mtf.add_paragraph()
        mpn.text = f"• Roll No. {roll}: {name} — {role}"
        mpn.font.size = PptxPt(14)
        mpn.font.color.rgb = TEXT_MUTED

    # SLIDE 2: QUESTIONS & VIZ MATRIX
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    tb2 = s2.shapes.add_textbox(PptxInches(0.8), PptxInches(0.6), PptxInches(11.7), PptxInches(0.8))
    tf2 = tb2.text_frame
    p = tf2.paragraphs[0]
    p.text = "Five Analytical Questions & Visualizations"
    p.font.size = PptxPt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    q_brief = [
        ("Q1. Wave Decoupling Dynamics", "Dual-Axis Line Chart", "Cases (millions) vs deaths (thousands) differ by 1,000x. Secondary axis reveals decoupling during 2022 Omicron wave."),
        ("Q2. Demographic Age vs Deaths", "Scatter Plot by Continent", "Shows positive correlation while spotlighting outliers like Japan (high age, low deaths) and Peru."),
        ("Q3. Continental Spread", "Box Plot by Continent", "Demonstrates that inter-continental differences dominate over variation inside individual continents."),
        ("Q4. Seasonal Mortality Cycles", "Year × Month Heatmap", "Recurring dark bands in Dec, Jan, and Feb expose respiratory winter surge cycles across consecutive years."),
        ("Q5. Global Vaccine Equity", "Frequency Histogram", "Reveals a stark bimodal distribution (<30% vs >75%) that a single global average completely conceals.")
    ]
    for idx, (q_t, v_t, j_t) in enumerate(q_brief):
        y_pos = 1.6 + idx * 1.1
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PptxInches(0.8), PptxInches(y_pos), PptxInches(11.7), PptxInches(0.95))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_BLUE
        btf = box.text_frame
        bp1 = btf.paragraphs[0]
        bp1.text = f"{q_t}  ➔  [{v_t}]"
        bp1.font.bold = True
        bp1.font.size = PptxPt(14)
        bp1.font.color.rgb = ACCENT_BLUE
        bp2 = btf.add_paragraph()
        bp2.text = j_t
        bp2.font.size = PptxPt(12)
        bp2.font.color.rgb = TEXT_MUTED

    # SLIDE 3: LIVE DASHBOARD SHOWCASE (WITH SCREENSHOTS)
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    tb3 = s3.shapes.add_textbox(PptxInches(0.8), PptxInches(0.5), PptxInches(11.7), PptxInches(0.8))
    tf3 = tb3.text_frame
    p = tf3.paragraphs[0]
    p.text = "Live Dashboard Showcase & Visualizations"
    p.font.size = PptxPt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    # Add 2 screenshots side by side
    s1_img = SCREENSHOTS_DIR / "screenshot_1_overview_kpis.png"
    s2_img = SCREENSHOTS_DIR / "screenshot_2_time_series_trends.png"
    if s1_img.exists() and s2_img.exists():
        s3.shapes.add_picture(str(s1_img), PptxInches(0.8), PptxInches(1.5), width=PptxInches(5.7))
        s3.shapes.add_picture(str(s2_img), PptxInches(6.8), PptxInches(1.5), width=PptxInches(5.7))

    # Caption box
    c_box = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, PptxInches(0.8), PptxInches(5.4), PptxInches(11.7), PptxInches(1.4))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = CARD_BG
    c_box.line.color.rgb = PptxRGBColor(51, 65, 85)
    ctf = c_box.text_frame
    cp = ctf.paragraphs[0]
    cp.text = "Interactive Features: Real-time KPI cards, country multiselect, date window slider, and dual-axis longitudinal trend comparisons."
    cp.font.size = PptxPt(14)
    cp.font.color.rgb = TEXT_LIGHT
    cp2 = ctf.add_paragraph()
    cp2.text = f"Live App Link: {LIVE_URL}"
    cp2.font.size = PptxPt(13)
    cp2.font.bold = True
    cp2.font.color.rgb = ACCENT_GREEN

    # SLIDE 4: FINDINGS & RECOMMENDATIONS
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    tb4 = s4.shapes.add_textbox(PptxInches(0.8), PptxInches(0.5), PptxInches(11.7), PptxInches(0.8))
    tf4 = tb4.text_frame
    p = tf4.paragraphs[0]
    p.text = "Five Major Findings & Three Actionable Recommendations"
    p.font.size = PptxPt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    # Left column: Findings
    f_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PptxInches(0.8), PptxInches(1.5), PptxInches(5.7), PptxInches(5.3))
    f_box.fill.solid()
    f_box.fill.fore_color.rgb = CARD_BG
    f_box.line.color.rgb = ACCENT_BLUE
    ftf = f_box.text_frame
    fp = ftf.paragraphs[0]
    fp.text = "💡 Five Major Findings"
    fp.font.bold = True
    fp.font.size = PptxPt(16)
    fp.font.color.rgb = ACCENT_BLUE
    f_items = [
        "1. Decoupling: Omicron wave produced 4x cases with proportionally far fewer deaths due to vaccines.",
        "2. Age Sensitivity: Age correlates with deaths, but Japan was an outlier due to rapid masking.",
        "3. Continental Disparities: Inter-continental variance exceeded internal continental variation.",
        "4. Winter Seasonality: Recurring mortality surges in Dec–Feb across consecutive years.",
        "5. Bimodal Vaccination: Countries split into twin clusters (<30% vs >75%), proving extreme inequity."
    ]
    for it in f_items:
        p = ftf.add_paragraph()
        p.text = it
        p.font.size = PptxPt(12)
        p.font.color.rgb = TEXT_LIGHT

    # Right column: Recommendations & Wrong Viz
    r_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PptxInches(6.8), PptxInches(1.5), PptxInches(5.7), PptxInches(5.3))
    r_box.fill.solid()
    r_box.fill.fore_color.rgb = CARD_BG
    r_box.line.color.rgb = ACCENT_GREEN
    rtf = r_box.text_frame
    rp = rtf.paragraphs[0]
    rp.text = "🎯 Three Actionable Recommendations"
    rp.font.bold = True
    rp.font.size = PptxPt(16)
    rp.font.color.rgb = ACCENT_GREEN
    r_items = [
        "1. Regional mRNA Hubs: Fund decentralized vaccine manufacturing in Africa & Latin America.",
        "2. Seasonal Preparedness: Schedule booster campaigns in autumn ahead of winter surges.",
        "3. Standardized Surveillance: Mandate unified pandemic reporting standards under WHO."
    ]
    for it in r_items:
        p = rtf.add_paragraph()
        p.text = it
        p.font.size = PptxPt(12)
        p.font.color.rgb = TEXT_LIGHT

    rp_wv = rtf.add_paragraph()
    rp_wv.text = "\n⚠️ Wrong Visualization Challenge (Q5):"
    rp_wv.font.bold = True
    rp_wv.font.size = PptxPt(14)
    rp_wv.font.color.rgb = PptxRGBColor(248, 113, 113)

    p_wvd = rtf.add_paragraph()
    p_wvd.text = "Correct Histogram exposes bimodal equity split. Misleading Pie Chart discretizes data into equal slices, concealing the valley of unimmunized nations."
    p_wvd.font.size = PptxPt(12)
    p_wvd.font.color.rgb = TEXT_MUTED

    # SLIDE 5: 2-MINUTE DATA STORY & AI CRITIQUE
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    tb5 = s5.shapes.add_textbox(PptxInches(0.8), PptxInches(0.5), PptxInches(11.7), PptxInches(0.8))
    tf5 = tb5.text_frame
    p = tf5.paragraphs[0]
    p.text = "2-Minute Data Story & AI as a Critic"
    p.font.size = PptxPt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    # Story box
    st_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PptxInches(0.8), PptxInches(1.5), PptxInches(11.7), PptxInches(3.3))
    st_box.fill.solid()
    st_box.fill.fore_color.rgb = CARD_BG
    st_box.line.color.rgb = PptxRGBColor(168, 85, 247)
    stf = st_box.text_frame
    stp = stf.paragraphs[0]
    stp.text = "🎙️ 2-Minute Data Story Framework:"
    stp.font.bold = True
    stp.font.size = PptxPt(16)
    stp.font.color.rgb = PptxRGBColor(192, 132, 252)

    story_points = [
        ("1. What did we discover?", "Pandemic waves decoupled in 2022 (Omicron peak blunted by vaccines); age did not dictate death rates in Japan; and vaccine coverage formed a bimodal divide."),
        ("2. Why does it matter?", "Tabular spreadsheets hide these realities. Without dual-axis plots and histograms, vaccine effectiveness is unseen and global vaccine inequality is buried under misleading averages."),
        ("3. What action should be taken?", "Fund regional manufacturing hubs in low-income nations, schedule seasonal autumn booster surges, and mandate standardized real-time surveillance.")
    ]
    for q, a in story_points:
        p = stf.add_paragraph()
        p.text = f"{q} {a}"
        p.font.size = PptxPt(13)
        p.font.color.rgb = TEXT_LIGHT

    # AI Critic Box
    ai_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PptxInches(0.8), PptxInches(5.0), PptxInches(11.7), PptxInches(1.8))
    ai_box.fill.solid()
    ai_box.fill.fore_color.rgb = CARD_BG
    ai_box.line.color.rgb = PptxRGBColor(51, 65, 85)
    aitf = ai_box.text_frame
    aip = aitf.paragraphs[0]
    aip.text = "🤖 AI as a Critic Evaluation Summary (Q1):"
    aip.font.bold = True
    aip.font.size = PptxPt(14)
    aip.font.color.rgb = ACCENT_BLUE

    ai_crit_summary = [
        "• Dual Y-Axis [ACCEPTED]: Solves 1,000x scale gap between daily cases and deaths.",
        "• Milestone Annotations [ACCEPTED]: Adds vital context (vaccine rollout, Omicron surge).",
        "• Logarithmic Scale [REJECTED]: Distorts public health severity and absolute mortality perception.",
        "• 7-Day Smoothed Label [ACCEPTED]: Ensures transparency regarding weekend reporting lags."
    ]
    for it in ai_crit_summary:
        p = aitf.add_paragraph()
        p.text = it
        p.font.size = PptxPt(11)
        p.font.color.rgb = TEXT_MUTED

    ppt_path = DOCS_DIR / "Group2_COVID19_Presentation.pptx"
    prs.save(str(ppt_path))
    print(f"PowerPoint presentation saved to: {ppt_path}")

def build_standalone_markdown_report():
    md_content = f"""# 🦠 COVID-19 Global Data Explorer
## Final Consolidated Project Report | Group 2
**Course:** Data Visualization Techniques (LA-2)  
**Live Interactive Dashboard:** [{LIVE_URL}]({LIVE_URL})  
**GitHub Repository:** [{GITHUB_URL}]({GITHUB_URL})  

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
"""
    out_file = BASE_DIR / "FINAL_SUBMISSION_REPORT.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Markdown report saved to: {out_file}")

def create_consolidated_zip():
    zip_dest_desktop = Path(r"C:\Users\nisha\OneDrive\Desktop\Group2_Final_Submission.zip")
    zip_dest_project = BASE_DIR / "Group2_COVID19_Consolidated_Submission.zip"

    files_to_include = [
        # Root files
        ("app.py", BASE_DIR / "app.py"),
        ("requirements.txt", BASE_DIR / "requirements.txt"),
        ("README.md", BASE_DIR / "README.md"),
        ("FINAL_SUBMISSION_REPORT.md", BASE_DIR / "FINAL_SUBMISSION_REPORT.md"),
        (".gitignore", BASE_DIR / ".gitignore"),
        # Data files
        ("data/covid_data.csv", DATA_DIR / "covid_data.csv"),
        ("data/owid-covid-codebook.csv", DATA_DIR / "owid-covid-codebook.csv"),
        ("data/create_dataset.py", DATA_DIR / "create_dataset.py"),
        # Screenshots
        ("screenshots/screenshot_1_overview_kpis.png", SCREENSHOTS_DIR / "screenshot_1_overview_kpis.png"),
        ("screenshots/screenshot_2_time_series_trends.png", SCREENSHOTS_DIR / "screenshot_2_time_series_trends.png"),
        ("screenshots/screenshot_3_rankings_and_map.png", SCREENSHOTS_DIR / "screenshot_3_rankings_and_map.png"),
        ("screenshots/screenshot_4_findings_and_recommendations.png", SCREENSHOTS_DIR / "screenshot_4_findings_and_recommendations.png"),
        # Documents
        ("docs/Group2_COVID19_Project_Report.docx", DOCS_DIR / "Group2_COVID19_Project_Report.docx"),
        ("docs/Group2_COVID19_Presentation.pptx", DOCS_DIR / "Group2_COVID19_Presentation.pptx"),
    ]

    for dest in [zip_dest_desktop, zip_dest_project]:
        with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zipf:
            for arcname, fpath in files_to_include:
                if fpath.exists():
                    zipf.write(fpath, arcname)
                    print(f"Added to {dest.name}: {arcname}")
                else:
                    print(f"WARNING: File not found: {fpath}")

        print(f"Consolidated zip created successfully: {dest} (Size: {dest.stat().st_size / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    print("Building Word document with embedded screenshots...")
    build_word_document()
    print("Building PowerPoint presentation with screenshots & live links...")
    build_presentation()
    print("Building Standalone Markdown report...")
    build_standalone_markdown_report()
    print("Packaging consolidated ZIP submission archive...")
    create_consolidated_zip()
    print("ALL SUBMISSION DELIVERABLES SUCCESSFULLY PRODUCED!")

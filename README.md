Manufacturing Sector Economic Performance & Supply Chain Risk Analytics

Business Objective & Project Overview
This project transforms raw macroeconomic survey data spanning over three decades into an interactive, production-ready analytical asset. By applying end-to-end data science methodology, this pipeline cleans complex quarterly formatting, reshapes structural data variables, and engineers an Inventory-to-Sales Ratio to evaluate microeconomic supply chain health and market risk profiles up through early 2026.

This project was built to demonstrate the practical application of core data science principles outlined in my Data Science Diploma curriculum, focusing on real-world data sanitization, domain-specific feature engineering, and advanced dual-axis data communication.


Tech Stack & Key Competencies
*   Language: Python 3.x
*   Data Manipulation & Engineering: Pandas, NumPy
*   Data Visualization: Plotly (Graph Objects)
*   Core Methodologies: Time-Series Indexing, Data Pivoting, Feature Engineering, Outlier Sanitization

Key Analytical Insights Engineered
*   The Supply Chain Risk Metric: Raw data maps total revenue and inventory columns independently. This project introduces an engineered feature: 
    $$\text{Inventory-to-Sales Ratio} = \frac{\text{Stocks}}{\text{Sales}}$$
*   Macro Economic Tracking: A rising ratio explicitly flags asset capture—where goods are stacking up in warehouses faster than consumer demand can clear them. A declining ratio highlights high demand or hyper-lean inventory efficiency.
*   Temporal Normalization: Converted arbitrary, non-standard decimal representations of calendar periods (e.g., `1992.12`) into uniform quarterly strings (`1992-Q4`) and functional python `datetime` timestamps to guarantee chronological tracking over multi-decade intervals.

Repository Structure
```text
├── economic-survey-of-manufacturing-march-2026-quarter.csv  # Raw Dataset
├── app.py                                                   # Complete Analytics Pipeline Script
├── manufacturing_insights.html                              # Generated Interactive Visual Asset
└── README.md                                                # Project Documentation# manufacturing-supply-chain-analytics
Python pipeline &amp; interactive dashboard tracking 30+ years of manufacturing data. Cleans quarterly metrics, pivots macroeconomic variables, and engineers an Inventory-to-Sales Risk Ratio using Pandas and Plotly. Implements end-to-end curriculum standards from my Data Science Diploma into a job-ready portfolio project.

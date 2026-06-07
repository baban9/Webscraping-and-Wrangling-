# Web Scraping and Data Wrangling

Social media data collection and exploratory analysis for Twitter datasets across multiple topics.

## Problem

Ingest public social text data, clean it for analysis, and build dashboards that surface trends.

## Approach

| Artifact | Role |
|----------|------|
| TwitterScraping.py | Data collection script |
| Twitter dashboard.ipynb | EDA and visualization |
| *.csv | Sample tweet datasets (organic food, farmers, coronavirus) |

## Reproducibility

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

For scraping, configure API credentials via environment variables (never commit keys):

```bash
export TWITTER_BEARER_TOKEN=your_token
python TwitterScraping.py
```

## Tech stack

Python 3, pandas, BeautifulSoup, requests, Jupyter

## Data ethics

- Respect platform Terms of Service and rate limits
- Do not republish PII from scraped datasets
- Prefer official APIs over brittle HTML scraping

## Limitations and next steps

- Move large CSVs to Git LFS or external storage
- Add data dictionary for each CSV column
- Parameterize queries in a config file instead of hardcoded strings

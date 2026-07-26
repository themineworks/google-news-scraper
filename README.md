# Google News Scraper: Headlines & Brand Monitor

Python client for **[Google News Scraper: Headlines & Brand Monitor](https://apify.com/themineworks/google-news)** — scrape Google News headlines and sources, monitor brands and topics.

> ⚡ No login, no cookies, no ban risk · runs in the cloud on [Apify](https://apify.com/themineworks/google-news)
>
> 💸 From **$4.0 per 1,000 results** (volume discounts on paid Apify plans). You are only charged for delivered results — empty searches and failed pages are never billed.

## Quick start

```bash
pip install apify-client
python3 google_news_scraper.py --token YOUR_APIFY_TOKEN --query "artificial intelligence"
```

Get a free API token: [console.apify.com/sign-up](https://console.apify.com/sign-up) — then find it under **Settings → API & Integrations**.

## Options

| Flag | Type | Description |
|---|---|---|
| `--token` | string | Apify API token (or `APIFY_TOKEN` env var) |
| `--out` | string | Output basename — writes `results.json` + `results.csv` |
| `--query` | string | Keywords to search Google News for (e.g. "artificial intelligence", "Tesla earnings", "cli |
| `--language` | string | Interface language code, e.g. en-US, en-GB, es-ES, fr-FR, de-DE, hi-IN. |
| `--country` | string | Edition / country code, e.g. US, GB, IN, AU, CA, DE, FR. |
| `--max-results` | integer | Maximum number of articles to return. A single Google News feed caps at ~100; the scraper  |
| `--topic` | string | Fetch a Google News topic section instead of (or alongside) a search. One of: WORLD, NATIO |

Flags map 1:1 to the actor's input schema — full reference and a live output sample on the [Store listing](https://apify.com/themineworks/google-news).

## Output

One row per result, saved as both JSON and CSV with every field the actor returns. Preview the exact fields on the [listing's output tab](https://apify.com/themineworks/google-news).

## Why this actor

- **HTTP-native** — fast, stable, no headless-browser overhead
- **No account risk** — never asks for your login or cookies
- **Fair billing** — pay per delivered result only

MIT © [The Mine Works](https://apify.com/themineworks) — part of a 69-scraper suite trusted by 450+ developers.

# Google News Scraper: Articles, Sources & Topics

Scrape Google News headlines, sources, and publication dates by keyword or topic. Returns article title, publisher, URL, published date, and image URL. No API key required. Pay per article returned.

**Run it on Apify:** [apify.com/themineworks/google-news](https://apify.com/themineworks/google-news)
**Docs, FAQ and pricing:** [themineworks.com/actors/google-news](https://themineworks.com/actors/google-news/)

**Price:** $0.001 per article on Apify's free plan, plus a $0.005 start fee per run. Failed and empty results are never charged.

## What it returns

* Headlines, sources, and publication dates
* Search by keyword, topic, or company name
* Filter by language, region, and recency
* Returns article URL and publisher name
* Zero charge on empty searches

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/google-news").call(run_input={
    "query": "artificial intelligence",
    "topic": "TECHNOLOGY",
    "language": "en-US",
    "country": "US"
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/google-news').call({
    "query": "artificial intelligence",
    "topic": "TECHNOLOGY",
    "language": "en-US",
    "country": "US"
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~google-news/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "artificial intelligence", "topic": "TECHNOLOGY", "language": "en-US", "country": "US"}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 google_news_scraper.py --token YOUR_APIFY_TOKEN --query "artificial intelligence" --topic "TECHNOLOGY" --language "en-US" --country "US"
node google_news_scraper.mjs --token YOUR_APIFY_TOKEN --query "artificial intelligence" --topic "TECHNOLOGY" --language "en-US" --country "US"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `query` | string |  | Keywords to search Google News for (for example "artificial intelligence", "Tesla earnings", "climate policy") |
| `topic` | string |  | Fetch a Google News topic section instead of (or alongside) a search, for example TECHNOLOGY or BUSINESS |
| `language` | string |  | Interface language code, for example en-US, en-GB, es-ES, fr-FR, de-DE, hi-IN |
| `country` | string |  | Edition / country code, for example US, GB, IN, AU, CA, DE, FR |
| `maxResults` | integer | `100` | Maximum number of articles to return |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `title` | string | Headline of the article |
| `url` | string | URL of the article |
| `source` | string | Publisher / news source name |
| `published_at` | string | Publication date from the RSS feed (RFC 2822 format) |
| `snippet` | string | Short description / preview text of the article |
| `topic` | string | Google News topic category (for example TECHNOLOGY), if scraped via topic mode |
| `query` | string | Search query that returned this article, if scraped via query mode |
| `scraped_at` | string | ISO 8601 timestamp of when the record was scraped |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/google-news
```

## FAQ

### Does Google News have an official API?

Google shut down the Google News API in 2013. The only official alternative is the Programmable Search Engine, which has limited news coverage. This scraper accesses Google News directly via the RSS feed and web interface.

### What data does each article record include?

Article title, publisher name, article URL, publication date and time, article snippet, and image URL where available. All returned as structured JSON.

### Can I search by company name or stock ticker?

Yes. Search queries work the same as Google News search: company names, stock tickers, product names, executive names, or any keyword. Use quotes for exact phrases.

### How fresh is the data?

Google News indexes articles within minutes of publication. This scraper returns whatever Google News is currently showing, so recency matches what you would see in the browser.

### Can I monitor competitor mentions or brand sentiment?

Yes. Run the scraper on a schedule via Apify's scheduler (hourly or daily) to track new articles about a company, product, or keyword over time. Combine with an LLM for sentiment analysis.

### How much does the Google News Scraper cost?

$0.001 per article on Apify's free plan, plus a $0.005 start fee per run. Failed and empty results are never charged. You can cap what a single run may spend with the maximum cost setting on Apify.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [B2B Leads Finder](https://themineworks.com/actors/b2b-leads-finder/): Business emails and LinkedIn profiles for target companies
* [LinkedIn Company Scraper](https://themineworks.com/actors/linkedin-company-details/): Company size, industry, website, and followers without login
* [Zillow Rental Listings Scraper](https://themineworks.com/actors/zillow-rental-listings/): Scrape Zillow for-rent listings by city or zip. $1 per 1,000 results

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works

#!/usr/bin/env python3
"""Headlines, sources, and publication dates as structured JSON. Python, Node.js and cURL clients for the Google News Scraper on Apify, pay per result.

Command-line client for the themineworks/google-news actor on Apify: runs it, waits for it
to finish and saves every result as JSON and CSV. Flags map 1:1 to the actor's input.
Free Apify account and API token: https://console.apify.com/sign-up
Docs and pricing: https://themineworks.com/actors/google-news/
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/google-news"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    ap.add_argument("--out", default="results", help="Output basename, writes .json and .csv")
    ap.add_argument("--query", help="Keywords to search Google News for (for example 'artificial intelligence', 'Tesla…")
    ap.add_argument("--topic", help="Fetch a Google News topic section instead of (or alongside) a search, for example…")
    ap.add_argument("--language", help="Interface language code, for example en-US, en-GB, es-ES, fr-FR, de-DE, hi-IN")
    ap.add_argument("--country", help="Edition / country code, for example US, GB, IN, AU, CA, DE, FR")
    ap.add_argument("--max-results", type=int, help="Maximum number of articles to return")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN. Free token: https://console.apify.com/sign-up")

    run_input = {}
    if a.query is not None: run_input["query"] = a.query
    if a.topic is not None: run_input["topic"] = a.topic
    if a.language is not None: run_input["language"] = a.language
    if a.country is not None: run_input["country"] = a.country
    if a.max_results is not None: run_input["maxResults"] = a.max_results

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    keys = []
    for it in items:
        keys += [k for k in it if k not in keys]
    if items:
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in it.items()})
    print(f"Done: {len(items)} results saved to {a.out}.json and {a.out}.csv")


if __name__ == "__main__":
    main()

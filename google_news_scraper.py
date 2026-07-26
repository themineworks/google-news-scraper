#!/usr/bin/env python3
"""Scrape Google News headlines and sources, monitor brands and topics.
CLI for the themineworks/google-news Apify actor: runs it, waits, saves JSON + CSV.
Free Apify account + API token: https://console.apify.com/sign-up
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/google-news"

def main():
    ap = argparse.ArgumentParser(description="scrape Google News headlines and sources, monitor brands and topics")
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"),
                    help="Apify API token (or set APIFY_TOKEN env var)")
    ap.add_argument("--out", default="results", help="Output basename (.json and .csv)")
    ap.add_argument("--query", help="Keywords to search Google News for (e.g. 'artificial intelligence', 'Tesla earnings', 'climate…")
    ap.add_argument("--language", help="Interface language code, e.g. en-US, en-GB, es-ES, fr-FR, de-DE, hi-IN")
    ap.add_argument("--country", help="Edition / country code, e.g. US, GB, IN, AU, CA, DE, FR")
    ap.add_argument("--max-results", type=int, default=25, help="Maximum number of articles to return")
    ap.add_argument("--topic", help="Fetch a Google News topic section instead of (or alongside) a search")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up")

    run_input = {}
    if a.query is not None: run_input["query"] = a.query
    if a.language is not None: run_input["language"] = a.language
    if a.country is not None: run_input["country"] = a.country
    if a.max_results is not None: run_input["maxResults"] = a.max_results
    if a.topic is not None: run_input["topic"] = a.topic

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    if items:
        keys = []
        for it in items:
            for k in it:
                if k not in keys: keys.append(k)
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: ("" if v is None else v) for k, v in it.items()})
    print(f"Done: {len(items)} results -> {a.out}.json / {a.out}.csv")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Rewrite the "By the Numbers" block from the LIVE oracle + chain.

Runs in GitHub Actions daily. Every dynamic figure is derived at run time —
a hand-typed number rots into a false claim (this repo's README carried a
superseded contract as "the" oracle for a month; never again). On ANY fetch
failure the script leaves the README untouched and exits 0: stale-but-honest
beats fresh-but-wrong, and yesterday's numbers carry yesterday's date stamp.
Static lines (tooling counts, test counts) stay static on purpose.
"""
import json
import re
import sys
import urllib.request
from datetime import date

UA = {"User-Agent": "sailorpepe-profile-refresh/1.0"}


def get_json(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def eth_call(sel, to):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "eth_call",
                       "params": [{"to": to, "data": sel}, "latest"]}).encode()
    req = urllib.request.Request("https://mainnet.base.org", data=body,
                                 headers={"Content-Type": "application/json", **UA})
    return json.load(urllib.request.urlopen(req, timeout=30))["result"]


def main():
    root = get_json("https://oracle.the-undesirables.com/")
    sr = get_json("https://oracle.the-undesirables.com/api/v1/soul-rating")

    catalog = root["total_products"]
    endpoints = root["total_endpoints"]
    free, paid = root["free_endpoints"], root["paid_endpoints"]
    proof_n = int(eth_call("0x9b9d326d", "0xE49104b3d540CBA4BFFe3B73bc06e910A3A7da4e"), 16)
    rated = len(sr.get("rated") or [])
    lock_n = (sr.get("latest_lock") or {}).get("n_predictions")
    sealed = (sr.get("sealed_souls") or {}).get("count")
    if not all([catalog, endpoints, proof_n, rated, lock_n, sealed]):
        print("a live figure came back empty — leaving README untouched")
        return

    block = f"""<!-- numbers:start -->
```
{catalog // 1000}K+    Products indexed across 25+ TCG games
30M+     Price history data points
{proof_n // 1000}K+    Products in the daily Merkle proof tree (roots on Base + LiteForge)
{lock_n:,}   Predictions locked in the latest weekly soul cohort (whole 4,444-soul family)
{rated * 3:,}      Calls graded per weekly cohort into write-once on-chain results roots
{rated}      Souls competing on the public leaderboard
{sealed:,}    Sealed souls making the same calls, records hidden until mint
50       Blue-chip cards with hourly TWAP feeds
{endpoints}       API endpoints ({free} free, {paid} paid)
35+      MCP local compute tools
24       Live-data AI agent skills
4,444    NFTs generated (ERC-721)
94       Solidity test cases passing
```
<sub>auto-refreshed daily from the live oracle · last refresh {date.today().isoformat()}</sub>
<!-- numbers:end -->"""

    readme = open("README.md").read()
    new = re.sub(r"<!-- numbers:start -->.*?<!-- numbers:end -->", block,
                 readme, count=1, flags=re.S)
    if new == readme:
        print("no change")
        return
    open("README.md", "w").write(new)
    print("numbers refreshed")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"refresh skipped ({e}) — README left untouched")
        sys.exit(0)

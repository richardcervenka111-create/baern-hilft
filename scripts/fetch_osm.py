#!/usr/bin/env python3
"""Fetch the Bern help layer from OpenStreetMap (Overpass) and write data/bern.json.

Layers: drinking water, public toilets, defibrillators (AED).
Area: Stadt Bern, OSM relation 1682378 (Overpass area id 3600000000 + relation id).
Licence of the data: ODbL, © OpenStreetMap contributors — keep the attribution in the page.

Usage:  python3 scripts/fetch_osm.py [--out data/bern.json] [--endpoint URL]
No third-party packages; standard library only.
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import date

AREA = 3601682378  # Stadt Bern
QUERY = f"""
[out:json][timeout:90];
area({AREA})->.a;
(
  nwr["amenity"="drinking_water"](area.a);
  nwr["amenity"="fountain"]["drinking_water"="yes"](area.a);
  nwr["amenity"="toilets"](area.a);
  nwr["emergency"="defibrillator"](area.a);
);
out center tags;
"""

def kind_of(tags):
    if tags.get("emergency") == "defibrillator":
        return "aed"
    if tags.get("amenity") == "toilets":
        return "wc"
    return "water"

def compact(el):
    tags = el.get("tags", {})
    lat = el.get("lat") or el.get("center", {}).get("lat")
    lon = el.get("lon") or el.get("center", {}).get("lon")
    if lat is None or lon is None:
        return None
    row = {
        "k": kind_of(tags),
        "lat": round(lat, 6),
        "lon": round(lon, 6),
        "id": f"{el['type'][0]}{el['id']}",
    }
    name = tags.get("name") or tags.get("description") or tags.get("operator")
    if name:
        row["n"] = name[:80]
    loc = tags.get("defibrillator:location") or tags.get("indoor")
    if loc:
        row["l"] = str(loc)[:120]
    if tags.get("opening_hours"):
        row["h"] = tags["opening_hours"][:80]
    if tags.get("wheelchair"):
        row["w"] = tags["wheelchair"]
    if tags.get("fee"):
        row["f"] = tags["fee"]
    if tags.get("access") in ("private", "customers", "no"):
        row["a"] = tags["access"]
    return row

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/bern.json")
    ap.add_argument("--endpoint", default="https://overpass-api.de/api/interpreter")
    args = ap.parse_args()

    body = urllib.parse.urlencode({"data": QUERY}).encode()
    req = urllib.request.Request(args.endpoint, data=body, headers={"User-Agent": "baern-hilft/1.0 (open data, once per release)"})
    with urllib.request.urlopen(req, timeout=120) as r:
        payload = json.load(r)

    rows = [c for c in (compact(e) for e in payload.get("elements", [])) if c]
    rows.sort(key=lambda r: (r["k"], r["lat"], r["lon"]))
    counts = {}
    for r in rows:
        counts[r["k"]] = counts.get(r["k"], 0) + 1
    out = {
        "source": "OpenStreetMap contributors, ODbL, via Overpass API",
        "area": "Stadt Bern (OSM relation 1682378)",
        "fetched": date.today().isoformat(),
        "counts": counts,
        "items": rows,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(f"wrote {args.out}: {counts} ({len(rows)} items)")
    if not rows:
        print("no rows: check the area id or the endpoint", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())

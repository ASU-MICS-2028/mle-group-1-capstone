"""Ghana's 16 regions from geoBoundaries gbOpen GHA ADM1 (CC BY-SA 2.0).

    python src/regions.py            # download once into data/raw/geoboundaries/, then self-check
"""
import json
import sys
import urllib.request
from pathlib import Path

import geopandas as gpd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "geoboundaries"
API = "https://www.geoboundaries.org/api/current/gbOpen/GHA/ADM1/"
FILE = RAW / "geoBoundaries-GHA-ADM1.geojson"


def download() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    meta = json.load(urllib.request.urlopen(API))
    urllib.request.urlretrieve(meta["gjDownloadURL"], FILE)
    keep = ["boundaryID", "boundaryYearRepresented", "boundaryLicense", "buildDate", "gjDownloadURL"]
    (RAW / "meta.json").write_text(json.dumps({k: meta[k] for k in keep}, indent=2))


def load() -> gpd.GeoDataFrame:
    """16 rows: region_id (shapeISO), region_name, geometry in EPSG:4326."""
    if not FILE.exists():
        download()
    g = gpd.read_file(FILE)[["shapeISO", "shapeName", "geometry"]]
    g = g.rename(columns={"shapeISO": "region_id", "shapeName": "region_name"}).to_crs(4326)
    return g.sort_values("region_id").reset_index(drop=True)


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "src"))
    from synthetic import REGIONS

    g = load()
    assert len(g) == 16 and g.region_id.is_unique, len(g)
    assert set(g.region_id) == set(REGIONS), set(g.region_id) ^ set(REGIONS)
    print("passed: 16 regions, codes match the contract")

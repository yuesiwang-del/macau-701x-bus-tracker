"""Educational example: scrape public 701X route page; never overwrite saved snapshot on failure."""
import json
from datetime import date
from pathlib import Path
import requests
from bs4 import BeautifulSoup

URL = "https://motransportinfo.com/cn/route/701X/0"
DEST = Path(__file__).with_name("stops.json")

def main():
    response = requests.get(URL, timeout=20, headers={"User-Agent": "Mozilla/5.0 (educational project)"})
    response.raise_for_status()
    response.encoding = response.apparent_encoding or "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    names = []
    keywords = ("澳门大学总站", "橫琴澳方口岸", "横琴澳方口岸", "莲花路", "連貫公路", "连贯公路", "永进马路", "路氹")
    for el in soup.find_all(["a","li","span"]):
        label = el.get_text(" ", strip=True)
        if 3 <= len(label) <= 36 and any(k in label for k in keywords) and (not names or names[-1] != label):
            names.append(label)
    if len(names) < 15:
        raise ValueError(f"Only extracted {len(names)} candidate stops: website structure may have changed. stops.json was not overwritten.")
    payload = {"route":"701X","source":URL,"scraped_on":date.today().isoformat(),"stops":names}
    DEST.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Saved {len(names)} stop entries to {DEST}")

if __name__ == "__main__":
    main()

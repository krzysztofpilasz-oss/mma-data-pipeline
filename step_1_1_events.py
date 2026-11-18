"""Krok 1.1: wypisz 10 ostatnich wydarzeń UFC z data/event.csv."""
import csv

with open("data/event.csv", encoding="utf-8") as f:
    events = list(csv.DictReader(f))

events.sort(key=lambda e: e["date"], reverse=True)

for e in events[:10]:
    print(e["date"], "|", e["event_name"], "|", e["location"])

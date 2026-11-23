from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import csv

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return "<h1>Hello world!</h1>"

@app.get("/ufo_sightings")
def get_sightings() -> list[dict]:
    return load_sightings("data/scrubbed.csv")

def load_sightings(filepath: str) -> list[dict]:
    sightings = []

    with open(filepath, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)

    return sightings
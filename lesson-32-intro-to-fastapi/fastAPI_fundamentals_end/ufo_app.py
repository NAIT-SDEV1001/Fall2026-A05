import csv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """


def load_ufo_data(filepath: str) -> list[dict]:
    sightings = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings


@app.get("/ufo_sightings")
def get_sightings() -> list[dict]:
    return load_ufo_data("data/scrubbed.csv")


@app.get("/ufo_sightings_complete")
def get_complete_sightings() -> list[dict]:
    return load_ufo_data("data/complete.csv")


@app.get("/ufo_sightings_first_ten")
def get_first_ten_sightings() -> list[dict]:
    return load_ufo_data("data/scrubbed.csv")[:10]

# Music Analysis Application

import csv
from pathlib import Path

NUMERIC_COLUMNS = ['members', 'year_formed', 'monthly_listeners']

def read_artists(file_path):
    """Read the music artists data from a CSV file"""
    all_artists = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for artist in reader:
                all_artists.append(artist)
    except FileNotFoundError as e:
        print(f"File not found: {e}")

    return all_artists

def filter_by_min_listeners(artists, minimum):
    """Return artists with `minimum` monthly listeners"""
    return [
        artist 
        for artist in artists 
        if (int(artist['monthly_listeners']) >= minimum)
    ]

def sort_artists_by(artists, column, reverse=True, top_n=5):
    """Sort the artists by a column and return the top N."""

    if column in NUMERIC_COLUMNS:
        key = lambda artist: int(artist[column])
    else:
        key = lambda artist: artist[column]

    sorted_artists = sorted(artists, key=key, reverse=reverse)
    
    return sorted_artists[:top_n]

def write_top_artists(file_path, artists):
    """Write a list of artist dictionaries to a CSV file."""
    fieldnames = list(artists[0].keys())
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)

def add_listeners_per_member(file_path):
    """Read the CSV, add a listeners_per_member column, and write it back."""
    
    artists = read_artists(file_path)
    for artist in artists:
        listeners = int(artist['monthly_listeners'])
        members = int(artist['members'])
        artist['listeners_per_member'] = round(listeners / members)
    
    write_top_artists(file_path, artists)

def add_revenue(file_path):
    """Read the CSV, add a revenue column, and write it back."""
    
    artists = read_artists(file_path)
    for artist in artists:
        listeners = int(artist['monthly_listeners'])
        artist['revenue'] = listeners * 20.0
    
    write_top_artists(file_path, artists)

def main():
    data_dir = Path(__file__).parent / 'data'
    file_path =  data_dir / "music_artists.csv"
    
    all_artists = read_artists(file_path)

    column = "year_formed"

    columns = list(all_artists[0].keys())
    print("\nAvailable columns to sort by:")
    
    for index, column in enumerate(columns):
        print(f"{index + 1}. {column}")
    
    choice = int(input("Enter the number of the column you want to sort by: ")) - 1

    selected_column = columns[choice]

    top_artists = sort_artists_by(all_artists, selected_column)

    for index, artist in enumerate(top_artists):
        print(f"{index+1}. {artist["band_name"]}")

    write_top_artists(data_dir / 'top_artists.csv', top_artists)

    # add_listeners_per_member(file_path)
    add_revenue(file_path)

if __name__ == "__main__":
    main()
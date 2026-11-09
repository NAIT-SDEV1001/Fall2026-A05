import pyexcel as pex

def main():
    GAME_REVIEWS_FILE_NAME = "game_reviews.xlsx"
    
    # the data we're going to write to the excel file
    GAME_REVIEWS = [
        ["Title", "Platform", "Score"],
        ["Elden Ring", "PC", 95],
        ["Stardew Valley", "Switch", 89],
        ["Cyberpunk 2077", "PS5", 82],
        ["No Man's Sky", "PC", 90],
        ["Gollum", "PS5", 43],
    ]

if __name__ == "__main__":
    main()
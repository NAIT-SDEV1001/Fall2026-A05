import pyexcel as pex

def create_game_reviews_excel_file(reviews: list[list], output_file: str) -> None:
    '''
    Creates an excel file of game reviews from source data to `output_file`
    '''
    pex.save_as(array=reviews, dest_file_name=output_file)

def add_recommendation_column_to_excel_file(input_file: str, output_file:str ) -> None:
    sheet: pex.Sheet = pex.get_sheet(file_name=input_file)

    recommendations = ["Recommendation"]

    rows_list = sheet.to_array()

    for row_index, row_value in enumerate(rows_list[1:]):
        score = row_value[2]

        if score >= 90:
            recommendations.append("Highly recommended")
        elif score >= 80:
            recommendations.append("Recommended")
        elif score >= 70:
            recommendations.append("Average")
        else:
            recommendations.append("Not recommended")

    sheet.column += recommendations

    sheet.save_as(output_file)

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

    create_game_reviews_excel_file(GAME_REVIEWS, GAME_REVIEWS_FILE_NAME)
    add_recommendation_column_to_excel_file(GAME_REVIEWS_FILE_NAME, "recommended_game_reviews.xlsx")

if __name__ == "__main__":
    main()
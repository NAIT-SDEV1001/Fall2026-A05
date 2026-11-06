import requests

def get_top_ten_headline_ids() -> list[int]:
    headline_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:10]
    return headline_ids

def get_headline_by(headline_id: int):
    headline = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{headline_id}.json").json()
    return headline

def main():
    ids = get_top_ten_headline_ids()

    for index, id in enumerate(ids):
        headline = get_headline_by(id)

        print(f"Headline {index + 1}.")
        print(f"Title: {headline['title']}")
        print(f"URL: {headline.get('url', 'No URL available')}")
        print("-" * 40)


if __name__ == "__main__":
    main()
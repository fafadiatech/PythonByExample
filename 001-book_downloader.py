import requests
from collections import defaultdict

books = [
    "/ebooks/1342",
    "/ebooks/2701",
    "/ebooks/1513",
    "/ebooks/145",
    "/ebooks/64317",
    "/ebooks/2641",
    "/ebooks/37106",
    "/ebooks/100",
    "/ebooks/67979",
    "/ebooks/16389",
    "/ebooks/2542",
    "/ebooks/11",
    "/ebooks/174",
    "/ebooks/6761",
    "/ebooks/394",
    "/ebooks/4085",
    "/ebooks/2160",
    "/ebooks/6593",
    "/ebooks/844",
    "/ebooks/1259",
    "/ebooks/5197",
    "/ebooks/1952",
    "/ebooks/98",
    "/ebooks/2554",
    "/ebooks/73093",
    "/ebooks/5200",
    "/ebooks/1080",
    "/ebooks/345",
    "/ebooks/408",
    "/ebooks/43",
    "/ebooks/25344",
    "/ebooks/1400",
    "/ebooks/70034",
    "/ebooks/1260",
    "/ebooks/219",
    "/ebooks/76",
    "/ebooks/1661",
    "/ebooks/2600",
    "/ebooks/1232",
    "/ebooks/205",
    "/ebooks/2591",
    "/ebooks/6130",
    "/ebooks/28054",
    "/ebooks/1727",
    "/ebooks/3207",
    "/ebooks/73091",
    "/ebooks/2000",
    "/ebooks/46",
    "/ebooks/35899",
    "/ebooks/73092",
    "/ebooks/4300",
    "/ebooks/768",
    "/ebooks/7370",
    "/ebooks/2814",
    "/ebooks/41445",
    "/ebooks/1998",
    "/ebooks/73096",
    "/ebooks/74",
    "/ebooks/514",
    "/ebooks/10623",
    "/ebooks/5740",
    "/ebooks/73102",
    "/ebooks/55",
    "/ebooks/16",
    "/ebooks/1184",
    "/ebooks/23",
    "/ebooks/45",
    "/ebooks/67098",
    "/ebooks/3825",
    "/ebooks/244",
    "/ebooks/2852",
    "/ebooks/17161",
    "/ebooks/1497",
    "/ebooks/158",
    "/ebooks/8492",
    "/ebooks/42324",
    "/ebooks/120",
    "/ebooks/2680",
    "/ebooks/996",
    "/ebooks/4363",
    "/ebooks/58585",
    "/ebooks/36",
    "/ebooks/8800",
    "/ebooks/600",
    "/ebooks/30254",
    "/ebooks/160",
    "/ebooks/15399",
    "/ebooks/4217",
    "/ebooks/27827",
    "/ebooks/161",
    "/ebooks/829",
    "/ebooks/16328",
    "/ebooks/3296",
    "/ebooks/33283",
    "/ebooks/36034",
    "/ebooks/41",
    "/ebooks/35",
    "/ebooks/10",
    "/ebooks/22472",
]


def download_book(file_name):
    book_id = file_name.replace("/ebooks/", "")
    file_to_save = f"{book_id}.txt"
    base_url = f"https://www.gutenberg.org/ebooks/{book_id}.txt.utf-8"
    response = requests.get(base_url)
    if response.status_code == 200:
        with open(file_to_save, "w") as output:
            output.write(response.text)
        print(f"Successfully downloaded: {file_to_save}")
        return file_to_save, True

    print(f"Failed to downloaded: {file_to_save}")
    return None, False


def count_words(file_to_read):
    counts = defaultdict(int)
    with open(file_to_read) as feed:
        for row in feed.readlines():
            row = row.strip().lower()
            for token in row.split():
                counts[token] += 1
    return sum(counts.values())


if __name__ == "__main__":
    for current in books:
        file_to_process, success = download_book(current)
        if success:
            total_words = count_words(file_to_process)
            print(f"{current} has {total_words} words")

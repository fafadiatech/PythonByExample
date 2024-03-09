import os
from collections import defaultdict


def index_single_file(file_to_index, index):
    with open(file_to_index) as feed:
        for row in feed.readlines():
            row = row.strip().lower()
            for token in row.split():
                if file_to_index not in index[token]:
                    index[token].append(file_to_index)
    print(f"Completed indexing: {file_to_index}")
    return index


def index_all_files(index):
    all_text_files = [
        current_file
        for current_file in os.listdir(".")
        if current_file.find(".txt") != -1
    ]
    for current in all_text_files:
        index = index_single_file(current, index)


if __name__ == "__main__":
    index = defaultdict(list)
    index_all_files(index)
    while True:
        q = input("What do you want to search for?:")
        if q == "QUIT":
            break
        if q in index:
            all_docs = ",".join(index[q])
            print(f"{q} in present in :{all_docs}")

def get_book_word_count(filepath: str):
    with open(filepath) as f:
        words = f.read().split()
    return len(words)


def count_char(text: str):
    counts = {}
    for c in text:
        lc = c.lower()
        counts[lc] = counts.get(lc, 0) + 1
    return counts


def sort_counts(chars: dict):
    sorted_counts = []
    for c in chars:
        if c.isalpha():
            sorted_counts.append({"character": c, "count": chars[c]})
    sorted_counts.sort(reverse=True, key=lambda x: x["count"])
    return sorted_counts

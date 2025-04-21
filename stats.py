def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict:
    char_count = {}
    text = text.lower()
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count


def get_sorted_character_report(char_count: dict) -> list:
    report = []

    for char, count in char_count.items():
        if char.isalpha():
            report.append({'char': char, 'count': count})
    
    report.sort(key=lambda item: item['count'], reverse=True)
    return report


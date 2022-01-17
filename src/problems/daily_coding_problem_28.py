def justify(words, line_length):
    results = []
    while words:
        results.append(_add_line(words, line_length))
        print(results)
    return results


def _add_line(words, line_length):
    line_words = [words.pop(0)]
    current_line_length = len(line_words[0])
    while words and current_line_length + len(words[0]) + 1 <= line_length:
        current_word = words.pop(0)
        line_words.append(current_word)
        current_line_length += len(current_word) + 1
    remaining = line_length - current_line_length
    space_count = len(line_words) - 1
    average = remaining // space_count
    line = []
    for i, w in enumerate(line_words):
        line.append(w)
        if i < len(line_words) - 1:
            spaces_to_add = average + 1 if average * space_count < remaining else average
            line.append(' ' * (spaces_to_add + 1))
            remaining -= spaces_to_add
            space_count -= 1
    return "".join(line)

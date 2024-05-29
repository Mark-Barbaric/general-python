def decode(message_file: str):
    try:
        with open(message_file, 'r') as file:
            text_lines = file.read().splitlines()
    except FileNotFoundError:
        print(f"file doesn't exist: {message_file}")
        return 1

    word_dict = {int(line.split(' ')[0]): line.split(' ')[1] for line in text_lines}
    decoded_words = []
    index = 1
    index_to_use = 1
    while len(text_lines) > 0:
        if len(text_lines) < index:
            break
        else:
            decoded_words.append(word_dict[index_to_use])

        text_lines = text_lines[index:]
        index += 1
        index_to_use += index

    return ' '.join(decoded_words)

def get_non_empty_input(min_length, prompt=''):
    while True:
        user_input = input(prompt)
        if len(user_input) >= min_length:
            return user_input
        else:
            print(f"Eingabe zu kurz. Es sind mindestens {min_length} Zeichen erforderlich.")


def build_multiline_input_string(prompt_end: list[str], prompt=''):
    lines = []
    while True:
        line = input(prompt)
        if line.strip() in prompt_end:
            break
        lines.append(line)
    return '\n'.join(lines)


def build_multiline_input_list(prompt_end: list[str], prompt=''):
    lines = []
    while True:
        line = input(prompt)
        if line.strip() in prompt_end:
            break
        lines.append(line)
    return lines

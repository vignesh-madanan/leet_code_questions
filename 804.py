# 804. Unique Morse Code Words

morse_codes = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]


def uniqueMorseRepresentations(words):
    character_map = dict((zip([chr(i) for i in range(97, 97 + 26)], morse_codes)))
    return "".join(character_map[c] for c in words)


if __name__ == "__main__":
    op = set(map(uniqueMorseRepresentations, ["gin", "zen", "gig", "msg"]))
    print(len(op))
def decode(secret_code, cipher, count, current, mappings, all_messages):
    if count == len(secret_code):
        all_messages.add(current)
        return

    for letter, code in mappings.items():
        code_len = len(code)
        if secret_code[count:count + code_len] == code:
            decode(secret_code, cipher, count + code_len, current + letter, mappings, all_messages)


code = input()
cipher_text = input()

mappings = {}
i = 0
while i < len(cipher_text):
    letter = cipher_text[i]
    i += 1
    num_start = i
    while i < len(cipher_text) and cipher_text[i].isdigit():
        i += 1
    mappings[letter] = cipher_text[num_start:i]

all_messages = set()

decode(code, cipher_text, 0, "", mappings, all_messages)

all_messages = sorted(list(all_messages))
print(len(all_messages))
for message in all_messages:
    print(message)


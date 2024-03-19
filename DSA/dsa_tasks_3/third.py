def decode_message(encoded):
    def decode(index):
        decoded = ''
        while index < len(encoded):
            if encoded[index].isdigit():
                num_start = index
                while index < len(encoded) and encoded[index].isdigit():
                    index += 1
                num_repeats = int(encoded[num_start:index])

                index += 1
                content, index = decode(index)
                decoded += content * num_repeats

            elif encoded[index] == '}':
                return decoded, index + 1
            else:
                decoded += encoded[index]
                index += 1

        return decoded, index

    decoded_message, _ = decode(0)
    return decoded_message


encoded_message = input()
print(decode_message(encoded_message))
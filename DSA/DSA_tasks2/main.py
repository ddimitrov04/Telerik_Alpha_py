def variations(symbols, length, current_text=""):
    if len(current_text) == length:
        print(current_text)
        return

    for symbol in reversed(symbols):
        variations(symbols, length, current_text + symbol)


length = int(input())
symbols = input().split()
variations(symbols, length)
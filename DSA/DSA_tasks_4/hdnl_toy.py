def hdnl_toy(tags):
    stack = []
    for tag in tags:
        letter, level = tag[0], int(tag[1:])
        while stack and stack[-1][1] >= level:
            last_tag = stack.pop()
            print(" " * (len(stack)) + "</" + last_tag[0] + str(last_tag[1]) + ">")

        print(" " * len(stack) + "<" + tag + ">")
        stack.append((letter, level))

    while stack:
        last_tag = stack.pop()
        print(" " * (len(stack))+ "</" + last_tag[0] + str(last_tag[1]) + ">")


hdnl_lines = int(input())
hdnl_tags = []
for i in range(hdnl_lines):
    tag = input()
    hdnl_tags.append(tag)

hdnl_toy(hdnl_tags)

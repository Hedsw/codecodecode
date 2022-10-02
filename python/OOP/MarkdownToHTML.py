def markdown(input):
    i = 0
    res = '<p>'
    block_is_active, is_new_para, strikethrough_began = False, True, False

    while i < len(input):
        ch = input[i: i+2]
        new_line = input[i:i + 1]

        if new_line == '\n':
            if input[i + 1: i + 2] == '\n':
                if block_is_active:
                    res += '</blockquote>'
                    block_is_active = False
                res += '</p>'
                res += '<p>'
                i += 2
            else:
                res += '<br />'
                i += 1

        elif ch == '> ':
            if not block_is_active:
                res += '<blockquote>'
                block_is_active = True
            i += 2
        elif ch == '~~':
            if not strikethrough_began:
                res += '<del>'
                strikethrough_began = True
            else:
                res += '</del>'
            i += 2
        else:
            res += input[i]
            i += 1
        
        # print(repr(res))
    res += '</p>'
    return res


input = "This is a paragraph with a soft\n" + "line break.\n\n" + "This is another paragraph that has\n" + "> Some text that\n" + "> is in a\n" + "> block quote.\n\n" + "This is another paragraph with a ~~strikethrough~~ word.";  

print(markdown(input))
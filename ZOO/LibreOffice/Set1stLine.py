def adjust_line_lengths():
    doc = XSCRIPTCONTEXT.getDocument()
    text = doc.Text
    enum = text.createEnumeration()

    while enum.hasMoreElements():
        paragraph = enum.nextElement()
        if "===>" in paragraph.String:
            if enum.hasMoreElements():
                first_paragraph = enum.nextElement()
                if enum.hasMoreElements():
                    second_paragraph = enum.nextElement()
                    if check_conditions(first_paragraph.String) and check_conditions(second_paragraph.String):
                        first_line, second_line = adjust_lines(first_paragraph.String, second_paragraph.String)
                        first_paragraph.String = first_line
                        second_paragraph.String = second_line

def check_conditions(line):
    return line != "" and not line.startswith("-")

def adjust_lines(first_line, second_line):
    words = second_line.split()
    for word in words:
        new_first_line = first_line + " " + word
        if len(new_first_line.strip()) <= 42 and len(new_first_line.strip()) <= len(second_line.strip()):
            first_line = new_first_line
            second_line = ' '.join(words[1:])
        else:
            break
        words = second_line.split()  # Re-split after modification
    return first_line.strip(), second_line.strip()

# This is required boilerplate for LibreOffice Python scripts
g_exportedScripts = adjust_line_lengths,

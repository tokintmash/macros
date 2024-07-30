def adjust_lines_to_extend_second():
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
                        first_line, second_line = adjust_lines_for_second_line(first_paragraph.String, second_paragraph.String)
                        first_paragraph.String = first_line
                        second_paragraph.String = second_line

def check_conditions(line):
    return line != "" and not line.startswith("-")

def adjust_lines_for_second_line(first_line, second_line):
    words_first_line = first_line.split()
    # Reverse the list to start moving words from the end of the first line
    words_first_line.reverse()
    
    for word in words_first_line:
        # Potential new second line if we move the current word from the first line
        new_second_line = word + " " + second_line
        if len(second_line.strip()) < len(first_line.strip()) and len(new_second_line.strip()) <= 42:
            second_line = new_second_line
            # Update the first line by removing the moved word
            first_line = ' '.join(words_first_line[1:])
        else:
            break
        words_first_line = first_line.split()  # Re-split after modification
        words_first_line.reverse()  # Reverse again for correct order
        
    # Reverse one last time to restore the original word order for the remaining words
    words_first_line.reverse()
    return ' '.join(words_first_line).strip(), second_line.strip()

# This is required boilerplate for LibreOffice Python scripts
g_exportedScripts = adjust_lines_to_extend_second,

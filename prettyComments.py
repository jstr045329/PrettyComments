#!/usr/bin/env python

#-----------------------------------------------------------------------------------------------------------------------
#                                                 prettyComments.py 
#
# In your favorite shell, type commands like this:
#
#       $ python prettyComments.py <language> My Impressive Module endtitle This module is awesome. The motivation for
#       this module is to increase awesomeness...
#
# and this file outputs easy-to-read comments to the console for the language of your choice. Automatically handles 
# word wrap. The comment you are reading right now was written by prettyComments! (Most of it anyway. The indented part
# and blank lines I did manually.)
#
# <language> is a string representing the language of your choice (see comment_markers). It is optional. By default
# this module writes C-style comments.
#
# Anything you type before the word "endtitle" will be centered. Hopefully this part is self explanatory. 
#
# Anything after the word "endtitle" will be left-justified, and words will wrap at the end of the line.
# 
#-----------------------------------------------------------------------------------------------------------------------
import sys
LINE_LENGTH = 120
LINE_MARGIN = 10
TITLE_END = "endtitle"
DEFAULT_LANGUAGE = "c"

# Choose your language by optionally passing in one of these keys from command line:
comment_markers = {
    "bash": "#",
    "c": "//",
    "clj": ";;",
    "cpp": "//",
    "c++": "//",
    "hs": "--",
    "java": "//",
    "py": "#",
    "tcl": "#",
    "v": "//", 
    "vhd": "--",
    }


def centerStr(s):
    numSpaces = int((LINE_LENGTH - len(s)) / 2) - 2
    return (" " * numSpaces) + s


def main():
    if len(sys.argv) < 2:
        return
    if (sys.argv[1] in comment_markers.keys()):
        language = sys.argv[1]
        comment_marker = comment_markers[language]
        argv_start_num = 2
    else:
        comment_marker = comment_markers[DEFAULT_LANGUAGE]
        argv_start_num = 1

    # If the user has entered the endtitle keyword, put an extra line above and below the comment body:
    if TITLE_END in sys.argv:
        add_pad_lines = True
    else:
        add_pad_lines = False

    num_dashes = LINE_LENGTH - len(comment_marker)
    demarcation = comment_marker + ('-' * num_dashes)
    
    words = sys.argv[argv_start_num:]
    y = []
    y.append(demarcation)
    s = " "
    scrapingTitle = True
    title = ""
    linesWritten = 0
    for oneWord in words:
        if oneWord.lower() == TITLE_END:
            scrapingTitle = False
            y.append(comment_marker + centerStr(title))
            title = ""
        
        elif scrapingTitle:
            title += oneWord + " "
            
        elif len(s) > LINE_LENGTH - LINE_MARGIN:
            if linesWritten == 0:
                y.append(comment_marker)
            y.append(comment_marker + s)
            s = " " + oneWord + " "
            linesWritten += 1
            
            
        else:
            s += oneWord + " "
    
    if len(title) > 0:
        y.append(comment_marker + centerStr(title))
    
    if add_pad_lines:
        y.append(comment_marker)

    if len(s.split()) > 0:
        # If s is just a space, don't append a new line for that.
        y.append(comment_marker + s)
    
    if add_pad_lines:
        y.append(comment_marker)
        
    y.append(demarcation)
    
    print("")
    for line in y:
        print(line)
    print("")

    resultStr = ""
    for line in y:
        resultStr += line
        resultStr += "\n"


if __name__ == "__main__":
    main()


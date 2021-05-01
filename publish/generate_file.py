import sys
import os 
import re
from datetime import datetime

from generate_components import generate_header, generate_page_menu, generate_footer, generate_link

def parse_file(path):
    """
    Parses a flattened markdown file exported from Roam
    """
    title = ' '.join(path.split('--')[-1].split('.')[:-1]).strip()
    with open(path, 'r') as fIn:
        lines = fIn.readlines()
    return title, [l for l in lines if l != '\n']

def generate_body(lines):
    body = ''
    for line in lines:
        line = process_line(line)
        if line:
            body += f'       {line}' + os.linesep
    return body

def format_line(line):
    words = re.split(r"(?=\W)|(?<=\W)", line)
    for wix, word in enumerate(words):
        if word[:2] == "__" == word[-2:]:
            words[wix] = "<i>" + word.replace("__", "") + "</i>"
        if word[:2] == "**" == word[-2:]:
            words[wix] = "<b>" + word.replace("**", "") + "</b>"
    return ''.join(words)


def process_line(line):
    line = line.strip()
    # headings
    if line[:2] == "**" == line[-2:]:
        return "<h2>" + line.replace("**", "") + "</h2>"

    # hyperlinks
    if 'http' in line:
        links = [m.group() for m in re.finditer(r"\[(.*?)\]\(.*?\)", line, re.MULTILINE)]
        processed_line = ''
        for link in links:
            chunks = line.split(link)
            processed_line += format_line(chunks[0])
            processed_line += f' {generate_link(link)} '
            processed_line += format_line(chunks[1])
        return '<p>' + processed_line + '<p>'
    
    return '<p>' + format_line(line) + '<p>'

def generate_html(title, paragraphs):
    filepath = "_".join(title.split(" ")[:3]).lower()
    today = datetime.today()
    with open(f'articles/{str(today.year)[2:]}{today.month}-{filepath}.html', 'w+') as fOut:
        fOut.writelines('<html lang="en-US">' + os.linesep)
        fOut.writelines(generate_header(title))
        fOut.writelines(generate_page_menu((title)))
        fOut.writelines('<html lang="en-US">' + os.linesep)
        fOut.writelines('       <div class="container">' + os.linesep)
        fOut.writelines(f'<p><i>{today.strftime("%B")} {today.year}</i></p>')
        fOut.writelines(generate_body(lines))
        fOut.writelines('      </div>')
        fOut.writelines(generate_footer())
        fOut.writelines('</html>')

if __name__ == "__main__":
    title, lines = parse_file(path=sys.argv[1])
    generate_html(title, lines)
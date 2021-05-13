import sys
import os 
import re
from datetime import datetime

import markdown

from generate_components import generate_header, generate_footer, generate_link

def parse_file(path):
    """
    Parses a flattened markdown file exported from Roam
    """
    title = ' '.join(path.split('--')[-1].split('.')[:-1]).strip()
    with open(path, 'r') as fIn:
        content = fIn.read()
    return title, content

def generate_html(title, paragraphs):
    title = title.split('/')[-1]
    filepath = "_".join(title.split(" ")[:3]).lower()
    today = datetime.today()
    with open(f'articles/{today.strftime("%y%m")}-{filepath}.html', 'w+') as fOut:
        fOut.writelines('<html lang="en-US">' + os.linesep)
        fOut.writelines(generate_header(title))
        fOut.writelines('<body>' + os.linesep)
        fOut.writelines('<script src="../js/header.js"></script>' + os.linesep)
        fOut.writelines('<div class="container">' + os.linesep)
        fOut.writelines(f'<h1>{title}</h1>' + os.linesep)
        fOut.writelines(f'<p><i>{today.strftime("%B")} {today.year}</i></p>'  + os.linesep)
        fOut.writelines('<hr>' + os.linesep)
        out = markdown.markdown(paragraphs)
        fOut.writelines(out)
        fOut.writelines('</div>' + os.linesep)
        fOut.writelines('</body>' + os.linesep)
        fOut.writelines(generate_footer())
        fOut.writelines('</html>')

if __name__ == "__main__":
    title, lines = parse_file(path=sys.argv[1])
    generate_html(title, lines)
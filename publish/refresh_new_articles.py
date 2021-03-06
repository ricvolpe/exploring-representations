import os
import re

month_to_name = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

if __name__ == "__main__":
    articles = sorted([a for a in os.listdir('articles/', ) if a.endswith('html')], reverse=True)
    
    with open(f'js/articles_new.js', 'w') as fOut:
        fOut.writelines('document.write(`' + os.linesep)
        fOut.writelines('<table style="width:100%;">' + os.linesep)

        for article in articles:
            path = f'articles/{article}'
            date = article.split('-')[0]
            year = '20' + date[:2]
            month = month_to_name[int(date[2:])]

            with open(path, 'r') as fIn:
                article_content = fIn.read()
            
            title = re.findall(r'<title>(.*)<\/title>', article_content)[0]

            fOut.writelines('<tr>' + os.linesep)
            fOut.writelines(f'<td>- <a href="{path}">{title}</a></td>' + os.linesep)
            fOut.writelines(f'<td>{month} {year}</td>'  + os.linesep)
            fOut.writelines('</tr>' + os.linesep)


        fOut.writelines('</table>' + os.linesep)
        fOut.writelines('`);' + os.linesep)

     
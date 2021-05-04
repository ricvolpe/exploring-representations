def generate_header(page_title):
    return f"""    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta http-equiv="X-UA-Compatible" content="ie=edge" />
      <meta name="msapplication-TileColor" content="#ffffff" />
      <link rel="apple-touch-icon" sizes="180x180" href="../fav/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="../fav/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="../fav/favicon-16x16.png">
      <link rel="manifest" href="../fav/site.webmanifest">
      <meta name="theme-color" content="#ffffff" /> <title>{page_title}</title>
      <meta name="description" content="A story about waiting"/>
      <link rel="stylesheet" href="../css/normalize.css">
      <link rel="stylesheet" href="../css/terminal.css">
      <link id="darkSheet" rel="stylesheet" href="../css/dark.css">
   </head>
   """

def generate_footer():
   return """   <footer>
      <p style="text-align: center; font-size: 12px;">© Riccardo Volpato <script>document.write(new Date().getFullYear())</script></p>
      <script src="../js/main.js"></script> 
   </footer>
   """

def generate_link(markdown_link):
   markdown_link = markdown_link.split(']')
   return f'<a href="{markdown_link[1][1:-1]}">{markdown_link[0][1:]}</a>'
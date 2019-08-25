import feedparser

rssFeedsFile = "rss-feeds.txt"
feedReaderFile = "index.html"
maxNumItems = 3

with open (rssFeedsFile) as r:
    rssLines = r.readlines()

rssFeeds = []
for line in rssLines:
    url = line.rstrip()
    rssFeeds.append(url)

feeds = []

for feed in rssFeeds:
    feeds.append(feedparser.parse(feed))

htmlHeader = """<html>
  <head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="rss-reader.css" type="text/css" />
  </head>
  <body>
  """

newLines = [htmlHeader]

for feed in feeds:
    counter = 0
    newLines.append("  <h3>" + feed["channel"]["title"] + "</h3>\n")
    for item in feed["items"]:
        if counter == maxNumItems:
            newLines.append("    <div class=\"content-collapse section\" >\n")
            newLines.append("      <h3>More ...</h3>\n")
        if counter >= maxNumItems:
            newLines.append("<a class=\"little-link\" href=\"" + item["link"] + "\">" + item["title"] + "</a><br>\n")
        else:
            newLines.append("    <div class=\"content-collapse section\" >\n")
            newLines.append("      <h3><a href=\"" + item["link"] + "\">" + item["title"] + "</a></h3>\n")
            newLines.append(item["summary"])
            newLines.append("    </div>\n")
        counter += 1
    if counter >= maxNumItems:
        newLines.append("    </div>")

htmlFooter = """  </body>
  <script src=\"rss-reader.js\"></script>
</html>"""

newLines.append(htmlFooter)


with open (feedReaderFile, "w") as htmlF:
    for line in newLines:
        htmlF.write(line)

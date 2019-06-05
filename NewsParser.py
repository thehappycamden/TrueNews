#!/home/ubuntu/environment/NeuralNet/bin/python3

import json

text = ""

with open("scraped_articles.json") as json_file:
    data = json.load(json_file)
    papers = data["newspapers"]
    for name, data in papers.items():
        link = data['link']
        text_current = f"-----\n\nSITE: {link}"
        if 'rss' in data:
            rss = data['rss']
            text_current += f"RSS: {rss}"
        text_current += "\n\n"
        for article in data['articles']:
            title = article['title']
            published = article['published']
            content = article['text']
            text_current += f'-----\n\nTITLE: {title}\nPUBLISHED: {published}\nTEXT: {content}\n\n'
        text += text_current

with open("plain_articles.txt", "w") as plaintext:
    plaintext.write(text)
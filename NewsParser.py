#!/home/ubuntu/environment/NeuralNet/bin/python3

import json

# Define the variable
text = ""


# open the json file containing the news articles.
with open("scraped_articles.json") as json_file:
    data = json.load(json_file) # load the file into a dictionary
    papers = data["newspapers"] # get the list of newspapers
    for name, data in papers.items(): # iterate through all of the sources
        link = data['link'] # get the link
        text_current = f"-----\n\nSITE: {link}" # add the url
        if 'rss' in data:
            rss = data['rss']
            text_current += f"\nRSS: {rss}" # add the rss feed
        text_current += "\n\n" # new lines
        for article in data['articles']: # add the article
            title = article['title']
            published = article['published']
            content = article['text']
            text_current += f'-----\n\nTITLE: {title}\nPUBLISHED: {published}\nTEXT: {content}\n\n'
        text += text_current # add to the master

with open("plain_articles.txt", "w") as plaintext:
    plaintext.write(text) # write the file
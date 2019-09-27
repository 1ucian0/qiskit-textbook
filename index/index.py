from yaml import safe_load
from datetime import datetime


def gen_index(index_data):
    text = []
    for key, title in index_data['Index']:
        text.append("\"\\n\"")
        text.append("\"**%s**<br />\\n\"" % title)
        text.append("\"\\n\"")
        for chapter in index_data[key]:
            text.append("\"&nbsp; &nbsp; %s<br />\\n\"" % chapter)
        text.append("\"\\n\"")
    return ',\n'.join(text) + ','


def gen_contributors(index_data):
    names = []
    contributors = index_data['Contributors']
    contributors.sort(key=lambda x: list(x.keys())[0])  # Sort by surname

    for contributor in contributors:
        surname, name = list(contributor.items())[0]
        names.append("%s %s" % (name, surname))
    return ', '.join(names)

with open("index.yaml", 'r') as stream:
    index_data = safe_load(stream)

index_text = gen_index(index_data)
contributors_text = gen_contributors(index_data)
date_text = datetime.now().strftime("%B %Y")

with open('index.ipynb.part') as f:
    newText = f.read().replace('{{{index}}}', index_text).replace('{{{contributors}}}',
                                                                  contributors_text)

with open('../index.ipynb', "w") as f:
    f.write(newText)

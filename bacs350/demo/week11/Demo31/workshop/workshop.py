from csv import reader
from markdown import markdown
from os.path import exists


def lorem(num_chars):
    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium quibusdam sit hic, ipsum labore commodi eligendi quos culpa maxime voluptate. Ad, voluptatem, esse! Quam accusantium minus sequi cumque minima quod odio accusamus assumenda dolorem consequuntur esse alias nisi, explicabo error! Dolores blanditiis adipisci laboriosam quo sequi nostrum consectetur recusandae illo sed molestias laborum, ullam modi doloremque. Facilis nulla iure odit accusamus. Doloremque voluptatibus repudiandae, beatae temporibus odit suscipit eius facere dolores quibusdam perspiciatis exercitationem velit porro cupiditate repellendus et tempora dolorem, sapiente, debitis cum nihil sunt. Illo perspiciatis cumque qui quia quam quibusdam doloribus fugiat porro, soluta esse nesciunt itaque? Blanditiis, voluptate, voluptates iure iste aut maxime perferendis aliquid, odit doloribus sapiente temporibus ad mollitia consequuntur, alias totam tenetur ut. Accusantium voluptas temporibus, ea a impedit.'''
    return text[:num_chars]
    
    
def card_data(title="Random Card", body=lorem(400), color='bg-primary', width='col-lg-12'):
    html = markdown(body)
    return dict(title=title, body=html, color=color, width=width)


def cards_data():
    return [
                card_data(),
                card_data("Card Two",   lorem(150), "bg-warning", 'col-lg-4'),
                card_data("Card Three", lorem(350), "bg-success", 'col-lg-4'),
                card_data("Card Four",  lorem(500), "bg-danger",  'col-lg-4'),
            ]


def markdown_file_data(doc):
    doc = 'Documents/' + doc
    if not exists(doc):
        text = '# 404 is for Losers!'
    else:
        text = markdown(open(doc).read())
    title = f'Document - {doc}'
    card = card_data(title, text, 'bg-success', 'col-lg-12') 
    return dict(card=card)


def table_data(path):
    return [row[:5] for row in reader(open(path))]


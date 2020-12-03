from os.path import dirname, exists, join

from tool.document import doc_path
from tool.files import read_json


def read_menu_data(page, menu_file='menu.json'):
    d = page
    json = doc_path(join(d, menu_file))
    while not exists(json):
        if json == doc_path(menu_file):
            return
        d = dirname(d)
        json = doc_path(join(d, menu_file))
    return json


def load_menu(page):
    menu = read_menu_data(page)
    if menu:
        menu = read_json(menu)
        for item in menu['menu_items']:
            if page.startswith(item['page']):
                item['active'] = 'active'
        return menu


def load_side_menu(page):
    menu = read_menu_data(page, 'menu_side.json')
    if menu:
        menu = read_json(menu)
        for item in menu['menu_items']:
            if page.startswith(item['page']):
                item['active'] = 'active'
        return menu


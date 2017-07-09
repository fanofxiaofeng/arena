#!/usr/local/bin/python3

import bs4
import pprint

def get_data(source_file_name):
    soup = bs4.BeautifulSoup(open(source_file_name), 'html.parser')

    temp_table_tag = soup.new_tag('table')

    table = soup.select('table.wikitable')[0]
    trlist = table.select('tr')
    for tr in trlist:
        temp_tr_tag = soup.new_tag('tr')
        thlist = tr.find_all('th')
        tdlist = tr.find_all('td')
        thlist = thlist if len(thlist) <= 4 else thlist[:4]
        tdlist = tdlist if len(tdlist) <= 3 else tdlist[:3]
        for th in thlist:
            temp_tr_tag.append(th)
        for td in tdlist:
            temp_tr_tag.append(td)
        temp_table_tag.append(temp_tr_tag)
    return temp_table_tag

def change_href(temp_table_tag):
    linklist = temp_table_tag.find_all('a')
    for link in linklist:
        link['href'] = 'https://en.wikipedia.org' + link['href']
    return temp_table_tag


def show_data(template_file_name, result_file_name, temp_table_tag):
    soup = bs4.BeautifulSoup(open(template_file_name), 'html.parser')
    soup.body.append(temp_table_tag)

    with open(result_file_name, 'w') as f:
        f.write(soup.prettify())

temp_table_tag = get_data('arena.html')
temp_table_tag = change_href(temp_table_tag)
show_data('template.html', 'result.html', temp_table_tag)

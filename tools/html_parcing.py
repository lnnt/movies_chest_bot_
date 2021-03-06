import html
import re

def remove_tags(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return html.unescape(cleantext).replace(u'\xa0', u' ').replace('&#39;','\'').replace('&quot;','\'')

def get_middle(string, left_part, right_part):
    #print('fucking length',len(string.split(left_part)))
    try:
        return string.split(left_part)[1].split(right_part)[0]
    except IndexError:
        print('get_middle error')
        return 'n/a'

def delete_slashes(string):
    return string.replace('\\','').replace('/','')

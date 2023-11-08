from bs4 import BeautifulSoup

def strip_html_tags(html : str):
        soup = BeautifulSoup(html, 'html.parser')
        stripped_text = soup.get_text()
        text = stripped_text.splitlines()
        
        return ''.join(text).replace('  ',' ').replace('\xa0', '').replace('\t', '')


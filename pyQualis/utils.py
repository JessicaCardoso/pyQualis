import os
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

_ROOT = os.path.abspath(os.path.dirname(__file__))
_url = 'https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.xhtml'

def _get_event_option(page, keyword="quadriênio"):
    keyword = keyword.upper()   
    soup = BeautifulSoup(page.text, 'html.parser')
    options = soup.find('select', {'id': 'form:evento'}).findAll("option")[1:]
    for op in options:
        if keyword in op.get_text():
            return op.get("value")

    return None


def _download_data(keyword="quadriênio"):

    if keyword.lower() not in ['quadriênio', 'triênio']:
        return
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate, br'}


    data = {'form' : 'form',
            'form:area': 0,
            'form:estrato' : 0,
            'form:consultar' : 'Consultar',
        }


    with requests.session() as s: 
        # Get the cookies and the source to parse the Viewstate token
        init = s.get(_url)
        soup = BeautifulSoup(init.text, 'html.parser')
        data['form:evento'] = _get_event_option(init, keyword)
        val = soup.find('input', {'id': 'javax.faces.ViewState'}).get('value')
        data["javax.faces.ViewState"] = val
        r = s.post(_url, data=data)
        # Get current page
        page = BeautifulSoup(r.text, "lxml")
        # Get the field of the file
        field_file = page.select_one("td > a")['onclick']
        file_download = re.compile(r'form:j_idt\d+') 
        field_file = file_download.search(field_file)
        field_file = field_file.group()
        data[field_file] = field_file
        # Download the table
        r = s.post(_url, data=data, stream=True, headers=headers)
        with open(os.path.join(_ROOT, f"data/{keyword}.tsv"), 'wb') as output:
            output.write(r.content)
            output.close()



def _download_all():
    _download_data("triênio")
    _download_data("quadriênio")
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open(os.path.join(_ROOT, "data/last-update.txt"), 'w') as text_file:
        text_file.write(dt_string)
        text_file.close()

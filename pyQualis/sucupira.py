import pandas as pd
import os
from .utils import _download_all

_ROOT = os.path.abspath(os.path.dirname(__file__))

class Search:

    def __init__(self):
        # load files from folder
        self._load_data()
        
    def _load_data(self):
        self.trien = pd.read_csv(os.path.join(_ROOT, "data/triênio.tsv"), 
                                 encoding = "ISO-8859-1", sep="\t")
        self.quadr = pd.read_csv(os.path.join(_ROOT, "data/quadriênio.tsv"), 
                                 encoding = "ISO-8859-1", sep="\t")
        with open(os.path.join(_ROOT, "data/last-update.txt"), "r") as text_file:
            self.last_update = text_file.read()
            text_file.close()

    def _filter_by(self, key, value, event):
        value = value.upper()
        if event == "triênio":
            return self.trien[self.trien[key].str.contains(value)]
        elif event == "quadriênio":
            return self.quadr[self.quadr[key].str.contains(value)]

    def get_last_update(self):
        return self.last_update


    def update_data(self):
        _download_all()
        self._load_data()
        print(self.last_update)


    def get_table(self, event="triênio"):
        if event == "triênio":
            return self.trien
        elif event == "quadriênio":
            return self.quadr

    def by_area(self, area, event="triênio"):
        return self._filter_by("Área de Avaliação", area, event)


    def by_title(self, title, event="triênio"):
        return self._filter_by("Título", title, event)


    def by_issn(self, issn, event="triênio"):
        return self._filter_by("ISSN", issn, event)


    def by_classification(self, value, event="triênio"):
        return self._filter_by("Estrato", value, event)
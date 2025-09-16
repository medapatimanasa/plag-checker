from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import lxml
import warnings

class Paper:
    def __init__(self, path: str) -> None:
        self.path = path
        self.json = json.load(open(path, encoding='utf-8'))
        self.title = self.json['articleTitle']
        self.number = self.json['articleNumber']
        self.authors = self.json['authors']
        self.abstract = self.json['abstract']
        self.text = self._get_text()

    def __str__(self) -> str:
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'

    def _get_text(self) -> str:
        warnings.filterwarnings("ignore", category=UserWarning, message=re.escape(
            "It looks like you're parsing an XML document using an HTML parser. If this really is an HTML document (maybe it's XHTML?), you can ignore or filter this warning. If it's XML, you should know that using an XML parser will be more reliable. To parse this document as XML, make sure you have the lxml package installed, and pass the keyword argument `features=\"xml\"` into the BeautifulSoup constructor."))
        soup = BeautifulSoup(self.json['xml'], 'lxml')
        text = self.abstract + "\n" + "\n".join([p.text for p in soup.find_all('p')])
        return self._clean_text(text)

    def _clean_text(self, text: str) -> str:
        """
        arg(s) : The input text is the xml component of the json object with the key `xml`
        return(s) : Return the cleaned text without the xml tags
        """
        regex = r"CCBY - IEEE.*|\[\d+\]|\$.*\$|View Source.*|\\begin.*|FIGURE \d+|Fig. \d+|[^A-Za-z0-9^ ]|SECTION [A-Z]+|\t\t|\n|Eq \d+|  "
        regex_empty = r" +"
        regex_eqns = r"Eq \d+|Lemma \d+|section \d+|section \d+ \d+|From \d+|Eqs[^a-z^A-Z]+"
        result = re.sub(regex, " ", text, 0, re.MULTILINE)
        result = re.sub(regex_empty, " ", result, 0, re.MULTILINE)
        result = re.sub(regex_eqns, "", result, 0, re.MULTILINE).strip()
        return result

    def __dict__(self):
        return {"title" : f"{self.title}",
        "number" : f"{self.number}" ,
        "authors": f"{self.authors}" ,
        "abstract" : f"{self.abstract}",
        "text" : f"{self.text}"}

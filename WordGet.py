import requests
import yaml
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import time

from GetSess import GetSess
from SeleniumGet import SeleniumGet

class WordGet:

    def __init__(self):
        self.url = WordGet.getConfig()["url"]
        self.searchWord = "밥"

    def urlReq(self):
        chromeObj = SeleniumGet.getObj()

        urlpath = urlencode({
            "a": "dic.kr"
        })
        dictUrl = self.url +"?"+ urlpath
        chromeObj.get(url=dictUrl)
        chromeObj.implicitly_wait(3)
        htmlTitle = chromeObj.title
        print(htmlTitle)

        chromeObj.find_element_by_css_selector("input#ac_input").send_keys(self.searchWord)
        time.sleep(1)
        chromeObj.find_element_by_css_selector("a.btn_search").click()
        time.sleep(1)
        w = chromeObj.find_element_by_css_selector("span.c_b > strong")
        print(w.text)
        #================================
        chromeObj.close()
        chromeObj.quit()

    """
    def byBs4(self):

        sess = GetSess.reqObjGet()
        #================================
        urlpath = urlencode({
            "range": "word",
            "query": "밥"
        })
        url = "https://ko.dict.naver.com/#/search"

        dictUrl = url + "?" + urlpath
        print(dictUrl)
        try:
            html = sess.get(dictUrl)
        except requests.exceptions.ConnectionError as err:
            print(err)
        else:
            if html.status_code == 200 and html.ok:
                bsObj = BeautifulSoup(html.text, "html.parser")
                print(bsObj)
        finally:
            #================================
            sess.close() """

    @classmethod
    def getConfig(cls):
        try:
            f=open("./config/info.yml", "r", encoding="utf-8")
        except FileNotFoundError as err:
            print(err)
            exit(1)
        else:
            info = yaml.safe_load(f)
            f.close()
            return info

if __name__ == "__main__":
    o = WordGet()
    o.urlReq()
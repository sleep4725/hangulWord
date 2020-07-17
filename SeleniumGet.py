from selenium import webdriver

class SeleniumGet:

    """ headless 로 chromeObject를 리턴
    """
    @classmethod
    def getObj(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("disable-gpu")

        ## headless 적용
        #chromeDriver = webdriver.Chrome(executable_path="./config/chromedriver.exe", chrome_options=options)
        ##
        chromeDriver = webdriver.Chrome(executable_path="./config/chromedriver.exe")
        return chromeDriver
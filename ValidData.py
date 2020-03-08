import requests
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class ValidData:
    def __init__(self, rfc, ciec):
        self.rfc = rfc
        self.ciec= ciec
        self.urlCiec = 'https://portalsat.plataforma.sat.gob.mx/SATauthenticator/AuthLogin/AuthLogin/askLogin.action?'
        self.downloadUrl = 'https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/'
        self.mime_types = 'application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml'
    
    def downloadFile(self):
        result = False
        options = Options()
        options.headless = True
        options.add_argument('download.default_directory=C:\Server\htdocs\Python\Examen\download')

        fp = webdriver.FirefoxProfile()
        fp.set_preference('browser.download.folderList', 2)
        fp.set_preference('browser.download.manager.showWhenStarting', False)
        fp.set_preference('browser.download.dir', 'C:\Server\htdocs\Python\Examen\download')
        fp.set_preference('browser.helperApps.neverAsk.saveToDisk', self.mime_types)
        fp.set_preference('plugin.disable_full_page_plugin_for_types', self.mime_types)
        fp.set_preference('pdfjs.disabled', True)

        try:
            driver = webdriver.Firefox(options=options,firefox_profile=fp, executable_path='C:\Server\htdocs\Python\Examen\geckodriver\geckodriver.exe')
            driver.get(self.downloadUrl)
            downloadFile = driver.find_element_by_css_selector('tr.even a.btn-orange')
            downloadFile.click()
            driver.quit()
            result = True
        except:
            result = False
        return result

    def rfcCiecValidator(self):
        try: 
            response = requests.post(self.urlCiec, data={'rfc':self.rfc,'password':self.ciec})
            
            if response.text.find('https') != -1:
                return True
            else:
                return False
        except:
            return False

rfc = sys.argv[1]
ciec = sys.argv[2]

validObj = ValidData(rfc,ciec)
result = validObj.rfcCiecValidator()#return true or false 
isDownloadedFile = validObj.downloadFile()#return true or false 

print( 'The data is Valid' if result else 'Invalid data' )#custom message
print( 'The file was downloaded successfully' if isDownloadedFile else 'Error to download' )#custom message
from selenium import webdriver
from time import sleep

class CveBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def goToPage(self):
        self.driver.get('https://www.cvedetails.com/')
    def goToHome(self):
        homeButton = self.driver.find_element_by_xpath('//*[@id="mainmenu"]/a[1]')
        homeButton.click()

        sleep(5)
    def SearchSSH(self):
        searchBox = self.driver.find_element_by_xpath('//*[@id="unifiedsearchinput"]')
        searchBox.send_keys('SSH')

        sleep(2)

        searchButton = self.driver.find_element_by_xpath('//*[@id="unifiedsearchbox"]/input[2]')
        searchButton.click()

        sleep(5)

        vulnerable = self.driver.find_element_by_xpath('//*[@id="contentdiv"]/div[1]/a[1]')
        vulnerable.click()

        sleep(5)
    def SearchFTP(self):
        searchBox = self.driver.find_element_by_xpath('//*[@id="unifiedsearchinput"]')
        searchBox.send_keys('FTP')

        sleep(2)

        searchButton = self.driver.find_element_by_xpath('//*[@id="unifiedsearchbox"]/input[2]')
        searchButton.click()

        sleep(5)

        vulnerable = self.driver.find_element_by_xpath('//*[@id="contentdiv"]/div[1]/a[2]')
        vulnerable.click()

        sleep(5)
    
    

bot = CveBot()
bot.goToPage()
bot.SearchSSH()
bot.goToHome()
bot.SearchFTP()
bot.goToHome()
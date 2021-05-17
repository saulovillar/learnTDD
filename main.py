from selenium import webdriver

if __name__ == "__main__":

    chrome = webdriver.Chrome("chromedriver.exe")
    chrome.get("https://google.com/")





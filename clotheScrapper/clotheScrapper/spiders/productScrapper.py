import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from time import sleep

class ProductscapperScrapper(scrapy.Spider):
    name = "productscrapper"

    def start_requests(self):

        url ="https://www.lazada.com.my/tag/denims/?spm=a2o4k.home-my.search.d_go&q=denims&catalog_redirect_tag=true"
        driver = webdriver.Chrome()
        #navigate to the site
        driver.get(url)

        sleep(5)
        # button=driver.find_element(By.XPATH,'//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[2]/article/div[1]/a')
        # driver.execute_script("window.scrollBy(0, 2000)")
        # sleep(2)
        # button.send_keys(Keys.RETURN)
        # sleep(2)
        # driver.close()

        #find the h1 element
        link_elements = driver.find_elements(By.CSS_SELECTOR, "div.Bm3ON a")
        links=[]
        for link_element in link_elements:
            link=link_element.get_attribute('href')
            print(f'##########------{link}')
            links.append(link)
        driver.quit()
        
       
       

        # print(f"button element: {button.text}")

    def parse(self, response):
        print('##############3')
        print(response)
        pass
    #     print(response)
    #     quotes=response.css('div.quote')
    #     print('##############################')
    #     print(quotes)
    #     for quote in quotes:
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('small.author::text').get()
    #             # 'tags': quote.css('div.tags a.tag::text').getall()
    #         }
			

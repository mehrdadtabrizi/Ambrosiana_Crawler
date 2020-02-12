from bs4         import BeautifulSoup
from selenium    import webdriver
from collections import OrderedDict
from urllib      import request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as EC
from selenium.webdriver.common.by  import By
import time
import Parameters
import csv
from random import randint

def browser_open():
    driver = webdriver.Firefox(executable_path=Parameters.Firefox_Driver_PATH)
    return driver

def browser_open_url(browser, url) :
    browser.get(url)
    return browser

def get_html_page(browser):
    res = browser.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(res, 'lxml')
    return soup

def go_to_next_page(browser):
    try:
        page_change = browser.find_element_by_xpath('//*/a[@rel="next"]')
        if page_change is not None:
            page_change.click()
            return  browser
    except:
        return False

def search_for_keyword(browser):
    print("Searching for the Keyword " + Parameters.KEYWORD + "...")
    browser = browser_open_url(browser,Parameters.search_URL)
    time.sleep(5)
    print("Searching is done!")
    return  browser

def extract_page_links(browser):
    page_links = []
    container_tags = browser.find_elements_by_xpath('//*/div[@style="padding: 8px 0px;"]/a')
    if container_tags is not None:
        for item in container_tags:
            try:
                link = item.get_attribute('href')
                if link is not None:
                    page_links.append(link)
                    print(link)
            except:
                link = ''

    return page_links

def save_links(browser):
    NEXT_PAGE_EXISTS = True
    current_page = 0
    all_links = []
    f = open(Parameters.LINKS_File_PATH, "w+")
    while (NEXT_PAGE_EXISTS):
        current_page += 1
        print("Extracting the item links of page " + str(current_page) + " ...")
        page_links = extract_page_links(browser)
        for link in page_links:
            f = open(Parameters.LINKS_File_PATH, "a")
            f.write(link + "\n")
        NEXT_PAGE_EXISTS = go_to_next_page(browser)


def extract_item_metadatas(browser,link):
    item_metadata = {}
    title = ''
    file_name = ''
    artist = ''
    date = ' '
    genre = ''
    material = ''
    subtitle = ''
    location = ''
    image_url = ''
    image_tag = ""
    repository = ''
    bibliography = ''

    soup  = get_html_page(browser)
    wait = WebDriverWait(browser, 10)
    table = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*/div[@style="margin-left: 40px;"]/dl')))
    if table is not None:
        tags = soup.find('div', {'style': 'margin-left: 40px;'}).find_all('dl')
        for tag in tags:
            label = tag.find('dt').text
            value = tag.find('dd').text
            if "ARTIST" in label:
                artist = value

            if "TITLE" in label:
                title = value
            if "MEDIUM" in label:
                material = value
            if "SUBJECT KEYS" in label:
                subtitle = value
            if "BIBLIOGRAPHY" in label:
                bibliography = value
            if "INVENTORY SHELFMARK" in label:
                repository = value

    wait2 = WebDriverWait(browser, 20)
    image_box = wait2.until(EC.presence_of_element_located((By.XPATH, '//*/div[@class="item-detail-zoom"]/img')))
    if image_box is not None:
        try:
            image_tag = browser.find_element_by_xpath('//*/div[@class="item-detail-zoom"]/img')
            image_url = image_tag.get_attribute('src')
        except:
            pass

    file_name = "Ambrosiana_" + Parameters.Iconography + str(randint(1000,9999)) + "_" + image_url.split('/')[-1]
    if not Parameters.Images_are_already_downloaded:
        try:
            download_image(image_url,file_name)
        except:
            pass

    print('Image URL          :' + image_url)
    print('Title              :' + title)
    print('Artist             :' + artist)
    print('Repository Number  :' + repository)
    print('Material           :' + material)
    print('Subtitle           :' + subtitle)
    print('File Name          :' + file_name)


    item_metadata = {
                'Iconography'       : Parameters.Iconography,
                'Branch'            : 'ArtHist',
                'Photo Archive'     : Parameters.base_url,
                'File Name'         : file_name,
                'Title'             : title,
                'Additional Information'  : subtitle,
                'Artist'            : artist,
                'Earliest Date'     : date,
                'Original Location' : location,
                'Genre'             : genre,
                'Repository Number' : repository,
                'Material'          : material,
                'Image Credits'     : image_url,
                'Details URL'       : link,
                'Bibliography'      : bibliography
            }
    # Fixing the order of dictionary
    keyorder = Parameters.Header
    item_metadata = OrderedDict(sorted(item_metadata.items(), key=lambda i: keyorder.index(i[0])))
    print('_________________________________________________________')
    return item_metadata

def download_image(url,file_name):
    path = Parameters.Images_PATH + file_name
    request.urlretrieve(url, path)

def create_csv_file(file_path):
    keyorder = Parameters.Header
    with open(file_path, "w", encoding="utf-8") as f:
        wr = csv.DictWriter(f, dialect="excel", fieldnames=keyorder)
        wr.writeheader()

def append_metadata_to_CSV(row):
    keyorder = Parameters.Header
    with open(Parameters.CSV_File_PATH, "a", encoding="utf-8") as fp:
        wr = csv.DictWriter(fp,dialect="excel",fieldnames=keyorder)
        wr.writerow(row)

def quit_browser(browser):
    browser.quit()

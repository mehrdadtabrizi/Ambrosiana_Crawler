# Web Crawler for the Ambrosiana (https://collections.library.nd.edu) photo archive
# Author(s): Mehrdad Tabrizi, Feb. 2019
# Attention: In order to use this code, you have to have the firefox/chrome driver. You need also their path in your Hard drive.
# This crawler uses Firefox driver (geckodriver.exe)
import Parameters
import ambrosiana as am
from time import sleep
def Main():

    current_item = 0
    am.create_csv_file(Parameters.CSV_File_PATH)
    #Opens the *.txt file containing all the relevant links, and save all the links into a list
    with open(Parameters.LINKS_File_PATH) as f:
        all_links = f.read().splitlines()

    temp_browser = am.browser_open()

    #Now the process begins
    while (current_item<=len(all_links)-1):
        print("Working on item " + str(current_item))
        temp_browser = am.browser_open_url(temp_browser,all_links[current_item])
        sleep(3)
        try:
            am.append_metadata_to_CSV(am.extract_item_metadatas(temp_browser,all_links[current_item]))
        except:
            pass
        current_item += 1
    am.quit_browser(temp_browser)

if __name__ == '__main__':
    Main()

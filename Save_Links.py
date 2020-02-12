import Parameters
import ambrosiana as am

browser = am.browser_open()

browser = am.search_for_keyword(browser)
am.save_links(browser)
am.quit_browser(browser)
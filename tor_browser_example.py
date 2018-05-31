from tbselenium.tbdriver import TorBrowserDriver
from os.path import dirname, join, realpath, getsize

out_img = join(dirname(realpath(__file__)), "screenshot.png")
with TorBrowserDriver("/home/manivannan/pythonexamle/selenium_example/tor-browser_en-US") as driver:
	driver.load_url('https://check.torproject.org', wait_for_page_body=True)
	print("----"*100)
	driver.get_screenshot_as_file(out_img)
	print("----"*100)
print("Screenshot is saved as %s (%s bytes)" % (out_img, getsize(out_img)))
    # driver.get()
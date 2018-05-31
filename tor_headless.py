from tbselenium.utils import start_xvfb, stop_xvfb
from tbselenium.tbdriver import TorBrowserDriver
from os.path import join, dirname, realpath



out_img = join(dirname(realpath(__file__)), "headless_screenshot.png")
xvfb_display = start_xvfb()
with TorBrowserDriver('/home/manivannan/pythonexamle/selenium_example/tor-browser_en-US') as driver:
    driver.load_url("https://check.torproject.org")
    driver.get_screenshot_as_file(out_img)
    print("Screenshot is saved as %s" % out_img)

stop_xvfb(xvfb_display)
from Drivers.GetChorom import Chrome
from Drivers.getMozilaFireFox import Firefox
eli_testing = Chrome("https://github.com/D10Sfm")
eli_testing.openBrowser()
eli_testing.action("js-responsive-underlinenav-item","click")
salomon_testing = Firefox("https://github.com/D10Sfm")
salomon_testing.openBrowser()
import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.VendorSearch import VendorSearch
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchVendorByname_006:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_searchVendorByname(self,setup):
        self.logger.info("************* SearchVendor_006 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Vendor By Name **********")

        searchvend = VendorSearch(self.driver)
        searchvend.clickOnCustomersMenu()
        time.sleep(2)
        searchvend.clickOnVendorMenu()
        time.sleep(2)
        searchvend.setVendorname("Vendor 1")
        searchvend.clickSearch()

        status=searchvend.searchVendorByName("Vendor 1")
      #status1=self.searchvend.setVendoremail("vendor1email@gmail.com")
     #   self.driver.close()
        assert True==status
        print(status)
        #assert True==status1

        self.logger.info("***************  TC_SearchVendorBYName_006 Finished  *********** ")
        self.driver.close()
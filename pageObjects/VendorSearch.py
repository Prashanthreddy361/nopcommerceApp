import time
from selenium.webdriver.support.ui import Select

class VendorSearch:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkVendorSearch_xpath = "//span[contains(text(),'Vendors')]"
    txtVendorname_xpath = "//input[@id='SearchName']"
    txtVendoremail_xpath = "//input[@id='SearchEmail']"
    btnSearch_xpath = "search-vendors"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='vendors-grid']"
    tableRows_xpath = "//table[@id='vendors-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='vendors-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnVendorMenu(self):
        self.driver.find_element_by_xpath(self.lnkVendorSearch_xpath).click()

    def setVendorname(self,vname):
        self.driver.find_element_by_xpath(self.txtVendorname_xpath).send_keys(vname)

    def setVendoremail(self,email):
        self.driver.find_element_by_xpath(self.txtVendoremail_xpath).send_keys(email)

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))
    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_xpath).click()

    def searchVendorByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          name=table.find_element_by_xpath("//table[@id='vendors-grid']/tbody/tr["+str(r)+"]/td[1]").text
          if name == Name:
              flag = True
              break
        return flag
    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
          table=self.driver.find_element_by_xpath(self.table_xpath)
          emailid=table.find_element_by_xpath("//table[@id='vendors-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag
from ZipangAutoV2 import ZiapngAutoV2_Workflow
import pytest
import allureReport

class Test_Login:

    @pytest.mark.login
    def test_login(self,driver):

        app = ZiapngAutoV2_Workflow(driver)
        app.allow_Permission()
        app.Open_LoginPage()
        app.Login("jagadeesh.yadav@sysquare.in", "password")

    def test_pre_bid(self,driver):
        PB = ZiapngAutoV2_Workflow(driver)
        PB.pre_bid("2100")
        PB.Assertion_pre_bid("2467124122","154.53911452") # Check the exchange rate if it is different from change it first than try otherwise the test will fails

    def test_cancel_prebid(self,driver):
        PB = ZiapngAutoV2_Workflow(driver)
        PB.cancel_prebid() # This will not work if the phase is guest user or past auction

    def test_NR(self,driver):
        NR = ZiapngAutoV2_Workflow(driver)
        NR.NR() # This will not work in past auction


    def test_Search(self,driver):
        SE = ZiapngAutoV2_Workflow(driver)
        SE.Search("1")

    def test_Export(self,driver):
        EX = ZiapngAutoV2_Workflow(driver)
        EX.Export()

    def test_Certificate(self,driver):
        cert = ZiapngAutoV2_Workflow(driver)
        cert.Certificate()

    def test_WatchList(self,driver):
        watch = ZiapngAutoV2_Workflow(driver)
        watch.Watchlist()

    def test_Sort(self,driver):
        sort = ZiapngAutoV2_Workflow(driver)
        sort.Sort()

    def test_Notes(self,driver):
        note = ZiapngAutoV2_Workflow(driver)
        note.notes("7","Version 2")

    def test_Long_Press(self,driver):
        LongPress = ZiapngAutoV2_Workflow(driver)
        LongPress.Long_Press("8")
        LongPress.Bulk_Bid("100","7")

    def test_Filter(self,driver):
        filter = ZiapngAutoV2_Workflow(driver)
        filter.Filter_Diamond("100","50000")

    def test_parcelFilter(self,driver):
        Parcel = ZiapngAutoV2_Workflow(driver)
        Parcel.Parcel_filter("100","1000")



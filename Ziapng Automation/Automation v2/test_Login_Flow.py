from ZipangAutoV2 import ZiapngAutoV2_Workflow


class Test_Login:

    # @pytest.mark.login
    # def test_login(self,driver):
    #
    #     app = ZiapngAutoV2_Workflow(driver)
    #     app.allow_Permission()
    #     app.Open_LoginPage()
    #     app.Login("jagadeesh.yadav@sysquare.in", "password")

    def test_pre_bid(self,driver):
        PB = ZiapngAutoV2_Workflow(driver)
        PB.pre_bid("2100")
        PB.Assertion_pre_bid("2467124122","154.05500922000002")

    def test_cancel_prebid(self,driver):
        PB = ZiapngAutoV2_Workflow(driver)
        PB.cancel_prebid()


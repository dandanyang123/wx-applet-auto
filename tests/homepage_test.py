import sys
sys.path.append("..")
from pages import homepage
from common.basecase import BaseCase
from random import randint
import minium
from element.home_page_el import *


# 小程序首页测试
@minium.ddt_class()
class HomePageTest(BaseCase):
    def __init__(self, methodName = 'runTest'):
        super(HomePageTest, self).__init__(methodName)
        self.homePage = homepage.HomePage(self)

    def test_get_wares_info(self):
        back_list = self.homePage.get_wares()
        print(back_list)
        if not self.homePage.different_result(back_list, check_wares_info):
            raise


    def test_buy_ware1(self):
        self.homePage.buy_ware()

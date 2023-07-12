# -*- coding:utf-8 -*-
from common.basepage import BaseDef
from element.home_page_el import *
from common.router import *

class HomePage(BaseDef):

    def get_wares(self):
        self.switch_to_tabbar(home_page)
        back_list = []
        for i in range(2, 5):
            info = self.mini.page.get_element(wares_info % i)
            back_list.append(info.inner_text)
        return back_list

    def buy_ware(self,):
        self.switch_to_tabbar(home_page)
        self.click(ware1_info)
        self.click(panic_buying)
        self.click(ware_size_m)
        self.click(ware_color_red)
        self.click(fix_button)
        self.click(indent_cofirm)





import minium
import time
from minium import Callback

class test(minium.MiniTest):
    def test_my(self):
        ##元素定位+点击
##        self.mini.app.navigate_to('/pages/addressList/index')
        
        self.mini.app.navigate_to('/pages/addressAdd/index')
        bindKeyName = self.page.get_element('input[placeholder="请填写姓名"]')
        bindKeyName.click()
        bindKeyName.trigger("input", {"value": "测试联系人"})

        bindKeyMobile = self.page.get_element('input[placeholder="11位手机号码"]')
        bindKeyMobile.click()
        bindKeyMobile.trigger("input", {"value": "18211110000"})

##        callback = Callback()
        picker = self.page.get_element('/page/view/view[1]/view[3]/picker')
##        self.app.hook_current_page_method("bindRegionChange", callback.callback)
        picker.click()
        picker.pick(["湖南省","长沙市","芙蓉区"])
        
        bindKeyMobile = self.page.get_element('input[placeholder="街道门牌号信息"]')
        bindKeyMobile.click()
        bindKeyMobile.trigger("input", {"value": "测试"})
        
        self.page.get_element('/page/view/view[2]').click()

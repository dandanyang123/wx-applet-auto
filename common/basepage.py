class BaseDef:
    def __init__(self, mini):
        self.mini = mini

    '''跳转到指定页面'''
    def navigate_to_open(self, route):
        self.mini.app.navigate_to(route)

    '''跳转到指定页面并关闭当前页面'''
    def redirect_to_open(self, route):
        self.mini.app.redirect_to(route)

    '''跳转到tabbar页面，关闭其他非tabbar页面'''
    def switch_to_tabbar(self, route):
        self.mini.app.switch_tab(route)

    '''跳转到非原生tabbar页面'''
    def switch_to_not_tabbar(self, selector, str=None):
        self.mini.page.get_element(selector, inner_text=str).click()

    '''无需加载的页面滑动到页面底部'''
    def scroll_to_buttom(self, selector):
        el = self.mini.page.get_element('scroll-view')
        rect = self.mini.page.get_element(selector).rect
        el.scroll_to(y=rect['top'])

    '''元素列表中找第几个元素'''
    def get_el_in_els(self, selector, index=0):
        els = self.mini.page.get_elements(selector)
        return els[index]

    '''断言每个元素文本中都包含某元素'''
    def assertIn(self, selector, text, msg=None):
        els1 = self.mini.page.get_elements(selector, text_contains=text)
        els2 = self.mini.page.get_elements(selector)
        if els1 != els2:
            raise AssertionError("selector:%s, inner_text=%s not Found")

    @property
    def current_path(self):    #返回当前路径
        return self.mini.page.path

    def click(self, ele):
        self.mini.page.get_element(ele).click()
        print("click:", ele)

    def input(self, ele, data):
        el = self.mini.page.get_element(ele)
        el.click()
        el.trigger("input", {"value": data})
        print("input:", ele)


    def different_result(self,a,b):
        if len(a) != len(b):
            return False
        for i in range(len(a)-1):
            if a[i] != b[i]:
                return False
        return True



from pathlib import Path
import minium


class BaseCase(minium.MiniTest):
    """测试用例基类"""
    @classmethod
    def setUpClass(cls):
        super(BaseCase, cls).setUpClass()
        output_dir = Path(cls.CONFIG.outputs)
        if not output_dir.is_dir():
            output_dir.mkdir()

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()

    def setUp(self):
        pass

    def tearDown(self):
        pass


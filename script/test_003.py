import allure


class Test_003:
    def test_bug_png(self):
        """添加图片.png,加入到测试报告中"""

        with open("G:\\add_pytest\\new_002.png", "rb") as f:
            # 添加图片到测试报告里,以附件的方式

            allure.attach("bug_截图", f.read(), allure.attach_type.PNG)

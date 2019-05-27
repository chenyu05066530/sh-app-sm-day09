import allure
import pytest

class Test_002:

    # @allure.step(title="这个是测试步骤01")
    # def test_002_01(self):
    #     allure.attach("支付","支付密码为中英文8个字符")
    #     print("--->test_002_01")
    #allure generate ./report -o ./report/html
    #     assert True
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这个是测试步骤02")
    def test_002_02(self):
        print("--->test_002_02")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这个是测试步骤02")
    def test_002_03(self):
        print("--->test_002_03")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这个是测试步骤02")
    def test_002_04(self):
        allure.attach("用户名","陈玉")
        allure.attach("密码", "123654")
        print("--->test_002_04")

        assert False

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这个是测试步骤02")
    def test_002_05(self):
        print("--->test_002_05")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这个是测试步骤02")
    def test_002_06(self):
        print("--->test_002_06")

        assert True


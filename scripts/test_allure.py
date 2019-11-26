import allure


class TestAllure(object):
    """测试类"""
    BLOCKER = allure.MASTER_HELPER.severity_level.BLOCKER
    CRITICAL = allure.MASTER_HELPER.severity_level.CRITICAL
    MINOR = allure.MASTER_HELPER.severity_level.MINOR
    TRIVIAL = allure.MASTER_HELPER.severity_level.TRIVIAL

    @allure.MASTER_HELPER.step(title ='测试方法01')
    @allure.MASTER_HELPER.severity(MINOR)
    def test_func(self):
        """测试方法"""
        allure.MASTER_HELPER.attach('登录','输入用户名密码')
        print("测试方法01")

    @allure.MASTER_HELPER.severity(BLOCKER)
    def test_func01(self):
        """测试方法"""
        print("测试方法02")

    @allure.MASTER_HELPER.severity(TRIVIAL)
    def test_func02(self):
        """测试方法"""
        print("测试方法03")
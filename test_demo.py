import shelve
from time import sleep

import pytest
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Testdemo:

    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome(executable_path="C:\Users\Administrator\AppData\Local\Google\Chrome
        # \Application\chrome.exe")
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)

    @pytest.mark.skip
    def test_get_cookie(self):
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.qq.com', 'expiry': 1603545509, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851343852333'},
            {'domain': '.qq.com', 'expiry': 1603631869, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1179335590.1603541906'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'qWZwAAhITy1C7g0sjM4n8_KXmmsdS0G_OAAH1Y7oJm77ogUOh3ZbsLe8yDwuwDnY'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3919431'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '5781865472'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '8951128236'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325069162854'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851343852333'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1644029624, 'httpOnly': False, 'name': '__utma', 'path': '/',
             'secure': False, 'value': '135912439.139122655.1575106162.1580957625.1580957625.1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1603545069'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '775774576361293'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603573418.376349, 'httpOnly': True, 'name': 'ww_rtkey',
             'path': '/', 'secure': False, 'value': 'n4cmg6'},
            {'domain': '.qq.com', 'expiry': 1906379124.681241, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/',
             'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'oZIbY3rMkrsFnnS3aaSwGVlLf7jIf1c8hDdwRApJCEZjj1C75HzbVH7eb1roB4BLsgR4Sku0vhKrUJTqz0gr2ipKhu1h-i17tG3SZOzFlh6t6iw9QX4tW_abOYdIKnmD8ojgt6UUQVstAOPkQgZRrtM1mdmHzYerZwMp9gw5BzunQiEZlv5RN7AZsuQc-1D3Y4E1RgairKvUZMp5mNuv-9yuMHUL-hWhvmCrdG8aQd8T1SEIkvgLzs5H-RCCPdGNDZucMgSaRiMekGRhDTnyaw'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635081069, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1603541892,1603544771,1603545061'},
            {'domain': '.qq.com', 'expiry': 1906379124.681135, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_792dcc92c8420'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1612493624, 'httpOnly': False,
             'name': 'Hm_lvt_f2ba645ba13636ba52b0234381f51cbc', 'path': '/', 'secure': False, 'value': '1580957625'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606137471.743334, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1666617469, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.139122655.1575106162'},
            {'domain': '.qq.com', 'expiry': 2147483645.959913, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
             'secure': False, 'value': '67e5bb8eadcdb2624c1d647a1651b3a7b85fff757497d0c2f320d559f467dbd5'},
            {'domain': '.qq.com', 'expiry': 1891159768, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '8b84f66802047a1f'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635077882.376414, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483650.876069, 'httpOnly': False, 'name': 'RK', 'path': '/',
             'secure': False, 'value': '5ZqJbdZMFC'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if isinstance(cookie.get("expiry"), float):
                cookie["expiry"] = int(cookie["expiry"])
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        print(cookies)

    # def test_shelve(self):
        '''
        # cookies = [
        #     {'domain': '.qq.com', 'expiry': 1603545509, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688851343852333'},
        #     {'domain': '.qq.com', 'expiry': 1603631869, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1179335590.1603541906'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'qWZwAAhITy1C7g0sjM4n8_KXmmsdS0G_OAAH1Y7oJm77ogUOh3ZbsLe8yDwuwDnY'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a3919431'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False, 'value': '5781865472'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '8951128236'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325069162854'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688851343852333'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1644029624, 'httpOnly': False, 'name': '__utma', 'path': '/',
        #      'secure': False, 'value': '135912439.139122655.1575106162.1580957625.1580957625.1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1603545069'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '775774576361293'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603573418.376349, 'httpOnly': True, 'name': 'ww_rtkey',
        #      'path': '/', 'secure': False, 'value': 'n4cmg6'},
        #     {'domain': '.qq.com', 'expiry': 1906379124.681241, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/',
        #      'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'oZIbY3rMkrsFnnS3aaSwGVlLf7jIf1c8hDdwRApJCEZjj1C75HzbVH7eb1roB4BLsgR4Sku0vhKrUJTqz0gr2ipKhu1h-i17tG3SZOzFlh6t6iw9QX4tW_abOYdIKnmD8ojgt6UUQVstAOPkQgZRrtM1mdmHzYerZwMp9gw5BzunQiEZlv5RN7AZsuQc-1D3Y4E1RgairKvUZMp5mNuv-9yuMHUL-hWhvmCrdG8aQd8T1SEIkvgLzs5H-RCCPdGNDZucMgSaRiMekGRhDTnyaw'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1635081069, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #      'value': '1603541892,1603544771,1603545061'},
        #     {'domain': '.qq.com', 'expiry': 1906379124.681135, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #      'secure': False, 'value': '0_792dcc92c8420'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1612493624, 'httpOnly': False,
        #      'name': 'Hm_lvt_f2ba645ba13636ba52b0234381f51cbc', 'path': '/', 'secure': False, 'value': '1580957625'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1606137471.743334, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.qq.com', 'expiry': 1666617469, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.139122655.1575106162'},
        #     {'domain': '.qq.com', 'expiry': 2147483645.959913, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
        #      'secure': False, 'value': '67e5bb8eadcdb2624c1d647a1651b3a7b85fff757497d0c2f320d559f467dbd5'},
        #     {'domain': '.qq.com', 'expiry': 1891159768, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
        #      'secure': False, 'value': '8b84f66802047a1f'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1635077882.376414, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.qq.com', 'expiry': 2147483650.876069, 'httpOnly': False, 'name': 'RK', 'path': '/',
        #      'secure': False, 'value': '5ZqJbdZMFC'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'}]
        # shelve是python内置数据库，持久性存储的库，相当于一个小型的数据库
        # 可以通过key，value来把数据保存到shelve中
        # db = shelve.open("cookies")    # 创建cookies的数据库
        # db["cookie"] = cookies
        # db.close()
        '''

    def test_get_cookie_shelve(self):
        db = shelve.open("cookies")
        cookies = db["cookie"]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if isinstance(cookie.get("expiry"), float):
                cookie["expiry"] = int(cookie["expiry"])
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys('C:\\Users\\Administrator\\Desktop\\test001.xlsx')
        sleep(3)
        filenema = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        print(filenema)
        assert "test001.xlsx" == filenema


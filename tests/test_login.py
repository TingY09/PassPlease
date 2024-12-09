import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLoginLogout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """初始化瀏覽器，執行所有測試前的設置"""
        options = Options()
        options.add_argument("--headless")  # 啟用 headless 模式
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        cls.driver.get("https://0a1e-61-216-55-185.ngrok-free.app/login")  # 替換成實際 URL
        cls.wait = WebDriverWait(cls.driver, 15)

    def test_login_and_logout(self):
        """測試登入並登出操作"""
        try:
            # 等待並點擊 'Visit Site' 按鈕
            visit_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Visit Site')]"))
            )
            visit_button.click()
            time.sleep(2)  # 等待頁面過渡效果

            # 輸入用戶名
            username_input = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_input.clear()  # 清空輸入框
            username_input.send_keys("B")  # 替換成實際的使用者名稱

            # 輸入密碼
            password_input = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_input.clear()  # 清空輸入框
            password_input.send_keys("B1234567")  # 替換成實際的密碼

            # 點擊登入按鈕
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            login_button.click()

            # 驗證登入是否成功
            submit_button_next = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-next")))
            submit_button_next.click()
            time.sleep(1)  # 等待頁面過渡效果
            print("成功登入")

            # 驗證是否成功登入
            self.assertTrue(self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-next"))))

            # 點擊登出按鈕
            logout_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-danger")))
            logout_button.click()

            # 確認登出成功
            print("登出成功")
            time.sleep(2)

        except Exception as e:
            self.fail(f"操作出現問題: {e}")

    @classmethod
    def tearDownClass(cls):
        """測試結束後關閉瀏覽器"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
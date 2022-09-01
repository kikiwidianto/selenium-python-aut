import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

# =====LOGIN====        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', text_atas)
        self.assertEqual(text_bawah, 'Anda Berhasil Login')

    def test_b_failed_login_by_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("hahahoho") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', text_atas)
        self.assertEqual(text_bawah, 'Email atau Password Anda Salah')

    def test_c_failed_login_by_wrong_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("ujang@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', text_atas)
        self.assertEqual(text_bawah, 'Email atau Password Anda Salah')

    def test_d_failed_login_with_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("ujangspeed") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").get_attribute("validationMessage")

        self.assertIn('Please include', text_atas)

    def test_e_failed_login_empty_email_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Login!')

#=====REGISTER=====
    def test_f_register_success(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#name_register").send_keys("juan baratheon") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#email_register").send_keys("juango@tester.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("juantester") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', text_atas)
        self.assertEqual(text_bawah, 'created user!')

    def test_g_register_failed_email_registered(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("cecep baratheon") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("cecepgo@tester.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("ceceptester") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_h_register_failed_empty_name(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("cecepgo@tester.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("ceceptester") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_i_register_failed_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("cecep baratheon") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("ceceptester") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_j_register_failed_empty_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("cecep baratheon") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("cecepgo@tester.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')    

    def test_k_register_failed_empty_name_email_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_l_register_failed_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("cecep baratheon") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("cecepgotester.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("ceceptester") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

    def test_m_register_failed_max_name(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("cecepbaratheonmichaelyudisnugrahamaulana") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("cecepgo@tester.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("ceceptester") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_n_success_forgot_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://automationpractice.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.CLASS_NAME,"login").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[1]/a").click() # klik forgot password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/form/fieldset/div/input").send_keys("asago@tester.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/form/fieldset/p/button/span").click() # klik tombol retrieve password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/ul/li/a/span").click() # klik tombol back to login
        time.sleep(1)

    def test_o_success_cart(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://automationpractice.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[4]/div/div[2]/div[2]/a[1]/span").click() # klik barang
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/span").click() # klik tutup pop-up
        time.sleep(3)

        # validasi
        text = browser.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/h2").text
        self.assertTrue('Product successfully added to your shopping cart', text)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
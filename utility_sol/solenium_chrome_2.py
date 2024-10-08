from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for login button to be clickable
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "login_button_name")))

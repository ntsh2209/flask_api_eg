from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def download_file(username, password, login_url, download_url):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (without opening the browser)
    
    # Specify download directory
    download_dir = "/path/to/download/folder"
    
    prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    
    # Specify path to your ChromeDriver
    chrome_driver_path = "/path/to/chromedriver"  # Modify to your local chromedriver path
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
    
    try:
        # Navigate to the login page
        driver.get(login_url)
        
        # Wait for page to load
        time.sleep(2)
        
        # Enter username and password
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        
        # Submit the form (you may need to adapt this part based on the website's structure)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        
        # Wait for login to complete
        time.sleep(2)
        
        # Navigate to the download link page
        driver.get(download_url)
        
        # Wait for the download to start (if necessary)
        time.sleep(5)  # You can increase or decrease this time based on the site's response

        print(f"File downloaded to: {download_dir}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # User credentials and URLs
    username = "your_userid"
    password = "your_password"
    login_url = "https://example.com/login"  # Replace with the actual login page URL
    download_url = "https://example.com/path_to_file"  # Replace with the link to the file you want to download
    
    # Call the function to download the file
    download_file(username, password, login_url, download_url)

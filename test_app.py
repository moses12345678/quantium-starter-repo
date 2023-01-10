from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_header_and_vis(dash_duo):
    driver = dash_duo.driver
    driver.get("http://localhost:8050/")
    # Check the header text
    header = driver.find_element_by_tag_name("h1")
    assert header.text == "Soul Foods’s Data Visualization"
    # Check the visualization component
    wait = WebDriverWait(driver, 10)
    vis = wait.until(EC.presence_of_element_located((By.ID, "visualisation")))
    assert vis.is_displayed()


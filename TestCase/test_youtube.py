from selenium.webdriver.common.by import By
def test_youtube_search_1st(setup):
    driver=setup
    driver.find_element(By.XPATH,"//input[@id='search']").send_keys("salman khan")
    driver.find_element(By.XPATH,"(//span[@class='yt-icon-shape yt-spec-icon-shape'])[11]").click()

def test_you_tube_search_2nd(setup):
    driver=setup
    driver.find_element(By.XPATH, "//input[@id='search']").send_keys("carryminati")
    driver.find_element(By.XPATH, "(//span[@class='yt-icon-shape yt-spec-icon-shape'])[11]").click()

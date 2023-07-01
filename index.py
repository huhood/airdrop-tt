

def scroll_addnetwork(driver):

    # 这里直接访问其他的唤起小狐狸钱包会失败，调用scroll后就成功了，打个问号？
    scroll_url = 'https://scroll.io/alpha/'
    driver.get(scroll_url)

    print('开始添加scroll测试网...')
    ele = findElementXpath(driver, '//*[@id="root"]/div/div[1]/div[1]/div[2]/dl/div[2]/div[2]/dd/ul/li/div[2]/a')
    if ele is None:
        print('按钮不可见...')
        return
    ele.click()


    print('点击添加小狐狸钱包...')
    time.sleep(3)

    # shadow_root 获取示例代码
    ele = driver.find_element(By.XPATH, '/html/body/onboard-v2')
    shadow_root = ele.shadow_root
    ele = shadow_root.find_elements(By.CLASS_NAME, 'wallet-button-styling')
    if len(ele) > 0:
        ele[0].click()
    else:
        print('未找到钱包选择按钮')

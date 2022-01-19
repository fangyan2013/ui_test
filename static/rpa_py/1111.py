from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://192.168.3.185/dpa/login
    page.goto("http://192.168.3.185/dpa/login")

    # Click [placeholder="请输入账号"]
    page.click("[placeholder=\"请输入账号\"]")

    # Fill [placeholder="请输入账号"]
    page.fill("[placeholder=\"请输入账号\"]", "fy")

    # Click img[alt="右边背景图"]
    page.click("img[alt=\"右边背景图\"]")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click img[alt="右边背景图"]
    page.click("img[alt=\"右边背景图\"]")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="http://192.168.3.185/dpa/workflow/workflowList"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [placeholder="请输入标题"]
    page.click("[placeholder=\"请输入标题\"]")

    # Fill [placeholder="请输入标题"]
    page.fill("[placeholder=\"请输入标题\"]", "1111")

    # Click text=请选择 无匹配数据 加载中 >> span
    page.click("text=请选择 无匹配数据 加载中 >> span")

    # Click form >> text=执行>Test>3.185
    page.click("form >> text=执行>Test>3.185")

    # Click button:has-text("确认")
    # with page.expect_navigation(url="http://192.168.3.185/dpa/workflow/edit?modelId=mdb0a203&execId=ee1607331978343&modelName=1111&changeProcess=false&execIp=192.168.3.185&createUser=ui170800&instanceId="):
    with page.expect_navigation():
        page.click("button:has-text(\"确认\")")

    # Click #workflowEditMain >> text=API
    page.click("#workflowEditMain >> text=API")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

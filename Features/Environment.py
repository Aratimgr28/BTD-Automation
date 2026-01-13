from selenium.webdriver import Firefox

def before_scenario(context,scenario):
    context.driver=Firefox()

def after_scenario(context,scenario):
    context.driver.close()
from selenium import webdriver
capabilities = {
  'chromeOptions': {
    'androidPackage': 'com.android.chrome',
  }
}

def before_feature(context, feature):

    context.driver = webdriver.Remote('http://localhost:9515', capabilities)


def after_feature(context, feature):
    context.driver.quit()
    # subprocess.Popen.terminate(context.tunnel_proc)

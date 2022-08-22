import time, re
from selenium import webdriver 

def getBrowserEmail(link):

  options = webdriver.ChromeOptions()
  options.binary_location = "<path to chrome.exe>" # Select a path where chrome.exe is located
  driver = webdriver.Chrome("<path to chromedriver.exe>", chrome_options=options) # Select a path where chromedriver.exe is located

  driver.get(link) # Fetching page

  # Adding 'http:/' to link if not found
  if 'http://' not in link[:10].lower() and 'https://' not in link[:10].lower():
    link = 'http://'+link

  while True:
    time.sleep(3) # Waiting for the resources to fully load

    try:
      body = driver.find_element_by_tag_name('body')
      links = body.find_element_by_tag_name('a')
      try:
        for link in links:
          url = link.attrs['href'].lower()
          if 'mailto' in url:
            return url.split(':')[1]
          elif '@' in link.get_text():
            match = re.findall(r'[\w\.-]+@[\w\.-]+', link.text)
            if match:
              return match   
      except:
          pass

      match = re.findall(r'[\w\.-]*@[\w\.-]+', body.text)
      if driver.current_url == link and match:
        return match
      else:
         print('NULL')

    except:
      return "Browser was either cancelled or not found!"

# Example
print(getBrowserEmail('https://blog.codinghorror.com/about-me/'))

# OUTPUTS
# 'NULL/<email>' (It will return 'NULL' forever unless an email is found)
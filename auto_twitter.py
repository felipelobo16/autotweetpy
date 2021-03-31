from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, random, sys

# options para o chrome + random user-agent #

senha = 'password'
login = 'login'


def relogio(segundos):
    for i in range(segundos, 0, -1):
        time.sleep(1)
        print('falta %d segundos' % i, end='\r')

def main():

    agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.78 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:79.0) Gecko/20100101 Firefox/75.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4324.192 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:69.2.1) Gecko/20100101 Firefox/69.2',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4324.192 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1'
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4324.192 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4324.192 Safari/537.36']

    r1 = random.randrange(len(agent)) - 1

    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument('user-agent={}'.format(agent[r1]))
    PATH = "/home/ubuntu/Desktop/chromedriver"
    driver = webdriver.Chrome(PATH, options=chrome_options)

    driver.get('https://twitter.com/login')
    time.sleep(3)

    l = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body/div[@id="react-root"]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]/div[1]/div[2]/div[1]/input[1]')))
    l.send_keys(login)
    s = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//body/div[@id="react-root"]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/label[1]/div[1]/div[2]/div[1]/input[1]')))
    s.send_keys(senha)
    driver.find_element_by_xpath('//body/div[@id="react-root"]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/span[1]/span[1]').click()
    time.sleep(5)

    num = 0

    print('Começando a tweetar')

    #f = open("tweet", "w")
    #f.write("XXXXXXXXXXXXXXX START XXXXXXXXXXXXXXX\n")
    #f.close()

    while True:
        tweets = open('tweet', 'r')
        r = tweets.readlines()
        tweets.close()
        tweet = r[num]


        if tweet == r[-1]:
            time.sleep(0.1)

        else:
            try:
                send = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body/div[@id="react-root"]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]')))
                send.send_keys(tweet.encode('utf-8'))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Tweetar')]"))).click()
                num += 1
                print('tweet: {}'.format(tweet))

            except Exception as e:
                driver.get('https://twitter.com/home')
                print(e)

if __name__ == "__main__":
    main()

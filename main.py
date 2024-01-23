from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


search_phrase = input("Enter a search phrase: ")

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")
    cookies = {
        '_GRECAPTCHA': '09ANjddZZPOzjiD4ZGnYBWXSsdEAj-kRuS8Y9f2FhyaZwp35J7sLFf94h9UCS_i-tnTpNaP_jBEjl11P_d7tQYoWs',
        '__Secure-3PAPISID': 'h59VDKjn7aZCf3SX/AaTWrvI_SpUrt-LDr',
        '__Secure-3PSID': 'egjDpSabhMxiA5TFrbwEvM3iKSLsjaW955RIRUoII7Hs8JQmqB758IVsh4yArKYIWCMBSg.',
        '1P_JAR': '2024-01-21-19',
        '__Secure-3PSIDTS': 'sidts-CjIBPVxjShEnup6sn-MJb_iOjB34QCRNZLFvEayEDCOB5cePbWQRGSmQd1lxFswXNaPPmBAA',
        'NID': '511=OKu214hqrPSf5sM67hLfq4DoKx_DgB_zlOYfiw2u0rQfYTLrbsjiAWBsXs1PaBHvFiIjX754N9M_O5D6usRvyqDTjRcX-0dsPz1fnAn0gXtXZUSmCr6jEoar6j8NYpK_wUtZ8tsnF8b9UGSjfewqoZbRcxkUGV1Z3tnHvhKKX0EGbCkYOuKc-C4-CLYALOUIYYaF1v7i_17laPvUxUdNVnhdWvzGhDpbHPf25tiSk2-lElixm2LeiVNg_GtxNjR862-zAEmChivWcuEWWyZEjZ18gx6rNUe9UrcCj3rCUSJVvbIQF6fnsGDrvNBOVUxxlDA420Tz8jzwPNFmtMvdubLQSxzuxKCydss',
        '__Secure-3PSIDCC': 'ABTWhQHYlMEVYli6bdpq6oybLcTd-WQpswEDKXJ4bGZsZKqDNRakSd-O0LBfGdrliz75oe6ZXA'
    }


    headers = {
        'authority': 'ad.doubleclick.net',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'attribution-reporting-eligible': 'not-trigger, event-source;navigation-source',
        'referer': 'https://googleads.g.doubleclick.net/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CIu2yQEIorbJAQipncoBCNKgygEIpYbLAQiSocsBCJv+zAEIhaDNAQii7s0BCIPwzQEYwMvMARin6s0B',
    }

    params = {
        'xai': 'AKAOjst8kqK_U980sU7HVeA1uSUPPL5JmWxnLliYl0JJset6BqL6CCY0QxnnyYzZIB6ITFBipZvAynFG3ngFE6Kb4iwGhOPJhiEwSxlgxaIRAaZvqFsqx71FVihoRBXZdrCYH3_9zWuhORUC5ZmJKep6M1qC13-xbPbOel0ShGM7nsGEEJGImkkVNsqAC7SjYak8WvTAF5hMZct5ey5yZ8o7okIDjmmxc6qazxT84W6pm51kgSX8vfinUl6Qi-PCp0COQMqJPUY-2bwS0e8C8SpJw0flp_wSsFjmJ3XkljIgviMy567i6RvJbztdxkY56BYZHMQtI2ZTLycNJHZb_72bD0u-AFGFgaf0rQIFqSxpsuu7dXDxtTMzMBfvA8EErjJORxdeHxz5pYh4JM-sstqXzkOu5PfHF1DTRzlU5vXcUU70qjgrACFovIjeo5mlKcS3RygmwhMMrrAOxm1hB0x4m5yoMPjSGztDI6gd0-s9QZhif56NerWQ6wx-j2eMzeTqJ27896SqBTWBl6NLchhGtuXNIf8pQlOnTq-brBb_L_aTi7vJvKZ_-LHBPk2Fde-Qjze1HjCimdOom9QypFP-VK4ylAGhrmOWZhEZw6xVFqlLW6VHuFhcPCkF5JOhDuP-HPZ1ludjamnHxwp8rPaAXV1ubXEB0EIl2RJVxsLKvaUm9w9xZGecKr6wmQ2EsMsbnV00qTX9FmPFZCsG8CWWzm_4qB_05RyLtSsVUJqsj0enBNKWnqAJJgL_sJudagDCvOoi896JqmD-XcsO5Z5BPmpyroLYRRA_yyWDDy3JnAJBG_vvnA19mpkEA-7C08b2lomRCdg_n4v3rVQYEYacn2l6m1oR-DRR9sACPU6hSuC0S6XCE0xMEDODLIKP_nIMSTTcTvkMQoL5_IcD5A1SBlplGetMo4b2wo1eSG-Z1f3uucwLOo9l3wX6P6mx5w0kU8fa8waf_kixvOAwLRPlSFIFkpoh3k2qrL3CiFxXOvC8nG4IoYv9WazTh6GoxfKGhgfHXH2fEBwz3ozlSP_CslhRZcb0WDu9Ru8TeNJ-mD-2H85wYHhDNStV6z1g4a-TY7vbgirdtamLFNZhhCkaVV0tPkgx50u12OYu7l9mjCtDHBH892zJXNDL6Cvu4dvF8YriyOynEUbFMcBiJ1IbReKfoltzYok4Owz7mDL26AZ1A7rNQsZtpZSBLO8ycVIBCyqqmkUy3sMpDcRuB4fBLlu863vEEBYE9dxNTShtDM1ndoMn5UOb49gTyBTjJGuWFCnsco-0n6scmV9H2DNokrUWQRMRoGf3t9kCFQ',
        'sai': 'AMfl-YQZIC3ifKx-9XExhqOPNkPqYZa8BKbBKcpD4WSlStf9JxCgEAzRPNfNgus-thlcG0e5XWIaPySFLEN8_sfhZaIL337bsfPAWlzKxZCWJcrHqLeQ3nRkwysXsfEJrQh5TWnrA9NpI5oN-AtAHsOo8HiyYNb2MPQxrXdohS16iuFtUZIX8mg1TkS4LT67MYAjGMwlrq8fBhFm0BlFcxQwcPBg62pfLJ9KqGKLdyxnokIchhTw1ZKZ_uwboCi1zO--cVPCBCkNNPUD-qSS5wLJmnwLKC-MaI8',
        'sig': 'Cg0ArKJSzGxc7MIPhYdXEAE',
        'uach_m': '[UACH]',
        'crd': 'aHR0cHM6Ly9oYm9nby5jby50aA',
        'fbs_aeid': '[gw_fbsaeid]',
        'urlfix': '1',
        'nis': '4',
        'adurl': '',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': '',
        # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
    }

    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://ssstik.io/en', params=params, cookies=cookies, headers=headers, data=data )
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()

    print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"videos/{id}-{videoTitle}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break


print("STEP 1: Open Chrome browser")
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
# Change the tiktok link
driver.get(f"https://www.tiktok.com/search/video?q={search_phrase.replace(' ', '%20')}")

# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
# to 60 seconds, just enough time for you to complete the captcha yourself.
time.sleep(60)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break

    # this class may change, so make sure to inspect the page and find the correct class
className = " css-1as5cen-DivWrapper e1cg0wnj1"

script = "let l = [];"
script += "document.getElementsByClassName(\""
script += className
script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
script += "return l;"

urlsToDownload = driver.execute_script(script)

print(f"STEP 3: Time to download {len(urlsToDownload)} videos")
for index, url in enumerate(urlsToDownload):
    print(f"Downloading video: {index}")
    downloadVideo(url, index)
    time.sleep(10)
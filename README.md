# Download_Teach
經理人聲音情緒與投資人有限注意：影片下載教學
裡面附上可以自動化下載證交所的webURL.py , 可自行搭配m3u8toCSV.py , 或是直接使用[m3u8]位址去下載（可使用下載test.csv模組）
# Requirements pip
- selenium
- requests
- BeautifulSoup

[1.安裝與啟用 參考](https://medium.com/seaniap/%E7%94%A8python%E6%8E%A7%E5%88%B6chrome%E7%80%8F%E8%A6%BD%E5%99%A8-selenium%E5%88%9D%E9%AB%94%E9%A9%97-732929668ce3)
安裝Selenium
在使用Selenium執行網站的操作前，首先需先確認是否已經安裝Selenium套件。我們可以使用pip安裝Selenium，或者是直接在Anaconda裡面安裝套件。下面是透過pip安裝的指令：

pip install selenium
匯入Selenium套件
使用的第一步就是在程式碼中匯入selenium套件。由於套件中的 webdriver可以幫助我們透過selenium開啟各種不同的瀏覽器驅動程式，好讓我們可以操作該瀏覽器的行為。我們直接使用from…import…的方式，匯入webdriver。

from selenium import webdriver
可以驅動的瀏覽器包括Microsoft的IE、Mozilla的Firefox以及Google 的 Chrome。在這裡我們會使用Google Chrome來進行說明。


Selenium可用的瀏覽器
下載Chrome WebDriver
由於selenium在Google Chrome 瀏覽器中操作必須透過Chrome WebDriver程式，我們必須先安裝該驅動程式。驅動程式可以到下面的網址下載適合自己作業系統的Chrome WebDriver驅動程式。

https://chromedriver.chromium.org/


依照Current Releases裡面的說明，確認自己目前使用的Chrome 瀏覽器版本後（目前我使用的版本是84.0.4147.xx），點進去：


再依照自己的作業系統（ Ｗindows、Mac或者是Linux）下載適當的檔案。

下載完畢後，將檔案放在專案裡面（目前我把檔案放在driver資料夾裡面）。如此，我們就可以使用webdriver.Chrome()建立一個Chrome瀏覽器物件。

然後我們用driver變數，標示webdriver.Chrome()物件。（當然，您也可以用別的名稱當變數。）括弧裡面放置剛剛下載的檔案路徑，可以參考如下：
``` 
driver = webdriver.Chrome('/your_path/your_project/driver/chromedriver')
``` 

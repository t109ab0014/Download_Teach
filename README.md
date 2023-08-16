# Download_Teach
## 經理人聲音情緒與投資人有限注意：影片下載教學

本專案提供了一個自動化下載證交所的工具，你可以使用webURL.py，或者是配合m3u8toCSV.py進行工作，也可以直接使用m3u8位址進行下載（可使用下載test.xlsx模組）。

- 證交所：安裝並使用ffmpeg，需要該影片[.m3u8]的位址
- 1.建立「webURL.txt」，並修改路徑
- 2.在[證交所找到該公司網址](https://webpro.twse.com.tw/WebPortal/search/investor/?searchPageUrl=%2FWebPortal%2Fsearch%2Finvestor%2F&keyword=%E6%96%B0%E5%85%89%E9%87%91&eventDateFrom=&eventDateTo=&topCategoryId=&subCategoryId=&industryCode=&market=&speaker=&description=&order=eventDate&queryType=normal) , 在[getWebURL.py]目標網址裡面修改，並修改#總共？頁
- 3.再使用[m3u8toCSV.py]抓取位址，使用[下載test.xlsx]模板來獲取cmd命令
> 可以全部貼上終端機，或是修改一個記事本的內容與副檔名，改成.cmd ，請參考test.txt

### 環境需求
- selenium
- requests
- BeautifulSoup

### 安裝流程

#### 1. 安裝Selenium
你可以使用pip或在Anaconda裡面直接安裝Selenium套件。

```
pip install selenium
```

#### 2. 匯入Selenium套件
透過下列指令匯入selenium的webdriver。

```
from selenium import webdriver
```

#### 3. 選擇瀏覽器
你可以使用Microsoft的IE、Mozilla的Firefox或Google的Chrome來進行操作。在這裡，我們以Google Chrome為例進行說明。

#### 4. 下載Chrome WebDriver
你必須先安裝Chrome WebDriver程式，才能在Google Chrome瀏覽器中透過selenium進行操作。

[下載Chrome WebDriver](https://chromedriver.chromium.org/)

#### 5. 配置Chrome WebDriver
下載適合自己作業系統的Chrome WebDriver驅動程式後，將檔案放在專案裡面。

以下是一個範例程式碼，你可以參考它來建立一個Chrome瀏覽器物件。

```
driver = webdriver.Chrome('/your_path/your_project/driver/chromedriver')
```

### 更多資訊
如果你需要更詳細的指導，請參考 [這篇文章](https://medium.com/seaniap/%E7%94%A8python%E6%8E%A7%E5%88%B6chrome%E7%80%8F%E8%A6%BD%E5%99%A8-selenium%E5%88%9D%E9%AB%94%E9%A9%97-732929668ce3)。

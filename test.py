from src.integration import Data_Integration
from datetime import datetime
from dotenv import load_dotenv

now = datetime.now()
load_dotenv()

def test():

    total_token=0
    total_error=0
    saveName="report/test/test"

    for i in range(10):

        # a = Data_Integration(filePath1="112年國道每月營業額.csv",filePath2="113年國道每月營業額.csv",saveName=f"test/test{i}",model="gpt-4o-mini")
        # a.do_no_CoT("幫我按月份、區名平均計算這兩年的營業額，以整數表示")
        
        a = Data_Integration(filePath1="聯發科2454_20250528.csv", filePath2="聯發科2454_20250529.csv",saveName=f"{saveName}{i}",model="gpt-4.1-mini")
        a.do("幫我合併這兩天卷商的均價跟總買進股數、總買進成交金額，計算到小數點第一位，去除沒買入的卷商，並加上對應的股票代號。欄位：卷商,均價,總買進股數,總買進成交金額,股票代號")

        # a = Data_Integration(filePath1="公司登記(依營業項目別)－電子資訊供應服務業.csv",filePath2="中小企業行動智慧應用計畫-補助名單.csv")
        # a.do_no_CoT("幫我依照統一編號合併這兩個檔案，獎補助金額由高到低排序，補助事項去除-補助中小企業擴散行動支付場域及創新應用的字串，欄位順序：統一編號、公司名稱、資本額、公司地址、獎補助事項、獎補助金額")
        # a.do("幫我依照統一編號合併這兩個檔案，獎補助金額由高到低排序，補助事項去除-補助中小企業擴散行動支付場域及創新應用的字串，欄位順序：統一編號、公司名稱、資本額、公司地址、獎補助事項、獎補助金額")

        total_token += a.total_tokens
        total_error += a.total_error
    
    with open(f"{saveName}_report.txt", 'a', encoding='utf-8') as f:
            f.write(f"total_token={total_token}\n")
            f.write(f"total_error={total_error}\n")
            avg_token=total_token//10
            f.write(f"avg_token={avg_token}")
            

def test1():
#     i = Data_Integration(filePath1="公司登記(依營業項目別)－飼料製造業.csv",filePath2="公司登記(依營業項目別)－飼料零售業.csv")
#     i.do("過濾出地址在新北的公司，按照統一編號找出重疊的公司，將實收資本總額由低到高排序")

    # j = Data_Integration(filePath1="公司登記(依營業項目別)－電子資訊供應服務業.csv",filePath2="中小企業行動智慧應用計畫-補助名單.csv")
    # j.do_no_CoT("幫我依照統一編號合併這兩個檔案，僅留統一編號、公司名稱、資本額、公司地址、補助事項、補助金額，補助金額由高到低排序，補助事項去除-補助中小企業擴散行動支付場域及創新應用字串")
    # j.do("幫我依照統一編號合併這兩個檔案，僅留統一編號、公司名稱、資本額、公司地址、補助事項、補助金額，補助金額由高到低排序，補助事項去除-補助中小企業擴散行動支付場域及創新應用字串")
    # j.do("這兩個檔案可以怎麼合併？請幫我合併")
    
    # k = Data_Integration(filePath1="受僱員工人數、每人薪資-住宿及餐飲業.csv",filePath2="受僱員工人數、每人薪資-電力及燃氣供應業(按職類別分).csv")
    # k.do("合併兩筆資料，幫我標記產業類別，並由高到低排序7月經常性薪資")

    # a = Data_Integration(filePath1="112年國道每月營業額.csv",filePath2="113年國道每月營業額.csv",saveName=f"test/test{i}",model="gpt-4.1")
    # a.do("幫我按月份、區名平均這兩年的營業額，以整數表示")

    # b = Data_Integration(filePath1="臺中市警察局104年1月份交通事故資料_3.csv",filePath2="臺中市警察局104年2月份交通事故資料.csv")
    # b.do("幫我計算各區交通事故數量，由高到低排序，並分別標記月份")

    # c = Data_Integration(filePath1="股票市場統計-信用交易.csv",filePath2="股票市場統計-股票交易與股價指數.csv")
    # c.do("我想知道近一年的股市加權指數跟融資、融卷金額、融資年增率，請幫我合併")

    # d = Data_Integration(filePath1="聯發科2454_20250528.csv", filePath2="聯發科2454_20250529.csv")
    # d.do_no_CoT("幫我合併這兩天卷商的均價跟總買進股數，計算到小數點第一位，並加上對應的股票代號")
    # d.do("幫我合併這兩天卷商總買進股數跟卷商總買進成交金額、購買均價，計算到小數點第一位，並加上對應的股票代號")
    
    # e = Data_Integration(filePath1="雲林iTaiwan.csv", filePath2="高雄iTaiwan.csv")
    # e.do("幫我合併這兩個檔案，雲林的熱點名稱對應高雄的地點，進行上下合併，保留熱點名稱、地址、經緯度")
   
    # f = Data_Integration(filePath1="109年各區出生登記統計.csv", filePath2="110年各區出生登記統計.csv")
    # f.do("幫我加總這兩個檔案")

    # g = Data_Integration(filePath1="012.csv", filePath2="018.csv")
    # g.do("幫我加總各村里用電度數，並由高到低排序，保留縣市、鄉鎮欄位")

    pass
    
test()
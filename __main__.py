from src.auto_script import run_script,run_script1

def main():
    # run_script(
    #     filePath1="data/公司登記(依營業項目別)－電子資訊供應服務業.csv",
    #     filePath2="data/中小企業行動智慧應用計畫-補助名單.csv",
    #     model="gpt-4.1-mini",
    #     isCoT=False,
    #     savePath="補助事項NoCoT-4.1-mini",
    #     prompt="合併這兩個檔案，只保留兩邊有共同統一編號的資料，獎補助事項刪除(補助中小企業擴散行動支付場域及創新應用-)的字串，資本總額由高到低排序。欄位：統一編號、公司名稱、資本總額、公司地址、獎補助事項、補助金額"
    # )

    # run_script(
    #     filePath1="data/112年國道每月營業額.csv",
    #     filePath2="data/113年國道每月營業額.csv",
    #     model="gpt-4o-mini",
    #     isCoT=True,
    #     savePath="國道CoT-4o-mini",
    #     prompt="計算這兩年的營業額的平均，到小數點第一位，區名位置不要做更動"
    # )

    run_script1(
        filePath1="data/雲林iTaiwan.csv",
        filePath2="data/高雄iTaiwan.csv",
        filePath3="data/南投iTaiwan.csv",
        model="gpt-4o-mini",
        isCoT=True,
        savePath="iTaiwanCoT-4o-mini",
        prompt="幫我合併這三個檔案，缺值自行擷取，郵遞區號由低到高排序，欄位:郵遞區號、地區、熱點名稱、地址、經度、緯度"
    )
main()
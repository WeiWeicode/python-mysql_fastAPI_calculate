import json

# 本篇重點
# 接收到json的數據做運算處理
# 將函式合併成一個函式

def orderTotal(e):
    # 計算訂單總金額
    len = e.__len__()
    # 取得訂單總數
    total = 0
    for i in range(len):
        total += e[i][2]
        # 取得訂單總金額
        # [2]: 第二個欄位是ord_total
        
        # TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType' 
        # 解決方式:table欄位ord_total原為int改numeric
        # 之後改回int又好了= =

    return total

def orderTotalAverage(e):
    # 計算訂單總金額平均
    len = e.__len__()
    # 取得訂單總數
    total = 0
    for i in range(len):
        total += e[i][2]
        # 取得訂單總金額
        # [2]: 第二個欄位是ord_total
        
        # TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType' 
        # 解決方式:table欄位ord_total原為int改numeric
        # 之後改回int又好了= =
    average = total / len
    return average

def orderTotalAndAverage(e):
    # 計算訂單總金額與平均
    total = orderTotal(e)
    average = orderTotalAverage(e)
    len = e.__len__()

    # 轉成json

    jsonorder = {"total": total, "average": average, "len": len}
    return jsonorder


# 個別列出訂單編號與總金額
    # json_array = e
    # store_list = []

    # for item in json_array:
    #     store_details = {}
    #     store_details['ord_number'] = item[1]
    #     store_details['ord_total'] = item[2]
    #     store_list.append(store_details)
        # return store_list
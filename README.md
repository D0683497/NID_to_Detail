# NID_to_Detail

## 環境設定

```
pip install -r requirements.txt
```

## 單筆查詢

1. 執行 `single.py`
2. 輸入學號、密碼、欲查詢學號
3. 結果顯示於終端機上

### 錯誤資訊

+ 若出現 未使用校內網路 則有以下可能:
    + 網頁無回應，請檢察您的網路
    + 您為使用校內網路，請使用校內網路
+ 若出現 帳號密碼輸入錯誤 則有以下可能:
    + 您無權進入系統
    + 您的帳號輸入錯誤，密碼不一定
+ 若出現 密碼輸入錯誤 則有以下可能:
    + 您的密碼輸入錯誤，帳號是對的

## 多筆查詢

1. 於 `example.xlsx` 輸入欲查詢學號

2. 執行 `multi.py`

3. 若有資料查詢不到，則會詢問您 是否將無資料欄位標註為紅色，請輸入y或n來決定

4. 結果產生於 `ouput.xlsx`

### 錯誤資訊

+ 若出現 未使用校內網路 則有以下可能:
    + 網頁無回應，請檢察您的網路
    + 您為使用校內網路，請使用校內網路
+ 若出現 帳號密碼輸入錯誤 則有以下可能:
    + 您無權進入系統
    + 您的帳號輸入錯誤，密碼不一定
+ 若出現 密碼輸入錯誤 則有以下可能:
    + 您的密碼輸入錯誤，帳號是對的
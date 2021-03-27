# WestJR
JR西日本列車走行位置 非公式API Pythonライブラリ

## 機能
* 列車走行位置 (/api/v3/LINE.json)
* 路線名 (/api/v3/area_AREA_master.json)
* 駅一覧 (/api/v3/LINE_st.json)
* 運行情報 (/api/v3/area_AREA_trafficinfo.json)

## 注意
* 動作を完全には確認していません．

## 導入

* requests のインストール
```
$ pip install requests
```

* Import
```
import westjr
jr = westjr.WestJR()
```



## 例

### 列車走行位置の取得

```
import westjr
jr = westjr.WestJR()

trains = jr.trains(line="kobesanyo")

for i in range(len(trains)):
    print(trains[i].no, trains[i].displayType, trains[i].dest_text, "行き")
    if trains[i].next:
        print(trains[i].prev, trains[i].next, "間を走行中")
    else:
        print(trains[i].prev, "に停車中")
        
>>> 5032M 寝台特急 東京 行き
>>> 兵庫 神戸 間を走行中

>>> 257C 普通 西明石 行き
>>> 須磨 に停車中
```



### 路線一覧

```
lines = jr.lines(area="kinki")
print(lines[0].name, lines[0].range)

>>> 赤穂線 相生〜播州赤穂
```



### 駅名一覧

```
stations = jr.stations(line="kyoto")
print(stations[0].name)

>>> 山科
```


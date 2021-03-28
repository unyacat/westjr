# WestJR
JR西日本列車走行位置 非公式API Pythonライブラリ

## 機能
* 列車走行位置取得 (/api/v3/LINE.json)
* 路線名取得 (/api/v3/area_AREA_master.json)
* 駅一覧取得 (/api/v3/LINE_st.json)
* 運行情報取得 (/api/v3/area_AREA_trafficinfo.json)

## 注意
* 動作を完全には確認していません．

## 導入

```console
$ pip install WestJR
```

## 例

* 列車走行位置の取得

```Python
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



* 路線一覧の取得

```Python
lines = jr.lines(area="kinki")
print(lines[0].name, lines[0].range)

>>> 赤穂線 相生〜播州赤穂
```


* 駅名一覧の取得

```Python
stations = jr.stations(line="kyoto")
print(stations[0].name)

>>> 山科
```


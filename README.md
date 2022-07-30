# WestJR

![Python Versions](https://img.shields.io/pypi/pyversions/WestJR.svg)
![PyPI](https://badge.fury.io/py/WestJR.svg)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/unyacat/westjr/master.svg)](https://results.pre-commit.ci/latest/github/unyacat/westjr/master)
![GitHubActions](https://github.com/unyacat/westjr/workflows/Test/badge.svg)

JR西日本列車走行位置 非公式API Pythonライブラリ

* 列車走行位置取得 (`/api/v3/{LINE}.json`)
* 路線名取得 (`/api/v3/area_{AREA}_master.json`)
* 駅一覧取得 (`/api/v3/{LINE}_st.json`)
* 運行情報取得 (`/api/v3/area_{AREA}_trafficinfo.json`)
* 列車環境取得 (`/api/v3/trainmonitorinfo.json`)
* 列車走行位置駅名，列車停車種別の変換

## Notice

* 動作を完全には確認していません．

## Installation

```bash
pip install WestJR
```

## Usage

[Wiki](https://github.com/unyacat/westjr/wiki) に情報があります．

```python
import westjr
jr = westjr.WestJR()

# あらかじめ area や line をセットする
jr = westjr.WestJR(line="kobesanyo", area="kinki")
```

### Example

#### 列車走行位置取得

```python
print(jr.get_trains())
# {'update': '2021-03-31T08:14:34.313Z', 'trains': [{'no': '798T', 'pos': '0414_0415', ...```
```

#### 駅一覧取得

```python
print(jr.get_stations())
# {'stations': [{'info': {'name': '新大阪', 'code': '0415', 'stopTrains': [1, 2, 5], 'typeNotice': None, ...
```

#### 路線一覧取得

```python
print(jr.get_lines())
# {'lines': {'ako': {'name': '赤穂線', 'range': '相生〜播州赤穂', 'st': ...
```

#### 運行情報取得

```Python
print(jr.get_traffic_info())
# {'lines': {}, 'express': {}}
```

#### エリア名一覧表示

```python
print(jr.areas)
# ['hokuriku', 'kinki', 'okayama', 'hiroshima', 'sanin']
```

#### 路線名一覧表示

```python
print(jr.lines)
# ['hokuriku', 'kobesanyo', 'hokurikubiwako', 'kyoto', 'ako', 'kosei', 'kusatsu', 'nara', 'sagano', 'sanin1', 'sanin2', 'osakahigashi', 'takarazuka']
```

#### 列車環境取得

```python
print(jr.get_train_monitor_info()["trains"]["3489M"][0]["cars"][0]["congestion"])
# 26(%)
print(jr.get_train_monitor_info()["trains"]["3489M"][0]["cars"][0]["temp"])
# 23(°C)
```

#### 駅に停車する種別を id から名称に変換する

```python
station = jr.get_stations(line="kyoto")["stations"][0]
print(station["info"]["name"])
print(jr.convert_stopTrains(station["info"]["stopTrains"]))
# 山科
# ['新快速', '快速', '特急']

```

#### 列車走行位置の場所を前駅と次駅の名前に変換する

```python
train = jr.get_trains(line="kobesanyo")["trains"]
tr = train[0]
prev, next = jr.convert_pos(train=tr)
print(prev)
# 塚本
```

## Contribution

* develop ブランチにお願いします

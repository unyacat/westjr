import westjr

jr = westjr.WestJR(line="kobesanyo", area="kinki")

print(jr.get_trains())
# {'update': '2021-03-31T08:14:34.313Z', 'trains': [{'no': '798T', 'pos': '0414_0415', ...
print(jr.get_stations())
# {'stations': [{'info': {'name': '新大阪', 'code': '0415', 'stopTrains': [1, 2, 5], 'typeNotice': None, ...
print(jr.get_lines())
# {'lines': {'ako': {'name': '赤穂線', 'range': '相生〜播州赤穂', 'st': ...
print(jr.get_maintenance())
# {'status': 1, 'notification': {'groupId': 2023012802, 'text': '1月24日から1月31日...
print(jr.get_traffic_info())
# {'lines': {}, 'express': {}}


# エリア名一覧
print(jr.areas)
# ['hokuriku', 'kinki', 'okayama', 'hiroshima', 'sanin']

# 路線名一覧
print(jr.lines)
# ['hokuriku', 'kobesanyo', 'hokurikubiwako', 'kyoto', 'ako', 'kosei', 'kusatsu', 'nara', 'sagano', 'sanin1', 'sanin2', 'osakahigashi', 'takarazuka']


# 駅に停車する種別を id から名称に変換する．
# stopTrains_to_realname()
station = jr.get_stations(line="kyoto")["stations"][0]
print(station["info"]["name"])
print(jr.convert_stopTrains(station["info"]["stopTrains"]))
# 山科
# ['新快速', '快速', '特急']


# 列車走行位置の場所を前駅と次駅の名前に変換する
# jr.pos_to_realname(train=tr)
train = jr.get_trains(line="kobesanyo")["trains"]
tr = train[0]
prev, next = jr.convert_pos(train=tr)
print(prev)
# 例: 塚本

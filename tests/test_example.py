import westjr

jr = westjr.WestJR(line="kobesanyo", area="kinki")


def test_get_trains() -> None:
    """
    {'update': '2021-03-31T08:14:34.313Z', 'trains': [{'no': '798T', 'pos': '0414_0415', ...
    """
    trains = jr.get_trains()
    assert "update" in trains
    assert "trains" in trains


def test_get_stations() -> None:
    """駅一覧取得
    >>> {'stations': [{'info': {'name': '新大阪', 'code': '0415', 'stopTrains': [1, 2, 5], 'typeNotice': None, ...
    """
    stations = jr.get_stations()
    assert "stations" in stations


def test_get_lines() -> None:
    """路線名取得
    >>> {'lines': {'ako': {'name': '赤穂線', 'range': '相生〜播州赤穂', 'st': ...
    """
    lines = jr.get_lines()
    assert "lines" in lines


def test_get_traffic_info() -> None:
    """運行情報取得
    >>> {'lines': {}, 'express': {}}
    """
    traffic_info = jr.get_traffic_info()
    assert "lines" in traffic_info
    assert "express" in traffic_info


def test_get_const_areas() -> None:
    """エリア名一覧
    >>> ['hokuriku', 'kinki', 'okayama', 'hiroshima', 'sanin']
    """
    areas = jr.areas
    assert type(areas) is tuple


def test_get_const_lines() -> None:
    """路線名一覧
    >>> ['hokuriku', 'kobesanyo', 'hokurikubiwako', 'kyoto', 'ako','kosei', 'kusatsu', 'nara', 'sagano', 'sanin1', 'sanin2', 'osakahigashi', 'takarazuka']
    """
    lines = jr.lines
    assert type(lines) is tuple


def test_convert_stopTrains() -> None:
    """駅に停車する種別を id (0~10) から名称に変換

    JR京都線最初の始発駅を取得
    駅名と停車する列車種を抽出
    """
    station = jr.get_stations(line="kyoto")["stations"][0]
    assert station["info"]["name"] == "山科"

    stopTrain_types = jr.convert_stopTrains(station["info"]["stopTrains"])
    assert stopTrain_types == ["新快速", "快速", "特急"]


def test_convert_pos() -> None:
    """列車走行位置の場所を前駅と次駅の名前に変換"""
    train = jr.get_trains(line="kobesanyo")["trains"][0]
    prev, next = jr.convert_pos(train=train)
    assert prev is None or type(prev) is str
    assert next is None or type(next) is str
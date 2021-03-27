import requests
from . import const


class WestJR(object):
    def __init__(self):
        self.uri_suffix = "https://www.train-guide.westjr.co.jp/api/v3/"

    def lines(self, area: str) -> list:
        """
        広域エリアに属する路線一覧を返す．
        該当API例: https://www.train-guide.westjr.co.jp/api/v3/area_kinki_master.json
        :param area: [必須] 広域エリア名(ex. kinki)
        :return: list[Line()]
        """
        uri = self.uri_suffix + "area_" + area + "_master.json"
        response = requests.get(uri)
        if response.status_code != 200:
            raise ValueError("Invalid area name")
        json = response.json()
        res = []
        for li in json["lines"]:
            res.append(Line(line=json["lines"][li]))
        return res

    def stations(self, line: str):
        """
        路線に所属している駅名一覧を返す
        :param line: [必須] 路線名(ex. kobesanyo)
        :return: list[Station()]
        """

        uri = self.uri_suffix + line + "_st.json"
        response = requests.get(uri)
        if response.status_code != 200:
            raise ValueError("Invalid line name")
        json = response.json()

        stations = json["stations"]
        res = []
        for i in range(len(stations)):
            st = Station(station=stations[i])
            res.append(st)

        return res

    def trains(self, line: str) -> list:
        """
        取得時の列車走行位置を返す．
        :param line: [必須] 路線名(ex. kobesanyo)
        :return: list[Train()]
        """
        uri = self.uri_suffix + line + ".json"
        response = requests.get(uri)
        if response.status_code != 200:
            raise ValueError("Invalid line name")
        json = response.json()
        res = []
        for i in range(len(json["trains"])):
            # 指定路線上に存在しない列車情報が交じることがある
            # 該当した場合は飛ばす．
            # 例) 加古川線 - 西脇市行
            try:
                res.append(Train(train=json["trains"][i], update=json["update"], line=line))
            except:
                continue

        return res

    def traffic_line_info(self, area: str) -> dict:
        """
        路線の交通情報を返す．問題が発生しているときのみ情報が載る．
        :param area: [必須] 広域エリア名(ex. kinki)
        :return: dict
        """
        uri = self.uri_suffix + "area_" + area + "_trafficinfo.json"
        response = requests.get(uri)
        if response.status_code != 200:
            raise ValueError("Invalid area name")
        json = response.json()
        lines = json["lines"]

        res = {}
        for key in lines.keys():
            res[key] = TrafficExpressInfo(info=lines[key])
        return res

    def traffic_express_info(self, area: str) -> dict:
        """
        特急の運行情報を返す．問題が発生しているときのみ情報が載る．
        :param area: 広域エリア名(ex. kinki)
        :return: dict
        """
        uri = self.uri_suffix + "area_" + area + "_trafficinfo.json"
        response = requests.get(uri)
        if response.status_code != 200:
            raise ValueError("Invalid area name")
        json = response.json()
        lines = json["express"]
        res = {}
        for key in lines.keys():
            res[key] = TrafficExpressInfo(info=lines[key])
        return res


class Station(object):
    def __init__(self, station: dict):
        self.name = station["info"]["name"]  # 駅名
        self.code = station["info"]["code"]  # 駅ID
        self.stopTrains = self._stop_trains(data=station)  # 停車する種別を配列で返す．．
        self.typeNotice = self._type_notice(data=station)  #
        self.transfer = self._transfer()

    def _transfer(self):
        transfer = self.data["info"]["transfer"]
        if not transfer:
            return None
        res = []
        for i in range(len(transfer)):
            res.append(Transfer(transfer=transfer[i]))
        return res

    def _stop_trains(self, data):
        if data["info"]["stopTrains"]:
            res = [const.stopTrains[i] for i in data["info"]["stopTrains"]]
            return res
        else:
            return None

    def _type_notice(self, data):
        if data["info"]["typeNotice"]:
            return data["info"]["typeNotice"]
        else:
            return None


class Transfer(object):
    """
    乗り換え管理
    """
    def __init__(self, transfer: dict):
        self.name = transfer["name"]
        self.type = transfer["type"]
        self.code = transfer["code"]
        self.link = transfer["link"]
        self.linkCode = transfer["linkCode"]


class Line(object):
    """
    路線管理
    """
    def __init__(self, line: dict):
        self.name = line["name"]   # 路線名 (ex. 赤穂線)
        self.range = line["range"]  # 対象駅名(ex. 相生〜播州赤穂)
        self.st = line["st"]  # 駅名が取れるエンドポイント
        self.pos = line["pos"]  # 列車位置が取れるエンドポイント
        self.relatelines = self._relate_lines()  # 関連路線のエンドポイント
        self.index = line["index"]  # 不明
        self.dest_upper = line["dest"]["upper"]  # 上 の駅名
        self.dest_lower = line["dest"]["lower"]  # 下 の駅名

    def _relate_lines(self):
        if "relatelines" in self.data.keys():
            return self.data["relatelines"]
        else:
            return None


class TrafficLineInfo(object):
    """
    交通情報管理 - Line
    """
    def __init__(self, info: dict):
        self.count = info["count"]
        self.section_from = info["section"]["from"]
        self.section_to = info["section"]["to"]
        self.status = info["status"]
        self.mark = info["mark"]
        self.transfer = bool(info["transfer"])
        self.url = info["url"]


class TrafficExpressInfo(object):
    """
    交通情報管理 - Express
    """
    def __init__(self, info: dict):
        self.count = info["count"]
        self.unique = info["unique"]
        self.name = info["name"]
        self.status = info["status"]
        self.mark = info["mark"]
        self.cause = info["cause"]
        self.url = info["url"]


class Train(object):
    """
    列車情報管理
    """
    def __init__(self, train: dict, update: str, line: str):
        self.update = update  # 更新日時
        self.line = line  # 路線名
        self.no = train["no"]  # 列車番号
        self.direction = int(train["direction"])  # 0が上． 1が下．
        self.pos = train["pos"]  # 列車の場所(APIそのまま)
        self.prev = self._pos_prev()  # [追加] 前の駅名 or 停車中の駅名
        self.next = self._pos_next()  # [追加] 次の駅名．停車中なら None
        self.nickname = train["nickname"]  # 特急名とか (ex. こうのとり９号)
        self.type = train["type"]  # 列車種別？
        self.displayType = train["displayType"]  # 列車種別
        self.dest_text = train["dest"]["text"]  # 行き先
        self.dest_code = train["dest"]["code"]  # 行き先ID
        self.dest_line = train["dest"]["line"]  # (不明)
        self.via = train["via"]  # 経由(ex. 湖西線)
        self.delayMinutes = train["delayMinutes"]  # 遅延時間
        self.typeChange = train["typeChange"]  # 途中で種別が変わる時に入る (ex. 高槻－明石間快速)
        self.numberOfCars = train["numberOfCars"]  # 車両数


    def _pos_split(self):
        return self.pos.split("_")

    def _pos_prev(self):
        prev_st_id, next_st_id = self._pos_split()
        if self.direction == 1:
            return const.st[self.line][prev_st_id]
        elif self.direction == 0:
            if next_st_id == "####":
                return const.st[self.line][prev_st_id]
            else:
                return const.st[self.line][next_st_id]

    def _pos_next(self):
        prev_st_id, next_st_id = self._pos_split()
        if self.direction == 1:
            if next_st_id == "####":
                return None
            else:
                return const.st[self.line][next_st_id]

        elif self.direction == 0:
            if next_st_id == "####":
                return None
            else:
                return const.st[self.line][prev_st_id]

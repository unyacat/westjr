import json
import requests
from requests import RequestException
from . import const


class WestJR(object):
    def __init__(self, line: str = None, area: str = None):
        self.uri_suffix = "https://www.train-guide.westjr.co.jp/api/v3/"
        self.line = line
        self.area = area
        self.areas = const.areas
        self.lines = const.lines

    def _request(self, endpoint: str, method="GET"):
        uri = self.uri_suffix + endpoint + ".json"

        if method == "GET":
            res = requests.get(url=uri)
            try:
                res.raise_for_status()
            except RequestException as e:
                print(e)
                raise e

            return res.json()

    def get_lines(self, area: str = None) -> dict:
        """
        広域エリアに属する路線一覧を取得して返す．
        該当API例: https://www.train-guide.westjr.co.jp/api/v3/area_kinki_master.json
        :param area: [必須] 広域エリア名(ex. kinki)
        :return: dict
        """
        if not area and not self.area:
            raise ValueError("Need to set the area name.")

        _area = area if area else self.area
        endpoint = "area_" + _area + "_master"

        res = self._request(endpoint=endpoint)

        return res

    def get_stations(self, line: str = None) -> dict:
        """
        路線に所属している駅名一覧を取得して返す．
        :param line: [必須] 路線名(ex. kobesanyo)
        :return: dict
        """
        if not line and not self.line:
            raise ValueError("Need to set the line name.")

        _line = line if line else self.line
        endpoint = _line + "_st"

        res = self._request(endpoint=endpoint)
        return res

    def get_trains(self, line: str = None) -> dict:
        """
        列車走行位置を取得して返す．
        :param line: [必須] 路線名(ex. kobesanyo)
        :return: dict
        """
        if not line and not self.line:
            raise ValueError("Need to set the line name.")

        _line = line if line else self.line
        res = self._request(_line)

        return res

    def get_traffic_info(self, area: str = None) -> dict:
        """
        路線の交通情報を取得して返す．問題が発生しているときのみ情報が載る．
        :param area: [必須] 広域エリア名(ex. kinki)
        :return: dict
        """
        if not area and not self.area:
            raise ValueError("Need to set the area name.")

        _area = area if area else self.area
        endpoint = "area_" + _area + "_trafficinfo"
        res = self._request(endpoint=endpoint)

        return res

    def convert_stopTrains(self, stopTrains: list = None) -> list:
        """
        駅一覧にある停車種別IDの配列を実際の停車種別名の配列に変換する．
        :param stopTrains: list[int]
        :return: list[str]
        """
        if stopTrains:
            res = [const.stopTrains[i] for i in stopTrains]
            return res
        else:
            return []

    def convert_pos(self, train: dict, line: str = None) -> tuple:
        """
        ID_ID を (前駅名称, 次駅名称) に変換する．
        停車中の場合 prev_st_name に駅名が入り，next_st_name は None となる．
        :param train: 列車オブジェクト
        :param line: 路線ID
        :return: (前駅名称, 次駅名称)
        """
        prev_st_id, next_st_id = train["pos"].split("_")

        prev_st_name = ""
        next_st_name = ""

        if not line and not self.line:
            raise ValueError("Need to set the line name.")

        _line = line if line else self.line

        if train["direction"] == 1:
            prev_st_name = const.st[_line][prev_st_id]
            if next_st_id == "####":
                next_st_name = None
            else:
                next_st_name = const.st[_line][next_st_id]

        elif train["direction"] == 0:
            if next_st_id == "####":
                prev_st_name = const.st[_line][prev_st_id]
                next_st_name = None
            else:
                prev_st_name = const.st[_line][next_st_id]
                next_st_name = const.st[_line][prev_st_id]

        return prev_st_name, next_st_name


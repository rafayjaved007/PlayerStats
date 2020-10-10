import json
from json.decoder import JSONDecodeError
import requests

from ..items import PlayerstatisticsItem

from scrapy.spiders import CrawlSpider
import scrapy


class PlayerStatsSpider(CrawlSpider):
    name = 'player_stats'

    def start_requests(self):
        url = 'https://www.whoscored.com/StatisticsFeed/1/GetPlayerStatistics?category=shots&subcategory=zones&statsAccumulationType=0&isCurrent=true&playerId=&teamIds=&matchId=&stageId=&tournamentOptions=2,3,4,5,22&sortBy=Rating&sortAscending=&age=&ageComparisonType=0&appearances=&appearancesComparisonType=0&field=&nationality=&positionOptions=%27FW%27,%27AML%27,%27AMC%27,%27AMR%27,%27ML%27,%27MC%27,%27MR%27,%27DMC%27,%27DL%27,%27DC%27,%27DR%27,%27GK%27,%27Sub%27&timeOfTheGameEnd=5&timeOfTheGameStart=0&isMinApp=&page=1&includeZeroValues=&numberOfPlayersToPick=2000'
        for cookie in ['+XzQR5/+AltVuN2HkA1PDYVVgV8AAAAANf5LXh8w7gZofwh3tG10Mg==;', 'kkDfXvX3qwmK+uOHkA1PDTVbgV8AAAAADc0gqyM0tWcqtAkE1LXT5w==', '+xizIOSQkWI8Z/GHkA1PDe1ogV8AAAAAzDEQlMzWAOdw0yJscgAGmw==;', 'dNZFEUW3hjvA6w+IkA1PDYqKgV8AAAAA7UE72cQNko2yt61l2B0DwA==;', 'SvB9L/qMGSbrcROIkA1PDWOOgV8AAAAAwWOdWUAAGnQHQqNM2woqAQ==;']:
            headers = {
                'authority': 'www.whoscored.com',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'x-newrelic-id': 'UAAPWV9VGwIFXFlRAwQA',
                'model-last-mode': 'qUR59UFirskTRQtPg4CQy6hBGM79iM9A9+zfuEJzuMI=',
                'x-requested-with': 'XMLHttpRequest',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.228',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.whoscored.com/Statistics',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cookie': f'_ga=GA1.2.1030469665.1602236789; _gid=GA1.2.1856366010.1602236789; ct=PK; _fbp=fb.1.1602236789673.1560055172; _xpid=1539374307; _xpkey=5whG9OpMA7dc6H6TdCJaYdoc2JX_YTT2; __qca=P0-1950620898-1602237287447; incap_ses_959_774904={cookie} visid_incap_774904=bNePccKFQ6yEv6M/aGpA4HMxgF8AAAAAQkIPAAAAAACAKX2XAUj/OfKTVYefvanbfFZvEI0kVorB'
            }
            res = requests.get(url=url, headers=headers)
            try:
                json.loads(res.text)
                headers1 = {
                    'authority': 'www.whoscored.com',
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'x-newrelic-id': 'UAAPWV9VGwIFXFlRAwQA',
                    'model-last-mode': 'qUR59UFirskTRQtPg4CQy6hBGM79iM9A9+zfuEJzuMI=',
                    'x-requested-with': 'XMLHttpRequest',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.228',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.whoscored.com/Statistics',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'cookie': f'_ga=GA1.2.1030469665.1602236789; _gid=GA1.2.1856366010.1602236789; ct=PK; _fbp=fb.1.1602236789673.1560055172; _xpid=1539374307; _xpkey=5whG9OpMA7dc6H6TdCJaYdoc2JX_YTT2; __qca=P0-1950620898-1602237287447; incap_ses_959_774904={cookie} visid_incap_774904=bNePccKFQ6yEv6M/aGpA4HMxgF8AAAAAQkIPAAAAAACAKX2XAUj/OfKTVYefvanbfFZvEI0kVorB'
                }
                yield scrapy.Request(url=url, callback=self.parse_item, headers=headers1)
            except JSONDecodeError:
                continue


    def parse_item(self, response):

        print(response.text)

        item = PlayerstatisticsItem()
        for player in json.loads(response.text)["playerTableStats"]:
            item['ranking'] = player["ranking"]
            item['first_name'] = player["firstName"]
            item['last_name'] = player["lastName"]
            item['team_name'] = player["teamName"]
            item['team_region_name'] = player["teamRegionName"]
            item['played_positions'] = player["playedPositions"]
            item['age'] = player["age"]
            item['height'] = player["height"]
            item['position'] = player["positionText"]
            item['apps'] = player["apps"]
            item['rating'] = player["rating"]
            item['full_name'] = player["name"]
            item['weight'] = player["weight"]
            yield item



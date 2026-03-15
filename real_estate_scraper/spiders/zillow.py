from typing import Any

import scrapy
import json

class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["zillow.com"]
    start_urls = ["https://zillow.com"]


    def start_requests(self):
        url = "https://zillow.com/houston-tx"

        yield scrapy.Request(url=url, callback=self.parse, meta={"impersonate": "chrome124"
        })

    def parse(self, response):
        script_text = response.css("script#__NEXT_DATA__::text").get()

        if script_text:
            json_data = json.loads(script_text)

        try:
            listings = json_data["props"]["pageProps"]['searchPageState']['cat1']['searchResults']['listResults']

            all_results = []  # ← collect all matching houses

            for house in listings:
                recency_text = house.get("flexFieldText", "")

                if recency_text and ("minute" in recency_text.lower() or "hour" in recency_text.lower()):
                    zillow_data = {
                        "id": house.get("id"),
                        "price": house.get("unformattedPrice"),
                        "url": house.get("detailUrl"),
                        "time_on_market": recency_text,
                        "address": house.get("address")
                    }
                    all_results.append(zillow_data)  # ← accumulate
                    yield zillow_data

            # ← write once, outside the loop, with the full list
            with open("zillow_data.json", "w", encoding="utf-8") as file:
                json.dump(all_results, file, indent=4)

        except KeyError:
            self.logger.error("Error parsing Zillow page")
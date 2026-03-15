from dataclasses import field
import mysql.connector
from itemadapter import ItemAdapter


class RealEstateScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name:
                value = adapter[field_name]
                if isinstance(value, str):
                    adapter[field_name] = value.strip()
        return item

class SaveItemPipeline:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost"
            , user="root"
            , password="Jehovah1#.mysql",
            database="zillow",
        )

        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS zillow (
        id VARCHAR(50) PRIMARY KEY,
        price int NOT NULL,
        address varchar(255) NOT NULL,
        time_on_market varchar(255) NOT NULL,
        url varchar(255) NOT NULL)
        """)

        self.cursor.execute("""
        INSERT IGNORE INTO zillow (id, price, address, time_on_market, url)
        values(%s, %s, %s, %s, %s)
                            
                            """, (item["id"], item["price"], item["address"], item["time_on_market"], item["url"]))

        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()

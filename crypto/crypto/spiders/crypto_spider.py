from scrapy import Spider, Request
from scrapy.selector import Selector
from crypto.items import CryptoItem


class CryptoSpider(Spider):
	name = "crypto"
	allowed_urls = ['https://coinmarketcap.com/']
	start_urls = ['https://coinmarketcap.com/' + str(i+1) for i in range(16)]

	# def parse(self, response):
	# 	for url in start_urls:
	# 		yield scrapy.Request(url, callback = self.parse_each)

	def parse(self, response):
		rows = response.xpath('//*[@id="currencies"]//tr')
		for row in rows:
			Name = row.xpath('./td[2]/a/text()').extract_first()
			#works
			Symbol = row.xpath('./td[2]/span/a/text()').extract_first()
			#works
			MCap = row.xpath('./td[3]/@data-usd').extract_first()
			#works
			Price = row.xpath('./td[4]/a/@data-usd').extract_first()
			#works
			Vol = row.xpath('./td[5]/a/@data-usd').extract_first()
			#works
			CSupply = row.xpath('./td[6]/a/@data-supply').extract_first()
			#works
			DayChg = row.xpath('./td[7]/@data-percentusd').extract_first()
			#works

			item = CryptoItem()
			item['Name'] = Name
			item['Symbol'] = Symbol
			item['MCap'] = MCap
			item['Price'] = Price
			item['Vol'] = Vol
			item['CSupply'] = CSupply
			item['DayChg'] = DayChg
			yield item


			
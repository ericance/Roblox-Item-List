from get_data import ItemData
import unittest
import requests

class TestGame(unittest.TestCase):

	def test_xml_from_request(self):
		# Different url from the Base64 asset I'm using
		url = "https://assetdelivery.roblox.com/v1/asset?id=172732271"
		req = requests.get(url)
		item_data = ItemData()
		xml_tree = item_data.get_xml_from_request(req)
		# Verify that the roblox url returns a roblox XML tag from the request
		self.assertEqual(xml_tree[0: 7], "<roblox")

	def test_get_root_from_xml(self):
		url = "https://assetdelivery.roblox.com/v1/asset?id=317944796"
		req = requests.get(url)

		item_data = ItemData()
		root = item_data.get_root_from_xml(req)
		print(root.find("./Item"))

		# Verify that it is the root
		self.assertEqual(root.find("./Item").text, None)


if __name__ == '__main__':
	unittest.main()
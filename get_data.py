'''
	Name : get_data
	Author: Eric Stalcup
	Created : 11/17/2021
	Course: CIS 152 - Data Structure
	Version: 1.0
	OS: Windows 10
	IDE: Visual Studio Code 1.61.2
	Copyright : This is my own original work 
	based on specifications issued by our instructor
	
	Description : This is the bulk of where the data structures are included. 
	requests.get("roblox item link") returns an XML page in the form of a tree 
	which will be converted into a stack so it can be used inside of a list.
	
	Academic Honesty: I attest that this is my original work.
	I have not used unauthorized source code, either modified or
	unmodified. I have not given other fellow student(s) access
	to my program.
'''

import xml.etree.ElementTree
import requests
import base64
import json

class ItemData():

	def get_xml_from_request(self, req):
		# <Response [200]>

		# req.text returns what is inside of items.xml
		xml_tree = req.text
		return xml_tree
	
	def get_root_from_xml(self, req):
		# fromstring() returns the root: <Element 'roblox' at 0x01809E88>
		root = xml.etree.ElementTree.fromstring(req.text)
		return root

	# Returns a list (stack) in json format
	def get_item_data(self):
		req = requests.get("https://assetdelivery.roblox.com/v1/asset?id=317944796")
		
		xml_tree = self.get_xml_from_request(req)
		root = self.get_root_from_xml(req)
		print(xml_tree[0: 6])
		# root.find().text = Base64 string
		value = root.find("./Item/Properties/string[@name='Value']").text

		# Decodes Base64 into json format
		base64_string = base64.b64decode(value) # This is in binary!

		# json.loads converts to a python dictionary
		json_stack = json.loads(base64_string) # json.loads() can take a string or binary
		return json_stack # Can be used by anyone that wants to call this method

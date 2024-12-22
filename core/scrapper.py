import json
import os
import random
import requests
import datetime
from datetime import datetime
from bs4 import BeautifulSoup

Bl='\033[30m' # VARIABLE COLOR 
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

# User agents for scrapping
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

class Scrapper:
	def __init__(self, username):
		# Make sure that the usernames starts with @ for the http request
		if username.startswith('@'):
			self.username = username
		else:
			self.username = f'@{username}'
		
		self.create_dir()
		# Scrapes the profile and creates the data and posts objects
		self.data = self.scrape_profile()
		self.print_data()
		# Save the data into the text file in the dir
		self.save_data()


	def scrape_profile(self):
		"""
		Scrapes the user profile and creates the data object
		which contains the user information
		:params: none
		:return:none
		"""
		r = requests.get(
			f'http://tiktok.com/{self.username}',
			headers={'User-Agent': random.choice(user_agents)}
		)

		soup = BeautifulSoup(r.text, "html.parser")
		data = soup.find_all("script", attrs={"type": "application/json", "id": "__UNIVERSAL_DATA_FOR_REHYDRATION__"})
		"""data = [json.loads(x.string) for x in soup.find_all("script", type="application/ld+json")]"""
		content = json.loads(data[0].contents[0])

		return {
			"Nickname": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["nickname"],
			"Username": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["uniqueId"],
			"User id": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["id"],
			"Region": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["region"],
			"Language": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["language"],
			"Bio": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["signature"],
			"Following": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["stats"]["followingCount"],
			"Followers": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["stats"]["followerCount"],
			"Likes": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["stats"]["heart"],
			"Videos": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["stats"]["videoCount"],
			"Verified": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["verified"],
			"Is private": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["privateAccount"],
			"Create time": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["createTime"],
			"Nickname last modified": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["nickNameModifyTime"],
			"Profile image URL": content["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]["avatarLarger"]
		}

	def download_profile_picture(self):
		"""
		Downloads the profile picture
		:params: none
		:return: none
		"""
		r = requests.get(self.data['Profile image URL'])
		with open(f"{self.username}.jpg","wb") as f:
			f.write(r.content)
			print(f"{Cy}Profile picture saved to {Wh}{os.getcwd()}")


	def save_data(self):
		"""
		Dumps the dict into a json file in the user directory
		:params: none
		:return: none
		"""

		print(f"{Blu}DATA JSON BACKUP :\n")

		with open(f'{self.username}_profile_data.json','w') as f:
			f.write(json.dumps(self.data))
		#with open(f'{self.username}_post_data.json', 'w') as f:
			#f.write(json.dumps(self.posts))
		print(f"{Cy}Profile data saved to {Wh}{os.getcwd()}")

	def create_dir(self):
		"""
		Create a directory to put all of the OSINT files into,
		it also avoid a possible error with a directory already existing
		:params: none
		:return: none
		"""
		i = 0
		while True:
			try:
				os.mkdir(self.username + str(i))
				os.chdir(self.username + str(i))
				break
			except FileExistsError:
				i += 1

	def print_data(self):
		"""
		Prints out the data to the cmd line
		:params:none
		:return: none
		"""
		print(f"{Blu}ACCOUNT INFORMATION :\n")

		for key, value in self.data.items():

			if (key == "Nickname last modified"):
				nicknamelastmodify = datetime.fromtimestamp(value)
				print(f"{Cy}{key} : {Wh}" + str(nicknamelastmodify))
			elif (key == "Create time"):
				createtime = datetime.fromtimestamp(value)
				print(f"{Cy}{key} : {Wh}" + str(createtime))
			else:
				print(f"{Cy}{key} : {Wh}{value}")
			"""print(f"{key.upper()}: {value}")"""
		
		print(f" ")

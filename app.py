from flask import Flask, render_template

import requests
import time
import random
from apiclient.discovery import build
from os import environ

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', blog_url="")

# pip install --upgrade google-api-python-client
@app.route('/go')
def funcGo():
	Key = environ.get('BLOGGER_API_KEY')
	BlogId = "865457885342918674"

	blog = build('blogger', 'v3', developerKey=Key)
	def get_urls():
		ret = []
		NextPage = None
		while True:
			resp = blog.posts().list(blogId=BlogId, maxResults = 500, pageToken = NextPage).execute()
			time.sleep(2)
			try:
				for i in range(500):
					ret.append(resp["items"][i]["url"])
			except:
				break
			NextPage = resp.get("nextPageToken", None)
			if NextPage is None: 
				break
		return ret
	urls = get_urls()
	# print (urls)
	# print (len(urls))
	
	return render_template('index.html', blog_url =random.choice(urls))





if __name__ == '__main__': app.run(debug=True)
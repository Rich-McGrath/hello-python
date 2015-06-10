import os
import uuid
import urlparse
import redis
import json
from flask import Flask
app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = BLUE

@app.route('/')
def hello():

	return """
	<html>
	<body bgcolor="{}">

	<center><h1><font color="white">Hi, I'm GUID:<br/>
	{}
	</center>

	</body>
	</html>
	""".format(COLOR,my_uuid)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))

rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])

import os
import uuid
import urlparse
import redis
import json
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
from flask import Flask
app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"
COLOR = BLUE
rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])


if r.get("hit_counter") <= 0:
	r.set("hit_counter", 1)

@app.route('/')
def hello():
	r.incr("hit_counter")

	return """
	<html>
	<body bgcolor="{}">
	<center><h1><font color="white">Hi, I'm GUID:<br/>{}
	<center><h1><font color="white">Hit Counter:<br/>{}

	</center>
	<br/><br/>
	<a href="http://www.cornify.com" onclick="cornify_add();return false;"><img src="http://www.cornify.com/assets/cornifycorn.gif" width="52" height="51" border="0" alt="Cornify" /></a><script type="text/javascript" src="http://www.cornify.com/js/cornify.js"></script><br/><br/><br/>
    <iframe src="//giphy.com/embed/RM4wYXmnt3zaM" width="480" height="269" frameBorder="0" style="max-width: 100%" class="giphy-embed" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe><br/>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/ZTidn2dBYbY" frameborder="0" allowfullscreen></iframe><br/><br/>
	<iframe width="560" height="315" src="https://www.youtube.com/embed/bS5P_LAqiVg" frameborder="0" allowfullscreen></iframe><br/><br/>
	<br/><br/>
	<a href="http://www.wonder-tonic.com/geocitiesizer/content.php?theme=2&music=10&url=http://richm-hello-python.cfapps.io/">Click Here for Facemetling Awesomesauce</a>
	</body>
	</html>
	""".format(COLOR,my_uuid,r.get("hit_counter"))





if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))

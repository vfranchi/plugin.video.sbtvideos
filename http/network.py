import xbmc;
import xbmcgui;
import xbmcplugin;
import xbmcaddon;
import urllib2;


class Cache:
	cacheData = {};
	settings = xbmcaddon.Addon("plugin.video.sbtvideos");
	
	def __init__(self):
		if (settings.getSetting("cache") != ""):
			cacheData = pickle.loads(settings.getSetting("cache"));

	def valid(self, key):
		return (cacheData.has_key(url) and time() - cacheData[url]["timestamp"] < 1 * 24 * 3600);
		
	def getData(self, key):
		if cacheData.has_key(key):
			return cacheData[key].get("data", None);
		return None;
	def setData(self, key, data):
		cacheData[url] = {
			"timestamp" : time(),
			"data" : data
		};
		settings.setSetting("cache", pickle.dumps(cacheData));
	
	def delKey(self, key):
		cacheData.pop(key, None);
		settings.setSetting("cache", pickle.dumps(myCache));

cache = Cache();
		
def fetchUrl(url):
	# if url timestamp is less than 24-hour, return cached data
	if (cache.valid(key)):
		return cache.getData(key);
	else:
		header = {
			"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
			"Accept" : "application/json, text/javascript, */*; q=0.01",
			"Origin" : "http://www.sbt.com.br",
			"Referer" : "http://www.sbt.com.br/sbtvideos/programa/400/The-Noite-com-Danilo-Gentili/"
		};
		req = urllib2.Request(url, None, header);
		try:
			response = urllib2.urlopen(req);
			data = response.read();
			response.close();
			cache.setData(url, data);
		except urllib2.URLError:
			# ignore the timestamp if there is an error on the API
			if (myCache.has_key(url)): 
				return myCache[url]["data"];
			else:
				# Internet error
				data = "";
	return data;
	
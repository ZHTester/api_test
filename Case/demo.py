import urllib.request

def search(self, queryStr):
    queryStr = urllib.quote(queryStr)
    url = 'https://www.google.com.hk/search?hl=en&q=%s' % queryStr
    request = urllib.Request(url)
    response = urllib.urlopen(request)
    html = response.read()
    results = self.extractSearchResults(html)
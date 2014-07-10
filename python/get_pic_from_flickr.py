# -*- coding: utf-8 -*-
import urllib
import os
import json

args = { 
#           'place_id' : '9cw_d0JQV7obLp8N5A', # 京都市　IDはflickr.photos.geo.getLocationで見れる
#           'group_id' : '84769930@N00', # kyoto group　サイトで見れる
             # 'text'    : text, # 検索ワード
#           'page'    : str(page), # ページ　連続で取得するならこれをインクリメントする
            'has_geo' : 1,  # ジオタグがついているか
            'extras'  : "date_upload",
            'nojsoncallback' : 1,
            'format'  : 'json',
            'per_page': '20',
            'sort'    : 'date-posted-desc',
            'api_key' : '0bacbd797f523d2850bf3b9dd9377c39',           
            'method'  : 'flickr.photos.search'


}
url = "https://api.flickr.com/services/rest/?%s"%(urllib.urlencode(args) )
photos = json.loads( urllib.urlopen(url).readline() )
#print  json.dumps(photos, sort_keys= True, indent = 4)
#print photos
keylist = photos.keys()
keylist.sort()
#print json.dumps(keylist, sort_keys= True, indent=4)
for k in keylist:
#      print "[",k,"]"
      groupdict = photos[k]
      value=groupdict.keys()
      for v in value:
#            print json.dumps(groupdict[v], sort_keys=True, indent=4)
            a = groupdict[v]
            if v != "total":
#at this line v = "photo"
                  print json.dumps(a, sort_keys=True, indent=4)
                  for d in range(len(a)):
                        d = int(d)
                        print a[d]["farm"]
                  break
      break
#      if value.keys == "photo":
#            t = value.keys()
#            print json.dumps(t, sort_keys = True, indent = 4)
#      print json.dumps(value, sort_keys = True, indent = 4)
#      valuelist = groupdict.keys()
#      valuelist.sort()
#      for value in valuelist:
#            print groupdict[value]
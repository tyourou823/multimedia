# -*- coding: utf-8 -*-
args = { 'method'  : 'flickr.photos.search',
             'api_key' : '0bacbd797f523d2850bf3b9dd9377c39',           
             'per_page': '100', # 1回に取得する画像枚数 <= 500
             'sort'    : 'date-posted-desc',
             'format'  : 'json',
             'nojsoncallback' : 1,
             'place_id' : '9cw_d0JQV7obLp8N5A', # 京都市　IDはflickr.photos.geo.getLocationで見れる
             'group_id' : '84769930@N00', # kyoto group　サイトで見れる
             # 'text'    : text, # 検索ワード
             'page'    : str(page), # ページ　連続で取得するならこれをインクリメントする
             'extras'  : "date_upload",
             'has_geo' : 1  # ジオタグがついているか
             }
url = "http://api.flickr.com/services/rest/?%s"%(urllib.urlencode(args) )
photos = simplejson.loads( urllib.urlopen(url).readline() )
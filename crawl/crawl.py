import http.client
import json
from core_movie.models import Movie
from bson.objectid import ObjectId

conn = http.client.HTTPSConnection("api.studify.tv")

def getInfoMovie(id):
    #export as Bash in Postman
    payload = "{\"query\":\"\\nquery getMovieDetail($id: ID!){\\n      movie(id:$id){\\n              _id\\n              title\\n              apiId\\n                            type\\n              poster_path\\n              backdrop_path\\n              release_date\\n                           trailer_key\\n              overview\\n                                            localizes{\\n                lang\\n                title\\n                overview\\n              }\\n              genres{\\n                id\\n                display_name\\n                name\\n              }\\n              level\\n     number_of_seasons\\n        number_of_episodes\\n             video_url:video_urls\\n              dateFirstPublished\\n        }\\n}\\n\",\"variables\":{\"id\":\""+ id +"\",\"season\":1,\"episode\":1}}"
    headers = {
      'authority': 'api.studify.tv',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/json;charset=UTF-8',
      'origin': 'https://phimlearning.com',
      'referer': 'https://phimlearning.com/',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    conn.request("POST", "/graph", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))["data"]["movie"]

def getSubs(id):
    payload = "{\"query\":\"query getSub($id: String!) {\\n  getSub(id:$id) {\\n      _id\\n      sub {\\n          cueStart\\n          transcript\\n          cueEnd\\n          transcript_vi\\n          seq\\n      }\\n  }\\n}\\n\",\"variables\":{\"id\":\""+ id +"\"}}"
    headers = {
    'authority': 'api.studify.tv',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://phimlearning.com',
    'referer': 'https://phimlearning.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    conn.request("POST", "/graph", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))["data"]["getSub"]

def getAllMovie():
    payload = "{\"query\":\"\\nquery byTrending($first: Int, $after: Cursor) {\\n  getTrending{\\n    films(first: $first, after: $after) {\\n      totalCount\\n      infos {\\n        _id\\n        title\\n        apiId\\n                type\\n        poster_path\\n        backdrop_path\\n        original_language\\n        release_date\\n               poster_image\\n        backdrop_image\\n        trailer_key\\n        overview\\n        poularity\\n        vote_average\\n        vote_count\\n        level\\n        runtime\\n        number_of_seasons\\n        number_of_episodes\\n        imdb\\n        dateFirstPublished\\n        localizes {\\n          lang\\n          title\\n          overview\\n        }\\n      }\\n      pageInfo{\\n        hasNextPage\\n        hasPreviousPage\\n        startCursor\\n        endCursor\\n      }\\n    }\\n  }\\n}\",\"variables\":{\"first\":5000,\"after\":null}}"
    headers = {
    'authority': 'api.studify.tv',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://phimlearning.com',
    'referer': 'https://phimlearning.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    conn.request("POST", "/graph", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))["data"]["getTrending"]["films"]["infos"]

    # dataMovies = []
    cnt = len(data)
    idx = 1
    for movie in data:
        print(idx, cnt, movie["_id"])
        idx += 1
        if Movie.objects.filter(pk=movie["_id"]).exists():
            print("Skipped")
            continue
        try:
            dataM = getInfoMovie(movie["_id"])
            dataM["movie_id"]=movie["_id"]
            dataM.pop('_id')
            for i in range(len(dataM["genres"])):
                dataM["genres"][i]["mongo_id"] = ObjectId()
            for i in range(len(dataM["localizes"])):
                dataM["localizes"][i]["id"] = ObjectId()
            # print(dataM)
            Movie.objects.create(**dataM)
            print("ok")
        except:
            print("skipped error")
    # print(dataMovies)
    # with open("./crawl/movies.json",'w', encoding='utf-8') as jsonfile:
    #     json.dump(dataMovies,jsonfile,ensure_ascii=False,indent=4)
# 첫번째 방법.. 
class LRUCache:
    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last = False)
        self.dic[key] = value

# 두번째 방법
import requests
cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = request.get(url)
    return response.text

def get_article(url):
    print("Getting article...")
    if url in cache:
        cache[url] = get_article_from_server(url)
        
    return cache[url]

get_article("https://test.com/languages/python")
get_article("https://test.com/languages/c")

def get_user(sefl, user_id):
    user = cache.get("user.{0}", user_id)
    if user is None:
        user = db.query("SELECT * FROM users WHERE user_id = {0}", user_id)
        if use is not None:
            key = "user.{0}". format(user_id)
            cache.set(key, json.dumps(user))
    return user

def set_user(user_id, values):
    user = db.query("UPDATE Users WHERE id = {0}", user_id, values)
    cache.set(user_id, user)
    
set_user(12345, {"foo":"bar"})

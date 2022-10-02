class user:
    def __init__(self, feed, message):
        self._feed = feed
        self._message = message 
        
    def get_feed(self):
        return self._feed
    
    def get_message(self):
        return self._message
    
    def set_feed(self, feed):
        self._feed = feed
        
    def set_message(self, message):
        self._message = message
    
    def feedprocessor(self, feed):
        self.feeds = []
        self.feeds.append(feed)
        
        self.sfeeds = sorted(self.feeds) 
        return self.sfeeds[-1] # 제일 최신 거 가져간다고 한다면.. 
    
def main():
    a = user()
    a.set_feed(1)
    a.set_message("helloworld")

    

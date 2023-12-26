from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post

class LatestEntriesFeed(Feed):
    title = "blog newest post"
    link = "/rss/feed"
    content = "best blog over."

    def items(self):
        return post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
    
 
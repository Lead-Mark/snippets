import feedparser

# List of RSS feed URLs to aggregate
rss_urls = [
    "https://rss.feed1.com",
    "https://rss.feed2.com"
]

def fetch_and_combine_feeds(urls):
    combined_entries = []
    for url in urls:
        feed = feedparser.parse(url)
        combined_entries.extend(feed.entries)
    return combined_entries

from feedgen.feed import FeedGenerator

def create_rss_feed(entries):
    fg = FeedGenerator()
    fg.title('Combined RSS Feed')
    fg.link(href='http://example.com', rel='alternate')
    fg.description('This is a combined feed of multiple RSS sources.')

    for entry in entries:
        fe = fg.add_entry()
        fe.title(entry.title)
        fe.link(href=entry.link)
        fe.description(entry.description)

    return fg.rss_str(pretty=True)


combined_feed = fetch_and_combine_feeds(rss_urls)
final_feed = create_rss_feed(combined_feed)

print(final_feed)  # Temporary, to see the result

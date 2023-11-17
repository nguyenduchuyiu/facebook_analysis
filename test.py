from facebook_scraper import *
from PreProcessingModule import Processor
# set_cookies("Data/cookies.txt")
results = []
start_url = None
post_result = []

def handle_pagination_url(url):
    global start_url
    start_url = url

while True:
    try:
        post = next(
            get_posts(
                post_urls=[696825412541931],
                options={
                    "comments": "generator",
                    "comment_start_url": start_url,
                    "comment_request_url_callback": handle_pagination_url,
                },
            )
        )
        comments = post["comments_full"]
        for comment in comments:
            comment["replies"] = list(comment["replies"])
            
            replies_list = []
            if comment["replies"]:
                for replies in comment["replies"]:
                    replies_list.append(replies)
            comment.update({"replies":replies_list})
            results.append(comment)
            
        print("All done")
        post.update({"comments_full":results})
        post_result.append(post)
        break
    except exceptions.TemporarilyBanned:
        print("Temporarily banned, sleeping for 10m")
        time.sleep(600)

pro = Processor(post_data=post_result)
pro.convert_to_dataframe().to_csv('haha.csv')


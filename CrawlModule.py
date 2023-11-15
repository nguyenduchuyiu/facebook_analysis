import facebook_scraper as fs

class Crawler():

    def __init__(self, cookie_path='Data/cookies.txt'):
        self.cookie_path = cookie_path


    # Get raw data from fanpage's post
    def get_post_data(self, fanpage_path, page_number):
        post_data = []

        for post in fs.get_posts_by_url(
            
        ) (fanpage_path,
                            pages=page_number,
                            cookies=self.cookie_path,
                            options={"comments": True, "reactions": True, "allow_extra_requests": True},
                            extra_info=True
                            ):
            post_data.append(post)
            print(post_data)

        return post_data


import facebook_scraper as fs

class Crawler():

    def __init__(self, cookie_path='Data/cookies.txt') -> None:
        fs.set_cookies(cookies=cookie_path)


    # Get raw data from fanpage's post
    def get_post_data(self, fanpage_path, page_number):
        post_data = []
        i = 0

        for post in fs.get_posts(fanpage_path,
                            pages=page_number,
                            options={'comments': True, 'reactions':True, 'allow_extra_requests': True},
                            extra_info=True):
            post_data.append(post)

            # Print progression
            per = i/(page_number*10) * 100
            i += 1
            print(f'{per}' + '%')

        return post_data


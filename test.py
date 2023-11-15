"""
Download comments for a public Facebook post.
"""
import pandas as pd
import facebook_scraper as fs

POST_ID = "695964205961385"

gen = fs.get_reactors(POST_ID)

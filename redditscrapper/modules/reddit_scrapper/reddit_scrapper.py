import re
import praw
import requests
import time
# from databases import Url_Table as ut
# from db_pipeline import Db_Pipeline as dp

def get_tag(test):
    """
    This function reads the given submission and finds suitable tags for given
    reddit post
    :param submission: object of reddit post
    :return: string separated by comas
    """
    #TODO: create logic to figure out tags by going deep int post
    #TODO: if deep search doesn't work, separate the title by comas

    return re.sub("\s+", ", ", (test).strip())

def check_blog_name():
    """
    This function gets the name of the blogger data is being posted on.
    :return:
    """
    return "www.redditflix.com"

def check_blog_posted(submission):
    """
    This function checks on blogger if there is any post made using given
    reddit post
    :param submission: object of reddit post
    :return: boolean: True if post is on blogger, False if post is not on
    blogger
    """
    #TODO: Create logic to see if there is any post on blogger relating
    #TODO: given reddit post
    #TODO: If there is, return True, else False.
    return False

def create_post_for_blogger(submission):
    """
    create a post for blogger using given reddit post
    :param submission: object of reddit post
    :return: a json named blog_post created according to google blogger api v3
    requirements containing all the required informaion for blog_post
    """
    #TODO: Create logic to create a HTML code for post to be posted on Blogger
    blog_post = {"": ""}
    return blog_post

def post_on_blogger(submission):
    """
    create a
    :param submission:
    :return:
    """

def get_subreddit():
    """

    :return:
    """
    return "videos"

def populate_data():
    pass

def retrieve_data():
    pass


def find_string(url):
    text = url
    return True


def scrape_reddit():
    good_urls = []
    number = 5000
    r = praw.Reddit(user_agent='reddit scraper by billcrystals')
    t = time.time()
    submissions = r.get_subreddit(get_subreddit()).get_new(limit=number)
    submissions1 = r.get_subreddit(get_subreddit()).\
        get_controversial_from_year(limit=number)
    results_from = 'New'

    try:
        for submission in submissions:
            if not submission.url:
                continue
            else:
                post_info = {
                    "post title":           submission.title,
                    "external url":         submission.url,
                    "reddit url":           submission.short_link,
                    "tags":                 get_tag(submission),
                    "subreddit":            get_subreddit(),
                    "blogger_posted_on":    check_blog_name(),
                    "posted":               check_blog_posted(submission)
                }

                if len(good_urls) == 0:
                    good_urls.append(post_info)
                elif not good_urls.__contains__(post_info):
                    good_urls.append(post_info)



                # endpoint = submission.url.find('.com/')
                # url = 'i.' + submission.url[:endpoint] + '.jpg'
                # good_urls.append([url, submission.short_link, submission.title])
                # good_urls.append([])
            # elif submission.url.startswith('imgur.com/'):
            #     endpoint = submission.url.find('.com/')
            #     url = 'i.' + submission.url[:endpoint] + '.jpg'
            #     good_urls.append([url, submission.short_link, submission.title,
            #                       submission.])
            # elif submission.url.startswith('gfycat'):
            #     endpoint = submission.url.find('.com/')

            # elif find_string('/r/')(submission.url):
            #     if find_string('imgur')(submission.url):
            #         print('/r/ found in %s' % submission.url)
            #         endpoint = submission.url.rfind('/')
            #         url = 'http://i.imgur.com' + submission.url[endpoint:] + '.jpg'
            #         good_urls.append([url, submission.short_link, submission.title])
            #     else:
            #         indirect_urls.append([submission.url, submission.short_link,
            #                               submission.title, submission.score])
            # elif find_string('/gallery/')(submission.url):
            #     print 'Submission (%s) is an Imgur album link' % submission.url
            #     indirect_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            # elif find_string('http://imgur.com/')(submission.url):
            #     if find_string('/a/')(submission.url):
            #         print 'Submission (%s) is an Imgur album link' % submission.url
            #         indirect_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            #     else:
            #         endpoint = submission.url.find('.com/')
            #         url = submission.url[endpoint + 5:]
            #         new_url = 'http://i.imgur.com/%s.jpg' % url
            #         if len(submission.title) > 75:
            #             try:
            #                 submission.title = str(submission.title[:75]) + '...'
            #                 good_urls.append([new_url, submission.short_link, submission.title])
            #             except UnicodeError:
            #                 continue
            #         else:
            #             good_urls.append([new_url, submission.short_link, submission.title])
            # elif find_string('qkme')(submission.url):
            #     print 'QKME link, adding to indirect_urls...'
            #     indirect_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            # elif find_string('youtube')(submission.url):
            #     print 'Youtube link, adding to indirect_urls...'
            #     indirect_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            # elif find_string('twitter')(submission.url):
            #     print 'Twitter link, adding to indirect_urls...'
            #     indirect_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            # elif '?' in submission.url:
            #     endpoint = submission.url.find('?')
            #     url = submission.url[:endpoint]
            #     if len(submission.title) > 75:
            #         try:
            #             submission.title = str(submission.title[:75]) + '...'
            #             good_urls.append([url, submission.short_link, submission.title])
            #         except UnicodeError:
            #             continue
            #     else:
            #         good_urls.append([url, submission.short_link, submission.title])
            # elif not submission.url.endswith(('.gif', '.png', '.jpg', '.jpeg')):
            #     print 'Indirect URL: %s' % submission.url
            #     indirect_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            # else:
            #     if len(submission.title) > 75:
            #         try:
            #             submission.title = str(submission.title[:75]) + '...'
            #             good_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            #         except UnicodeError:
            #             continue
            #     else:
            #         good_urls.append([submission.url, submission.short_link, submission.title, submission.score])
            #

            print(post_info)
    except (praw.errors.RedirectException, requests.HTTPError):
        return 'no subreddit'


    if len(good_urls) > 0:
        for url in good_urls:
            pass
    data = {
        'good_urls': good_urls,
        'good_urls_number': len(good_urls),
        'results_from': results_from
    }
    # return data

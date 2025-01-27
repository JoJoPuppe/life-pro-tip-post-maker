import praw
import os

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
PASSWORD = os.environ.get("PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")
USERNAME = os.environ.get("USERNAME")


class LifeProTip(object):
    def __init__(self):
        self.tips_ids = self._load_ids()
        self.reddit = self._auth_reddit()

    def _auth_reddit(self):
        reddit = praw.Reddit(client_id=CLIENT_ID,
                             client_secret=CLIENT_SECRET,
                             password=PASSWORD,
                             user_agent=USER_AGENT,
                             username=USERNAME)
        return reddit

    def _load_ids(self):
        with open("tips_ids.txt", "r") as f:
            tips = f.read().split(",")

        return tips

    def get_lpt(self):
        for sub in self.reddit.subreddit("LifeProTips").hot(limit=1):
            lpt = sub
        return lpt.title

    def get_life_pro_tip(self):
        new_ids = []
        submission_titles = []
        for submission in self.reddit.subreddit("LifeProTips").hot(limit=10):
            if submission.id not in self.tips_ids:
                new_ids.append(submission.id)
                submission_titles.append(submission.title)
        if new_ids:
            self._save_new_ids(new_ids)
            self._save_submissions(submission_titles)

        return submission_titles

    def _save_submissions(self, subs):
        with open("subs.txt", "a") as f:
            subs_text = "\n".join(subs)
            subs_text += "\n"
            f.write(subs_text)

    def _save_new_ids(self, ids):
        self.tips_ids.extend(ids)
        with open("tips_ids.txt", "w+") as f:
            text = ",".join(self.tips_ids)
            f.write(text)

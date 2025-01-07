<<<<<<< HEAD
import os
import dotenv
import json
import feedparser
from src.logs import init_log, logging_msg



dotenv.load_dotenv('.env', override=True)
DEBUG = os.getenv("DEBUG")
RSS_FEEDS = os.getenv("RSS_FEEDS")


### DOWNLOAD PODCASTS ###
def parse_rss_feed()->bool:
    logging_msg("Parsing RSS feeds", "INFO")

    try:
        logging_msg(f"Parsing: {RSS_FEEDS}", "INFO")
        
        rss_file_path = os.path.abspath(RSS_FEEDS)
        with open(rss_file_path, 'r', encoding='utf-8') as file:
            feeds = json.load(file)
        
        for feed in feeds:
            try:
                logging_msg(f"Podcsat: {feed['name']}", "DEBUG")
                
                rss_feed = feed['rss_feed']
                rss_data = feedparser.parse(rss_feed)
                for entry in rss_data.entries:
                    if 'enclosures' in entry:
                        for enclosure in entry.enclosures:
                            logging_msg(f"Downloadable file: {enclosure.href}", "INFO")

            except Exception as e:
                logging_msg(f"Error inner loop: {e}", "ERROR")
        
        return True

    except Exception as e:
        logging_msg(f"Error in parse_rss_feed(): {e}", "CRITICAL")
        return False

=======
import dotenv
import os
from logs import init_log, logging_msg
import utils



##################################################
##################################################
##################################################
>>>>>>> 6dece97de3ecd4d262879f3367d6edc4784a8aae

############
### MAIN ###
############
dotenv.load_dotenv(override=True)
init_log()
logging_msg("START PROGRAM", "WARNING")
<<<<<<< HEAD
parse_rss_feed()
=======
if utils.init():
    FEED_RSS = os.getenv("FEED_RSS")
    utils.parse_rss_feed(FEED_RSS)
>>>>>>> 6dece97de3ecd4d262879f3367d6edc4784a8aae
logging_msg("END PROGRAM", "WARNING")

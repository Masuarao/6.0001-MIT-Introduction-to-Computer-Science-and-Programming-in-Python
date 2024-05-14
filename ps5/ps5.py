# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid,title,description,link,pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    
    


#======================
# Triggers
#======================

class Trigger(object):
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def check_valid_phrase(self,phrase):
        '''
        Given a phrase, check if it is a valid phrase. 
        
        A valid phrase contains no puntuation. 
        
        A valid phrase also contains no two or more spaces. 
        
        '''
        #print('Debugging: Phrase is:',phrase)
        # Reject phrases with two or more spaces
        if '  ' in phrase:
            return False 
        
        # Reject phrases with punctuations
        for i in string.punctuation:
            if i in phrase:
                print('Phrase is not valid')
                return False
        # Debugging
        
        #print('Phrase is Valid')
        return True
    
    def __init__(self,phrase):
        self.phrase = phrase
        self.valid_phrase = self.check_valid_phrase(phrase)
    
    def get_phrase(self):
        return self.phrase
        
    def clean_string(self,input_string):
        '''
        Takes a string input 
        
        Cleans the string input and removes any punctuation marks 
        
        Also removes any extra spaces
        
        Inserts spaces iin 
        '''
        cleaned_list = []
      
        for i in range(len(input_string)):
            
            # Append first letter that is a character
            if len(cleaned_list) == 0 and input_string[i] not in string.punctuation:
                cleaned_list.append(input_string[i])
            else:
                
                # If current character is not a punctuation string    
                if input_string[i] not in string.punctuation:
                
                    # Append a space and character if previous character is a punctuation
                    if(input_string[i-1] in string.punctuation):
                    
                        if input_string[i] != ' ':
                            cleaned_list.append(' ')
                            cleaned_list.append(input_string[i])
                        else:
                            cleaned_list.append(input_string[i])
                
                    # Othersise, just append if character and current character is not a space 
                    elif len(cleaned_list)>0:
                        if not(cleaned_list[-1] == ' ' and input_string[i] == ' '):
                            cleaned_list.append(input_string[i])                
                
                
        return ''.join(cleaned_list).lower()
    
    def compare_exact(self,searching_string,searched_string):
        """
        Uses regex to do an exact search of searching_string in searched_string

        """
        cleaned_string = self.clean_string(searched_string)                     # Clean the string being searched
        pattern = r'\b' + re.escape(searching_string.lower()) + r'\b'           # Create regex matching pattern
        match = re.search(pattern, cleaned_string)                               # Return True if a match is found, False otherwise
        
        return bool(match)
    

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

    
# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self,phrase):
        PhraseTrigger.__init__(self,phrase)
    def evaluate(self,story):
        if self.valid_phrase == False:
            return False
        else:         
            return self.compare_exact(self.get_phrase(),story.get_title())
            
    
        
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self,phrase):
        PhraseTrigger.__init__(self,phrase)
    def evaluate(self,story):
        if self.valid_phrase == False:
            return False
        else:         
            return self.compare_exact(self.get_phrase(),story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self,date_time_input):
        self.date_time = datetime.strptime(date_time_input,"%d %b %Y %H:%M:%S")
        self.date_time = self.date_time.replace(tzinfo=pytz.timezone("EST"))
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def __init__(self,date_time_input):
        TimeTrigger.__init__(self,date_time_input)
    def get_date_time(self):
        return self.date_time
    
    def evaluate(self, story):
        if story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) < self.get_date_time():
            return True
        else: 
            return False

class AfterTrigger(TimeTrigger):
    def __init__(self,date_time_input):
        TimeTrigger.__init__(self,date_time_input)
    def get_date_time(self):
        return self.date_time
    
    def evaluate(self, story):
        
        story_pubdate_utc = story.get_pubdate().astimezone(pytz.timezone("UTC")) 
        trigger_datetime_utc = self.get_date_time().astimezone(pytz.timezone("UTC"))

        if story_pubdate_utc > trigger_datetime_utc:
            return True
        else:
            return False
        
        story_pubdate = story.get_pubdate()
        if story_pubdate.tzinfo is None:  # Check if offset-naive
            story_pubdate = story_pubdate.replace(tzinfo=pytz.timezone("UTC")) 
        
        # Now both datetimes are offset-aware
        if story_pubdate > self.get_date_time(): 
            return True
        else:
            return False
        
        
    
        #if story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) > self.get_date_time():
        #if story.get_pubdate() > self.get_date_time():
            #return True
        #else: 
            #return False
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self,input_trigger):
        self.trigger = input_trigger
    def get_trigger():
        return self.trigger 
    def evaluate(self,story):
        invert_boolean = self.trigger.evaluate(story)                           # Evaluate boolean to be inverted
        return not(invert_boolean)                                              # Return the inverted boolean

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.trigger1 = Trigger1
        self.trigger2 = Trigger2
    def evaluate(self,story):
        boolean1 = self.trigger1.evaluate(story)
        boolean2 = self.trigger2.evaluate(story)
        
        if boolean1 and boolean2:
            return True
        else: 
            return False
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self,Trigger1,Trigger2):
        self.trigger1 = Trigger1
        self.trigger2 = Trigger2
    def evaluate(self,story):
        boolean1 = self.trigger1.evaluate(story)
        boolean2 = self.trigger2.evaluate(story)
        
        if boolean1 or boolean2:
            return True
        else: 
            return False


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
            
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()


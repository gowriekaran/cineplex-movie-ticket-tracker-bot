# Python Cineplex Canada Movie Ticket Tracker Bot
Purpose: This software is used to track the availability of specific movie tickets. 

Disclaimer: This software is not a scalper bot. There are no purchasing abilities within this software. It's only purpose is notify the end-user via sound notification that the movie ticket(s) they are interested in are now on sale, and right after that, it shuts down automatically.

Requirements:
 - [Python](https://www.python.org/)
 - [PIP](https://pip.pypa.io/en/stable/)
 - [Selenium](https://pypi.org/project/selenium/)
 - [Colorama](https://pypi.org/project/colorama/)
 - [Winsound](https://docs.python.org/3/library/winsound.html)
 - [Time](https://docs.python.org/3/library/time.html)

Instructions:
 1. Configure the variables.py file
	 - CHROME_DRIVER_PATH: File path to your chome driver
	 - INITIAL_LOAD_DELAY: Delay before tracket bot starts 
	 - LOOP_REPEAT_DELAY: Delay before next loop run
	 - MOVIE_URL: The Cineplex individual movie page
	 - MOVIE_TICKETS_ON_SALE_MESSAGE: Success message
	 - MOVIE_TICKETS_NOT_ON_SALE_MESSAGE: Failure message
	 - NEGATIVE_SOUND_NOTIFICATION_DURATION: Failure sound duration
	 - NEGATIVE_SOUND_NOTIFICATION_FREQUENCY: Failure sound frequency
	 - TARGET_ELEMENT_XPATH: Web element xpath to target
	 - POSITIVE_SOUND_NOTIFICATION_DURATION: Positive sound duration
	 - POSITIVE_SOUND_NOTIFICATION_FREQUENCY: Positive sound frequency
2. Run app.py

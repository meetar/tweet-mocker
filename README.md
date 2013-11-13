tweet-mocker
============

Für mocking die Tweets.

A Twitter bot which watches another Twitter account for tweets, modifies them, and retweets them as their own.

I like to run it with this command:

    nohup python tweet-mocker.py &
    
The "nohup" command sends all output (like "print" statements) to a file called "nohup.out", which you can check later for troubleshooting purposes. The ampersand runs the command in the background, freeing up the console.

If you're running this in the background, to kill the process, run:

    pidof python
    
Then find the process ID of the python command (it will be a number like 5130) and kill it, like so:

    kill 5130

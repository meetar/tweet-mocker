tweet-mocker
============

Für mocken die Tweets.

A Twitter bot which watches another Twitter account for tweets, modifies them in some way, and tweets the result.

Intended to be run under Linux, but it might work on other systems.

#### Dependencies

Twython http://twython.readthedocs.org/

#### Usage

I like to run it with this command:

    nohup python tweet-mocker.py &
    
The "nohup" command sends all output (like "print" statements) to a file called "nohup.out", which you can check later for troubleshooting purposes. The ampersand runs the command in the background, freeing up the console.

If you're running it in the background, to kill the process run:

    pidof python
    
Then, find the process ID of the python command (it will be a number like 5130) and kill it like so:

    kill 5130

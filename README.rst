SendTeamsMessage
===============
Send a little card to your Teams channel  
------------
Installation
------------
Using PIP via Github::

    pip install git+https://github.com/jordimalla/SendTeamsMessage.git#egg=SendTeamsMessage

-----
Usage
-----
CLI Usage is as follows::

    usage: SendTeamsMessage [-h] [-t TITLE] [-m MESSAGE] [-H WEBHOOK] [-s SUMMARY]
                            [--send-ok]

    Send message to your Teams chanel

    optional arguments:
      -h, --help            show this help message and exit
      -t TITLE, --title TITLE
                            Card title
      -m MESSAGE, --message MESSAGE
                            Card message text
      -H WEBHOOK, --webhook WEBHOOK
                            Your channel webhook
      -s SUMMARY, --summary SUMMARY
                            Card summary text
      --send-ok             Put red color in the card or if not put red color

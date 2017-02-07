# WorkdayBot 

<a href="https://line.me/R/ti/p/%40fas6507o"><img height="36" border="0" alt="Add Friend" src="https://scdn.line-apps.com/n/line_add_friends/btn/en.png"></a>

LINE bot that helps calculate due dates using Taiwanese business calendar



# The Problem

1. **Colleagues in Taipei City Government spend non-trivial amount of time calculating due dates for contracts.**
  
  For example, when a 100-day contract starts on January 5th, 2017, the due date would be June 6th. The calculation should account for holidays and weekends, which could be easily done with [WORKDAY in excel](https://support.office.com/en-us/article/WORKDAY-function-F764A5B7-05FC-4494-9486-60D494EFBF33) or [offset aliasese in Python through Pandas](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases). However, the Taiwanese business calendar works differently than the US one, which brings us to problem 2.
  
2. **Sometimes Saturdays are business days in Taiwan**

  In Taiwan, we take the Monday off if the Tuesday is a national holiday Friday off if Thursday is a holiday. We then make up the extra holiday by turning a Saturday into a business day. As far as I know, the weekends cannot be overridden as businessdays in Excel, so I had to use the CustomBusinessDay from Pandas and add on the "working Saturdays" before computing the due date.
  
# The Interface

Most of my co-workers in the department aren’t familiar with running python scripts, so they need a more intuitive user interface. In the end, I built a bot for the Line app. 

![LINE bot](https://cdn-images-1.medium.com/max/800/1*2ajzYKjDlHjLUQX7SZwlBQ.png)

Type in the start date and number of business days, and the bot replies with the due date.

Line is one of the most popular messaging app in Asia and definitely the most prominent in Taiwan. While Slack is often used in the workplace in western countries, Line’s group chat is the main mode of communication in Taiwan.

There are a couple added benefits from exposing the service through a Line bot:
Similar to Slack, the bot can be added to a group chat, so my co-workers can ask for due dates without leaving the chat.
No need to design/develop the graphical user interface
Low friction when referring the bot to others on the platform. The bot can either be referred through chat or added through a QR code.

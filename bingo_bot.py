class BingoBot: 
   """Constructs the onboarding message and stores the state of which tasks were completed."""

   WELCOME_BLOCK = {
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Welcome to Deskop Bingo! :wave: We're so glad you're here. :blush:\n\n*Get started go and sign up**<https://prime-bingo.herokuapp.com/|Bingo App>*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Your bingo card will stay through a logout or refresh, but highlighting of the numbers will not I will work on that :grin:. So for now don't refresh if you want things easier on you but it's not the end of the world. For I will keep a running list of each game when calling out a new number.Rules are simple 5 in a row horizontally, diagonally, or vertically is a bingo"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please use 3 :desktop_bingos: to get the game going. Use :baby_chick: to let us know you have a bingo and submit a screenshot for verification by peers! Thank you and have fun!"
			}
		}
}

def __init__(self, channel): 
  self.channel = "desktop_bingo"
  self.username = "primebingobot"
  self.icon_emoji = ":robot_face:"
  self.timestamp = "" 
  self.start_task_completed = False; 
  self.found_bingo_completed = False; 

def get_message_payload(self): 
    return { 
        "ts": self.timestamp, 
        "channel": self.channe,
        "username": self.username, 
        "icon_emoji": self.icon_emoji,
        "block": [
        self.WELCOME_BLOCK
        ]
    }
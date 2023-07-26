import requests
import time
import datetime

delay = 60  # in seconds, the higher this number is, the lower the chances of getting rate limited/banned. Discord rate limite is 3 per minute i think.


class Main:

  def run(self):
    while True:  # you can change this code to whatever you want, whatever the formula is, it should change the status variable. for example:
   #   start_time = datetime.datetime(2007, 10, 11, 7, 12)
   #   current_time = datetime.datetime.now()
   #   time_diff = current_time - start_time
   #   minutes_diff = int(time_diff.total_seconds() // 60)
   #   formatted_minutes_diff = format(minutes_diff, ",")
   #   status = f"I just turned {formatted_minutes_diff} minutes old!!"

         status_list = ["1", "2", "3", "4", "5"] #add or remove as many as you want
         index = 0
         while index < len(status_list):
                   status = (f"unchanging text here if any {status_list[index]}")
                   index += 1

                   self.set_status(status)
                   time.sleep(delay)

  def set_status(self, status):
    headers = {
      "Authorization":
      "TOKEN", #fill this in
      "Content-Type": "application/json"
    }
    data = {"custom_status": {"text": status, "emoji_name": "🎉"}}
    response = requests.patch("https://discord.com/api/v9/users/@me/settings",
                              headers=headers,
                              json=data)
    if response.status_code == 200:
      print(f"Status updated to '{status}' successfully!")
    else:
      print(f"Failed to update status. Error code: {response.status_code}")


if __name__ == "__main__":
  bot = Main()
  bot.run()

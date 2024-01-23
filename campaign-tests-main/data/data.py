import time

youtube_channel = "https://testing.buzz.guru/youtube/channels/5b61d5e20d7d320017d827fd"
tiktok_channel = "https://testing.buzz.guru/tiktok/channels/127905465618821121"
instagram_channel = "https://testing.buzz.guru/instagram/channels/305701719"

channel_list = [youtube_channel, tiktok_channel]
# Instagram is blocked
# channel_list = [youtube_channel, tiktok_channel, instagram_channel]


youtube_video = "https://www.youtube.com/watch?v=GYJ-VQG3T94"
tiktok_post = "https://www.tiktok.com/@zachking/video/6768504823336815877"
instagram_post = "https://www.instagram.com/p/CtOJZkvoag8/"


#Название базы данных
db_name = "buzzguru_master"

# Данные для генерации клиентов
a = int(time.time())
client_email = (f"d.serakov+{a}+@buzzguru.com")
# client_email = "d.serakov+1686831144147765+@buzzguru.com"

print(client_email)



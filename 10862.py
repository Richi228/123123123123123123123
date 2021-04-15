import amino
import threading

client = amino.Client()
client.login(email="jkturhen277@mailto.plus", password="lfiekz228")
sub_client = amino.SubClient(comId="156542274", profile=client.profile)

@client.event("on_group_member_join")
def on_join(data):
    if data.message.author.level <= 1:
        threading.Thread(target=sub_client.kick, args=[data.message.author.userId, data.message.chatId, True]).start()
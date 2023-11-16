import tambotapi, random, requests, os
po1 = requests.get(
    "https://raw.githubusercontent.com/m6hmd/za/main/peoms").text.split("$$$$")
so1 = requests.get("https://raw.githubusercontent.com/m6hmd/za/main/songs").text.split(
    "$$$$")
p1 = requests.get(
    "https://raw.githubusercontent.com/m6hmd/a1/main/n1").text.split("$$$$")
n1 = requests.get("https://pastebin.com/raw/knDKNwGG").text.split("$$$$")
n3 = requests.get("https://pastebin.com/raw/BgycE5qk").text.split("$$$$")
n2 = requests.get("https://pastebin.com/raw/fvWzm8MF").text.split("$$$$")
token = "t7jgXiFaGlFSdqc4wYToEinEr9MfLofWpQzAskR6DRA"
channel_id = -73872872396476
bot = tambotapi.TamBot(token)


def subs(channel_id, token, user_id):
  response = requests.get(
      f'https://botapi.tamtam.chat/chats/{channel_id}/members?access_token={token}&user_ids={user_id}'
  ).text
  return response


bot = tambotapi.TamBot(token)


def main():
  chat_id = bot.get_chat_id()
  while True:
    try:
      last_update = bot.get_updates()
      if last_update:
        chat_id = bot.get_chat_id(last_update)
        user_id = bot.get_user_id(last_update)
        username = bot.get_username(last_update)
        type = bot.get_update_type(last_update)
        callback_id = bot.get_callback_id(last_update)
        text = bot.get_text(last_update)
        mid = bot.get_message_id(last_update)
        chatt = bot.get_chat_type(last_update)
        if "/all" in text:
                if username=="cooo" or username=="boss" or username=="sssn":
                  mess = str(text).replace('/all','')
                  if mess != "":
                    chats= bot.get_all_chats(100)["chats"]
                    numc = 0
                    for ccat in chats:
                       ch=  ccat["chat_id"]
                       if int(ch) != chat_id:
                        numc +=1
                        bot.send_message(f"{str(mess)}", int(ch))
                    bot.send_message(f"تم ارسال رسالتك للكل.. ✅ :: {str(numc)}", chat_id)
                  else:
                    chats= bot.get_all_chats(100)["chats"]
                    numac =0
                    numc = 0
                    for ccat in chats:
                       ch=  ccat["chat_id"]
                       if int(ch) != chat_id and str("-") in str(ccat):
                         numc +=1
                       elif int(ch) != chat_id and str("-") not in str(ccat):
                         numac +=1
                       
                    bot.send_message(f"عدد كروبات البوت.. ✅ :: {str(numc)}" +"\n" +f"عدد مشتركين البوت.. ✅ :: {str(numac)}", chat_id)
        elif type == "bot_started" and chatt == "dialog":
          bot.send_message(
              """ مرحباً بك بوت Adore3 ضيفه بگروبك وتونس  🌵.

- ارسل : /start للبدء 
ٴ——————————————""", chat_id)
        elif text == "/start" and chatt == "dialog":
          bot.send_reply_message("""هلا بيك حب  ...""", mid, chat_id)
        elif text == "بوت" and chatt == "chat":
          if 'is_admin' in subs(channel_id, token, user_id):
            bot.send_reply_message(text="""- مرحبا انا بوت Adore3 🧩 .

- ارسل : افتار ، ليش ، شيصير ، يجي ، شع ، غ.""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
          else:
            bot.send_reply_message(text="""يجب عليك الاشتراك في القناة اولا 

 القناة : http://tt.me/nnruu""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
        elif text == "ليش" and chatt == "chat":
          if 'is_admin' in subs(channel_id, token, user_id):
            mess = random.choices(n1)
            bot.send_reply_message(text=mess[0],
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
          else:
            bot.send_reply_message(text="""يجب عليك الاشتراك في القناة اولا 

 القناة : http://tt.me/nnruu""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
        elif text == "شيصير" and chatt == "chat":
          if 'is_admin' in subs(channel_id, token, user_id):
            mess = random.choices(n2)
            bot.send_reply_message(text="**" + mess[0] + "**",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
          else:
            bot.send_reply_message(text="""يجب عليك الاشتراك في القناة اولا 

 القناة : http://tt.me/nnruu""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
        elif text == "شع" and chatt == "chat":
          if 'is_admin' in subs(channel_id, token, user_id):
            songn = random.randint(1, 9437478758574)
            son = requests.get(str(random.choice(po1))).content
            open(f"zr{str(songn)}.mp3", 'wb').write(son)
            #song = random.choice(s1)

            bot.send_audio(content=f"zr{str(songn)}.mp3",
                           chat_id=chat_id,
                           text="تـمٛ اختـيِار شــعر اݪـك 🎙️🔖:")
            os.remove(f"zr{str(songn)}.mp3")
          else:
            bot.send_reply_message(text="""يجب عليك الاشتراك في القناة اولا 

         القناة : http://tt.me/nnruu""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
        elif text == "غ" and chatt == "chat":
          if 'is_admin' in subs(channel_id, token, user_id):
            songn = random.randint(1, 9437478758574)
            son = requests.get(str(random.choice(so1))).content
            open(f"zz{str(songn)}.mp3", 'wb').write(son)
            #song = random.choice(s1)

            bot.send_audio(content=f"zz{str(songn)}.mp3",
                           chat_id=chat_id,
                           text="تـمٛ اختـيِار غـنيهۃ اݪـك 🎙️🔖:")
            os.remove(f"zz{str(songn)}.mp3")
          else:
            bot.send_reply_message(text="""يجب عليك الاشتراك في القناة اولا 

 القناة : http://tt.me/nnruu""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
        elif text == "يجي" and chatt == "chat":
          if 'is_admin' in subs(channel_id, token, user_id):
            mess = random.choices(n3)
            bot.send_reply_message(text="**" + mess[0] + "**",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
          else:
            bot.send_reply_message(text="""يجب عليك الاشتراك في القناة اولا 

 القناة : http://tt.me/nnruu""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")
        elif text == "افتار" and chatt == "chat":
          if 'is_admin' in subs(channel_id, token, user_id):
            url = random.choice(p1)
            bot.send_image_url(url, chat_id, "تـمٛ اختـيِار افٓتٰار اݪـك 🍿🫘:")
          else:
            bot.send_reply_message(text="""يجب عليك الاشتراك في القناة اولا 

 القناة : http://tt.me/nnruu""",
                                   mid=mid,
                                   chat_id=chat_id,
                                   format="markdown")

        else:
          pass

    except:
      print("hi")
      continue


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    exit()

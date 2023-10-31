import webbrowser
import platform
class Whatsapp:
    def __init__(self):
        self.baseUrl  = "https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}"
    def openchat(self, phone:str):
        print(platform.system())
        if platform.system() == "Linux":
            webbrowser.open(f"https://web.whatsapp.com/send?phone={phone}")
        else:
            webbrowser.open(f"whatsapp://send?phone={phone}")

    def sendmessage(self, phone:str, message:str):
        print(platform.system())
        if platform.system() == "Linux":
            webbrowser.open(f"https://web.whatsapp.com/send?phone={phone}&text={message}")
        else:
            webbrowser.open(f"whatsapp://send?phone={phone}&text={message}")
    def sendfilemessage(self, phone, file):
        teste = 'https://media.sproutsocial.com/uploads/2017/02/10x-featured-social-media-image-size.png'
        url = f"whatsapp://send?phone={phone}&file=<{teste}>"
        webbrowser.open(url)
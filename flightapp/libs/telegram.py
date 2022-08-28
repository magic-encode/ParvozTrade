import requests

from django.conf import settings


class TeleBotClient:
    __PASE_MODE = "html"
    __SEND_MESSAGE = "/sendMessage"
    
    TYPE_SAVOL = "chat_id_savol"
    TYPE_ZAKAS = "chat_id_zakas"
    

    def __init__(self, base_url: str, token: str, chat_id: str) -> None:
        self.__token = token
        self.__chat_id = chat_id
        self.__base_url = base_url
        self.__main_url = f'{self.__base_url}{self.__token}'


    def send_message(self, text: str, _type: str) -> dict:
        if _type == self.TYPE_SAVOL:
            chat_id: str = self.__chat_id.get(self.TYPE_SAVOL)
            
        if _type == self.TYPE_ZAKAS:
            chat_id: str = self.__chat_id.get(self.TYPE_ZAKAS)
        
        params = {
            'text': text,
            'chat_id': chat_id,
            'parse_mode': self.__PASE_MODE
        }
        
        return requests.post(f'{self.__main_url}{self.__SEND_MESSAGE}', params)


telebot = TeleBotClient(
    **settings.MYSERVICE.get('telebot')
)
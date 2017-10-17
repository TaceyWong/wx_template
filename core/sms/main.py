# coding:utf-8

from twilio.rest import Client

client = Client("AC44416bfb198cb785b19eb5ace63d3179", "b45ac5981acaf45e74e6898e910259af")


client.messages.create(to="+8617600361536",
                       from_="+13343104990",
                       body="中文测试")

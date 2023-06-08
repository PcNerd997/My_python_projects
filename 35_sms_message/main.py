from twilio.rest import Client

USER_ID = "ACea2ddf495eed1b11d313b82a81213eb8"
AUTH_ID = "2ecbd22cc829ebfec644a40a1e72e973"

client = Client(USER_ID, AUTH_ID)

message = client.messages.create(body= "Dey play sho gbo", from_= "+15855342968", to = "+2348167138071")

print(message.status)
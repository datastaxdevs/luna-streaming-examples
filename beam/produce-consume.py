import requests
import json

beamUrl = "http://127.0.0.1:8085";

tenantName = "public";
namespace = "default";
topicName = "my-beam-topic2";

topic = "persistent://{0}/{1}/{2}".format(tenantName, namespace, topicName)

# Produce a message
response = requests.post(beamUrl + "/v2/firehose/persistent/{0}/{1}/{2}".format(tenantName, namespace, topicName), data="Hi there!")
print("Published 1 message ({0})".format(response.status_code))

# Consume a message
response = requests.get(beamUrl + "/v2/poll/persistent/{0}/{1}/{2}?SubscriptionType=shared&SubscriptionInitialPosition=earliest&SubscriptionName=my-beam-subscription".format(tenantName, namespace, topicName))
print("Consumed messages ({0}):\n".format(response.status_code) + json.dumps(response.json(),indent=2))
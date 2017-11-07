import simpletr64

"""

# discover
device_list = simpletr64.Discover.discover()
print(device_list)

if len(device_list) == 0:
	print('No upnp server found.')
	exit(0)

for deviceResponse in device_list:
	# print(deviceResponse.location)	# print description xml file http path

	# connect specific server
	try:
		server = simpletr64.DeviceTR64(hostname=deviceResponse.locationHost, port=deviceResponse.locationPort, protocol=deviceResponse.locationProtocol) #.createFromURL('http://192.168.50.48:12346/description.xml')
		urlOfXMLDefinition = deviceResponse.location
		server.loadDeviceDefinitions(urlOfXMLDefinition)
		name = server.deviceInformations['friendlyName']
		model = server.deviceInformations['modelName']
		print('name:{0}, model:{1}'.format(name, model))
		print('=======')
	except Exception as e:
		print(e)

"""

# print(simpletr64.discover.Discover.discover())
# print('--------')
# print(simpletr64.Discover.discover())
# print('--------')

server = simpletr64.DeviceTR64(hostname='192.168.50.48', port='12346') #.createFromURL('http://192.168.50.48:12346/description.xml')
urlOfXMLDefinition = 'http://192.168.50.48:12346/description.xml'
server.loadDeviceDefinitions(urlOfXMLDefinition)

# register device
# r = server.execute(
# 	'/X_MS_MediaReceiverRegistrar.control',
# 	'urn:microsoft.com:service:X_MS_MediaReceiverRegistrar:1',
# 	'RegisterDevice',
# 	2,
# 	RegistrationReqMsg=12345)

# x = server.execute(
# 	'/ConnectionManager.control',
# 	'urn:schemas-upnp-org:service:ConnectionManager:1',
# 	'GetSystemUpdateID')

y = server.execute(
	'/ContentDirectory.control',
	'urn:schemas-upnp-org:service:ContentDirectory:1',
	'Browse',
	2,
	ObjectID='138_3',
	BrowseFlag="BrowseDirectChildren",
	Filter='*',
	StartingIndex='0',
	RequestedCount=0,
	SortCriteria=''
)


print(y)


# print(server.deviceInformations)

# description = requests.get(urlOfXMLDefinition)

# from lxml import etree
# root = etree.fromstring(description.text)


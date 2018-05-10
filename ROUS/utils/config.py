import ConfigParser
import imp
import utils


settings_path = "ROUS/settings.ini"

#
def config_path(basepath):
	return utils.file_path(basepath)


# returns a config file object
def config_parser(file):
	config = ConfigParser.SafeConfigParser()
	config.read(file)
	return config


# return path of item
def settings(item):
	config = config_parser( config_path(settings_path) )
	for section in config.sections():
		for (name, path) in config.items(section):
			if name == item:
				return path



# scans config file and returns list of all
# 	the services that are defined
configuration = settings("configuration")
def all_services():
	config = config_parser( configuration )
	services = []
	for section in config.sections():
		for (function, file) in config.items(section): 
			if not (function == "file"): 
				services.append(function)
	return services

#
def call_service(service, sender_address):
	print service
	config = config_parser( configuration )
	for section in config.sections():
		for (function, file) in config.items(section): 
			if(function == service):
				print file
				file = "ROUS/"+file
				filepath = utils.file_path(file)
				print filepath
				#try:
				module = imp.load_source(function, filepath)
				print module
				call_func = getattr(module, function) #the goods, magic is here
				call_func(sender_address)
				return True
				#except:
				#	return False
	return False

from configparser import ConfigParser

# config = ConfigParser()
# config.read("conf.ini")
# print(config.get("locator","username"))
# print(config.get("basic info","testsiteurl"))


def readConfig(section,key):
    config = ConfigParser()
    config.read(r"Confugaration/conf.ini")
    return config.get(section,key)

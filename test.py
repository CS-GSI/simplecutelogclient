import configparser
import zmq
print(zmq.pyzmq_version())
config = configparser.ConfigParser()
config.read('FILE.INI')
config['TCP']['HOST'] = '/var/shared/'    # update
config['TCP']['default_message'] = 'Hey! help me!!'   # create

with open('FILE.INI', 'w') as configfile:    # save
    config.write(configfile)
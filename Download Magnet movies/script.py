from deluge_client import DelugeRPCClient

client = DelugeRPCClient('127.0.0.1', 58846, 'username', 'password')
client.connect()

magnet_link = "magnet:?xt=urn:btih:3c4a0e3f8b3e69d82a7b5b5c13080cf47316b5c6&dn=Sample.txt"
download_options = {
    'download_location': './downloads/',
}

client.call('core.add_torrent_magnet', magnet_link, download_options)
print("Magnet link added!")

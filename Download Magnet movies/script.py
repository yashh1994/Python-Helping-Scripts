import libtorrent as lt
import time

ses = lt.session()
params = {
    'save_path': './downloads/',  # Folder to save downloads
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True
}
handle = lt.add_magnet_uri(ses, "magnet_link_here", params)

print("Downloading metadata...")
while not handle.has_metadata():
    time.sleep(1)
print("Metadata downloaded, starting torrent download...")

while handle.status().state != lt.torrent_status.seeding:
    s = handle.status()
    print(f"Download: {s.progress * 100:.2f}% complete (down: {s.download_rate / 1000:.2f} kB/s up: {s.upload_rate / 1000:.2f} kB/s peers: {s.num_peers})")
    time.sleep(5)

print("Download complete!")

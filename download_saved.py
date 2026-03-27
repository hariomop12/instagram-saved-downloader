import instaloader
import browser_cookie3
import time

USERNAME = "proxmoxbaby"

COOKIE_PATH = "/home/hariom/insta/cookies.sqlite"

L = instaloader.Instaloader(
    download_videos=True,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    compress_json=False,
)

print("Loading cookies from Zen Browser...")
cookiejar = browser_cookie3.firefox(
    cookie_file=COOKIE_PATH,
    domain_name=".instagram.com"
)
L.context._session.cookies.update(cookiejar)
L.context.username = USERNAME

print(f"Logged in as: {USERNAME}")
print("Fetching saved posts...")

profile = instaloader.Profile.from_username(L.context, USERNAME)

count = 0
for post in profile.get_saved_posts():
    try:
        L.download_post(post, target=":saved")
        count += 1
        print(f"[{count}] Downloaded: {post.shortcode} | Type: {'Video' if post.is_video else 'Image'}")
        time.sleep(4)
    except Exception as e:
        print(f"Error on {post.shortcode}: {e}")
        time.sleep(6)

print(f"\nDone! Total downloaded: {count}")

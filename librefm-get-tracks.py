import pylast
import sys

username = sys.argv[2]
password_hash = pylast.md5(sys.argv[1])

network = pylast._Network(password_hash = password_hash, username = username, name = "Libre.fm",
                    homepage = "http://alpha.libre.fm",
                    ws_server = ("alpha.libre.fm", "/2.0/"),
                    api_key = "",
                    api_secret = "",
                    session_key = "",
                    submission_server = "http://turtle.libre.fm:80/",
                    domain_names = {},
                    urls = {
                        "album": "artist/%(artist)s/album/%(album)s",
                        "artist": "artist/%(artist)s",
                        "event": "event/%(id)s",
                        "country": "place/%(country_name)s",
                        "playlist": "user/%(user)s/library/playlists/%(appendix)s",
                        "tag": "tag/%(name)s",
                        "track": "music/%(artist)s/_/%(title)s",
                        "group": "group/%(name)s",
                        "user": "user/%(name)s",
                        })

print network
print network.get_top_tags(limit=10)



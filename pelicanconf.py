AUTHOR = 'Doogle'
SITENAME = 'dooglewoogle'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Pacific/Auckland'
DEFAULT_LANG = 'English'
THEME = "dev-random"

DISPLAY_PAGES_ON_MENU = True

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

HOMEPAGE = "landing"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
CATEGORIES = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["lightbox", "image_process"]

IMAGE_PROCESS = {
    "thumb": {
            "type": "image",
            "ops": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
        },
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}
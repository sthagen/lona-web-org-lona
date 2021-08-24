PROJECT_NAME = 'lona'
CONTENT_ROOT = 'content'
OUTPUT_ROOT = 'output'

THEME_PATHS = [
    'theme',
]

PLUGINS = [
    'flamingo.plugins.Menu',
    'flamingo.plugins.Git',
    'flamingo.plugins.Thumbnails',
    'flamingo.plugins.PhotoSwipe',
    'flamingo.plugins.SphinxThemes',

    'plugins/toc_tree.py::TocTree',
    'plugins/rst_setting.py::rstSetting',
    'plugins/pygments.py::rstPygments',
]

MENU = [
    ['Lona', [
        ['Basic Concept', 'basic-concept.rst'],
        ['FAQ', 'faq.rst'],
        ['News / Getting Help', 'news-getting-help.rst'],
        ['How To Contribute', 'how-to-contribute.rst'],
        ['Contributors', 'contributors.rst'],
        ['Changelog', 'changelog.rst'],
        ['License', 'license.rst'],
        ['Stickers', 'stickers.rst'],
    ]],

    ['End User Documentation', [
        ['Getting Started', 'end-user-documentation/getting-started.rst'],
        ['Lona Scripts', 'end-user-documentation/lona-scripts.rst'],
        ['Views', 'end-user-documentation/views.rst'],
        ['HTML', 'end-user-documentation/html.rst'],
        ['Frontends', 'end-user-documentation/frontends.rst'],
        ['Error Views', 'end-user-documentation/error-views.rst'],
        ['Middlewares', 'end-user-documentation/middlewares.rst'],
        ['Settings', 'end-user-documentation/settings.rst'],
        ['Sessions', 'end-user-documentation/sessions.rst'],
        ['Lona Shell', 'end-user-documentation/lona-shell.rst'],
        ['Debugging', 'end-user-documentation/debugging.rst'],
        ['Deployment', 'end-user-documentation/deployment.rst'],
    ]],

    ['Cookbook', [
        ['Using Traditional HTML', 'cookbook/using-traditional-html.rst'],
        ['Writing A Lona Form', 'cookbook/writing-a-lona-form.rst'],

        ['Writing A Traditional Form',
         'cookbook/writing-a-traditional-form.rst'],

        ['Writing A Daemon View', 'cookbook/writing-a-daemon-view.rst'],

        ['Writing A Multi User View',
         'cookbook/writing-a-multi-user-view.rst'],

        ['URL Reverse Resolving', 'cookbook/url-reverse-resolving.rst'],
        ['Using Server State', 'cookbook/using-server-state.rst'],
        ['Integrating Django', 'cookbook/integrating-django.rst'],
        ['Limit Concurrent Views', 'cookbook/limit-concurrent-views.rst'],

        ['Adding A Custom Command To Lona Shell',
         'cookbook/adding-a-custom-command-to-lona-shell.rst'],
    ]],

    [['Contrib'], [
        ['Django', 'contrib/django/index.rst'],
        ['Chart.js', 'contrib/chartjs/index.rst'],
    ]],
]

DEFAULT_GALLERY_TEMPLATE = 'photoswipe/gallery.html'
DEFAULT_IMAGE_TEMPLATE = 'photoswipe/image.html'

SPHINX_THEMES_HTML_THEME = 'sphinx_rtd_theme'
SPHINX_THEMES_LOGO = 'logo.svg'
SPHINX_THEMES_DOCSTITLE = 'Lona'
SPHINX_THEMES_SHORTTITLE = 'Lona'
SPHINX_THEMES_PROJECT = 'Lona'

SPHINX_THEMES_EXTRA_STYLESHEETS = [
    '/static/photoswipe/photoswipe.css',
    '/static/photoswipe/default-skin/default-skin.css',
    '/static/custom.css',
]

SPHINX_THEMES_EXTRA_SCRIPTS = [
    '/static/photoswipe/photoswipe.min.js',
    '/static/photoswipe/photoswipe-ui-default.min.js',
    '/static/photoswipe/photoswipe-init.js',
]

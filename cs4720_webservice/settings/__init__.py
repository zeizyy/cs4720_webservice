
# Import production settings.
from cs4720_webservice.settings.production import *

# Import optional local settings.
try:
    from cs4720_webservice.settings.local import *
except ImportError:
    pass

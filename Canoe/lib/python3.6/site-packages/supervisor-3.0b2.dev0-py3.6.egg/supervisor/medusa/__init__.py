"""medusa.__init__
"""

# created 2002/03/19, AMK

__revision__ = "$Id: __init__.py,v 1.2 2002/03/19 22:49:34 amk Exp $"


# The following methods are added to string module to simplify python3 portage
import string
string.split = lambda txt, sep=None, maxsplit=99999: txt.split(sep, maxsplit)
string.join = lambda lst, sepChar="": sepChar.join(lst)
string.atoi = lambda txt: int(txt)
string.lower = lambda txt: txt.lower()
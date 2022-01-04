# can import
import math
# can NOT import
# import mymodule

# how Python looks for modules
import sys

print(sys.path)
print(type(sys.path))

for p in sys.path:
    print(p)


sys.path.append('C:\PROJECTS\EBSCO\ci\platform.shared.language-classifier-lz\app')

import language_classifier

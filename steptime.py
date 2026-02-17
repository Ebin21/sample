# Source - https://stackoverflow.com/a/53957673
# Posted by Aman Raparia, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-14, License - CC BY-SA 4.0

import datetime

start_time = datetime.datetime.now()
print(start_time)
while True:
    if (datetime.datetime.now() - start_time).seconds == 1:
       start_time = datetime.datetime.now()
       print(start_time)

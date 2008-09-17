# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
# 
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
# 
# The Original Code is Reddit.
# 
# The Original Developer is the Initial Developer.  The Initial Developer of the
# Original Code is CondeNet, Inc.
# 
# All portions of the code written by CondeNet are Copyright (c) 2006-2008
# CondeNet, Inc. All Rights Reserved.
################################################################################
from r2.models import *

def populate(sr_name = 'reddit.com', start_account = 1, sr_title = "reddit.com: what's new online"):
    sr = Subreddit._new(name= sr_name, title = sr_title)
    sr._commit()
    for i in range(start_account,(start_account + 4)):
        name = 'test' + str(i)
        password = name
        user = register(name, password)
        for j in range(1, 30):
            link_id = str(i) + '_' + str(j)
            url = 'http://google.com/?q=' + link_id
            title = user.name + ' ' + link_id
            Link._submit(title, url, user, sr, '127.0.0.1')
            

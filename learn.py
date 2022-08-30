Back-end complete function Template for Python 3

from collections import defaultdict
from typing import List
class Solution:
    def mergeDetails(self, details : List[List[str]]) -> List[List[str]]:
        id_parents = list(range(len(details)))
        
        def find_parent(x):
            if id_parents[x] != x:
                id_parents[x] = find_parent(id_parents[x])
            return id_parents[x]

        def union(old, new):
            parent_old = find_parent(old)
            parent_new = find_parent(new)
            if parent_old != parent_new:
                id_parents[new] = parent_old
            return parent_old
        
        email_to_id = {} # map email to its id group, used for checking existing emails
        for curr_id, account in enumerate(details):
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = curr_id
                else:
                    curr_id = union(email_to_id[email], curr_id)
            
        id_to_emails = defaultdict(list) # map name to a set of emails
        for email in email_to_id:
            id_group = find_parent(email_to_id[email])
            id_to_emails[id_group].append(email)
        
        ans = []
        for id_group in id_to_emails:
            sorted_emails = sorted(id_to_emails[id_group])
            ans.append([details[id_group][0]]+sorted_emails)
    
        return ans
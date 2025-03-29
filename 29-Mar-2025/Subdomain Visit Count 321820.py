# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_count=defaultdict(int)

        for domains in cpdomains:
            count, sub_domains= domains.split(" ")
            sbs= sub_domains.split('.')
            for i in range(len(sbs)):
                domains_count['.'.join(sbs[i:])]+=int(count)
        res=[]
        for domain, count in domains_count.items():
            res.append(str(count)+" "+ domain)
        return res
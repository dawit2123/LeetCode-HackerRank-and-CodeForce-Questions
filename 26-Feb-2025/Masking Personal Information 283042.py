# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            return self.check_for_email(s)
        else:
            return self.check_for_phone_number(s)
    def check_for_phone_number(self, s):
        local_number, country_code="", ""
        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit():
                if len(local_number)<10:
                    local_number+=s[i]
                else:
                    country_code+=s[i]
        local_number, country_code= local_number[::-1], country_code[::-1]
        x_value= local_number[-4:]
        if len(country_code)==0:
            return "***-***-"+x_value
        elif len(country_code)==1:
            return "+*-***-***-"+x_value
        elif len(country_code)==2:
            return "+**-***-***-"+x_value
        elif len(country_code)==3:
            return "+***-***-***-"+x_value
    def check_for_email(self, s):
        index= s.index('@')
        name, domain= s[:index], s[index+1:].lower()
        names_char= ["*"]*7
        names_char[0], names_char[len(names_char)-1]= name[0].lower(), name[len(name)-1].lower()
        return "".join(names_char)+"@"+domain
'''
Created on Sep 6, 2015

@author: yangke
'''
import re
class LineOfCode:
    
    #===========================================================================
    # def __init__(self, numStr, codeStr,func_call_info):
    #     self.linenum = int(numStr)
    #     self.codestr = codeStr
    #     self.sub_code_list = None
    #     self.func_call_info=func_call_info
    #===========================================================================
        
    def __init__(self, line, func_call_info):
        
        lineNumPattern = re.compile(r'^[1-9][0-9]*')
        lineNumStr = re.findall(lineNumPattern,line)[0]
        codestr = line.lstrip(lineNumStr)#note that there are space character before the codeline
        self.linenum = int(lineNumStr)
        self.codestr = codestr
        self.expand_code_list = None
        self.func_call_info=func_call_info

    def get_func_call_info(self):
        return self.func_call_info

    def set_func_call_info(self, value):
        self.func_call_info = value

        
    def get_sub_code_list(self):
        return self.sub_code_list

    def set_sub_code_list(self, value):
        self.sub_code_list = value

    def get_linenum(self):
        return self.linenum


    def get_codestr(self):
        return self.codestr


    def set_linenum(self, value):
        self.linenum = int(value)


    def set_codestr(self, value):
        self.codestr = value
        
    def __str__(self): 
        return str(self.linenum) + self.codestr
        
    def __eq__(self,obj):
        return isinstance(obj,LineOfCode) and str(self)==str(obj)\
            and self.func_call_info == obj.func_call_info
            #and self.expand_code_list == obj.expand_code_list
            
    def __hash__(self):
        return hash(str(self))^hash(self.func_call_info) 
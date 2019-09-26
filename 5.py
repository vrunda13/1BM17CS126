class calldetail():
    def __init__(s,call,scall,ti,ty):
        s.called=call
        s.sendcall=scall
        s.duration=ti
        s.type=ty

class util():
    def __init__(s):
        s.list_of_call_objects=None
        s.l=[]

    def parse_customer(s,list_of_call_string):
        s.list_of_call_objects=[]
        for i in list_of_call_string:
           pho,se,t,typ=map(str,i.split(","))
           s.list_of_call_objects.append(calldetail(pho,se,t,typ))
        for j in s.list_of_call_objects:
            print(j.called,j.sendcall,j.duration,j.type)

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
util().parse_customer(list_of_call_string)
           
                
                

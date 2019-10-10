open_lists=["[","(","{"]
closed_li=["]",")","}"]
def check(myst):
	st=[]
	for i in myst:
		if i in open_lists:
			st.append(i)
		elif i in closed_li:
			pos=closed_li.index(i)
			if len(st)>0 and open_lists[pos]==st[len(st)-1]:
				st.pop()
			else: return "umatched"
	if len(st)==0 :
		return "matched"

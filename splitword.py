import wrdtoimage as wti
def start():

	i=1
	with open('file.txt','r') as f:
	    for line in f:
	        for word in line.split():
			wti.txt_to_img(word,str(i))
			i=i+1
		
            

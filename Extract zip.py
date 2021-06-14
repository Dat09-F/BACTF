import zipfile

for x in range(999,-1,-1):
	name = str(x) +'.zip'
	with zipfile.ZipFile(name,"r") as zip_ref:
   	 zip_ref.extractall()

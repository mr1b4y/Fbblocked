import requests,bs4,re,getpass
from multiprocessing.pool import ThreadPool

print("\n\t[ Facebook Mass Block By Deray ]\n")

class mass_blocks:
	def __init__(self):
		self.token=""
		self.req=requests.Session()
		self.url="https://mbasic.facebook.com/{}"
		self.getfriend()
		
	def blocks(self,*args,**kwds):
		name=requests.get(
			"https://graph.facebook.com/%s?access_token=%s"%(
			re.findall("bid=(.*?)&",args[0])[0],
		self.token)).json()["name"]
		self.req.post(args[0],data=kwds).text
		print("+ %s -> blocked. "%(name))
		
	def getfriend(self):
		self.email=raw_input("[+] Login\n[+] Email: ")
		self.passs=getpass.getpass("[+] Passs: ")
		t=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+self.email+"&locale=en_US&password="+self.passs+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
		try:
			self.token=t["access_token"]
			print("[+] getting friends ...")
			self.req.post(self.url.format("login"),
			data=
				{
					"email":self.email,
					"pass":self.passs
				})
		except Exception as f:
			exit("- Errno: %s"%(f))
		self.getfr()
		
		
	def getfr(self):
		kambing=[]
		for x in requests.get('https://graph.facebook.com/me/friends?access_token='+self.token).json()["data"]:
			kambing.append(x["id"])
		print("[+] friends: %s"%(len(kambing)))
		self.got(kambing)
		
	def got(self,kambing):
		try:
			self.ranges=input("[?] how many friends u want to blocks? ")
			
		except:return self.got(kambing)
		self.threads(kambing)
		
	def threads(self,kambing):
		p=[]
		for x in kambing:
			p.append(x)
			if len(p) == self.ranges:
				break
			
		print("[+] blocking %s friends ...\n"%(len(p)))
		t=ThreadPool(100)
		t.map(self.kam,p)
	
			
	def kam(self,i):
		
		POSTDATA=[]
		bs=bs4.BeautifulSoup(
			self.req.get(
				self.url.format(
			"/privacy/touch/block/confirm/?bid="+i)).text,
		features="html.parser")
		for x in bs("form"):
			if "block" in x["action"]:
				POSTDATA.append(
					self.url.format(
				x["action"]))
		for x in bs("input"):
			try:
				if "fb_dtsg" in x["name"]:
					POSTDATA.append(x["value"])
				if "jazoest" in x["name"]:
					POSTDATA.append(x["value"])
				if "confirmed" in x["name"]:
					POSTDATA.append(x["value"])
					break
			except:pass
		try:
			self.blocks(POSTDATA[0],
				fb_dtsg=POSTDATA[1],
					jazoest=POSTDATA[2],
						confirmed=POSTDATA[3])
		except Exception as f:
			pass
				
			
mass_blocks()
class Contact:
	def __init__(self,name,phone):
		self.name=name
		self.phone=phone
		
	def display(self):
			print(f"{self.name}:{self.phone}")
			
c1=Contact("Akshat","73098-039")
c2=Contact("rahul","790890890")

c1.display()
c2.display()			
			
from . import works

"""
	allows iterating through a collection of works (usually obtained from a search)
	
	for bugs please mention: lambricm
"""

class WorkList(object):

	def __init__(self, works=set()):
		self.works = set()
		
		self.add_works(works)
		self.work_iter = iter(self.works)
		
	def add_works(self, works):
		if (type(works) == type([])):
			for work in works:
				self.works.add(work)
		elif (type(works) == type(set())):
			self.works = self.works.union(works)

		self.work_iter = iter(self.works)
		
	def __add__(self, other_worklist):
		if other_worklist == None:
			return self
		else:
			return WorkList(self.works.union(other_worklist.works))
			
	def __repr__(self):
		return str(self.works)
		
	@property
	def next_work(self):
		try:
			id = next(self.work_iter)
			work = works.Work(id)
			return work
		except:
			return None
			
	@property
	def num_works(self):
		return len(self.works)
from __future__ import annotations
from collections.abc import Iterable, Callable



class Rollbackable:

	def __init__(self: Rollbackable, do: Callable, undo: Callable):
		self.do = do
		self.undo = undo

	def __call__(self: Rollbackable, *args, **kwargs):
		self.results.append(self.do(*args, **kwargs))

	def __enter__(self: Rollbackable) -> Rollbackable:
		
		self.results: Iterable = []
		
		return self
	
	def __exit__(self: Rollbackable, type, value, traceback) -> None:
		
		if type:
			
			for r in self.results:
			
				try:
					self.undo(r)
				except Exception:
					pass
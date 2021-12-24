import os
import glob
import shutil
import pytest
from growing_tree_base import saveToDirTree

from rollbackable import Rollbackable



def test_example():

	shutil.rmtree('root', ignore_errors=True)

	def f():
	
		for i in range(10):
			saveToDirTreeRollbackable('', 'root', base_file_name='.xml')
		
		saveToDirTreeRollbackable('', '$&#@!*)', base_file_name='.xml')

	with pytest.raises(OSError):
		with Rollbackable(saveToDirTree, os.remove) as saveToDirTreeRollbackable:
			f()
	
	assert not glob.glob('root/*.xml')
	shutil.rmtree('root')
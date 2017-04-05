def fetcher(obj, index):
	return obj[index]
def after():
	try:
		fetcher('spam',3)
	finally:
		print 'got exception'
	print "after try."
after()

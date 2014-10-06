def new(num_buckets=256):
	""" Initializes a Map with the given number of buckets. """
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap


def hash_key(aMap, key):
	""" Given a key, this will create a number and then convert it to an index for the aMap's buckets. """
	return hash(key) % len(aMap)  # using the modulus operator here
	# len(aMap) tells how many buckets there are, and hash is a built-in python function that turns basically anything into a number, and doing the modulo is a way to make the index number a reasonable size
	
	
def get_bucket(aMap, key):
	""" Given a key, find the bucket where it would go. """
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]


def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)
	print enumerate(bucket)
	
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, default
	# using this function to find where the key could be makes searching much less than what it would be normally.
	
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)
	return v
	# If there's no value assigned to a given key, it returns 'None'


def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not exist, append to create it
		bucket.append((key, value))


def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break


def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v


def dump(aMap):
	""" Dumps the contents of every bucket."""
	for bucket in aMap:
		print bucket


# A hashmap is a list of buckets, which are a list of slots, which have key/value pairs in them.
# A bucket is 'cities' or 'states'
# A slot is where a key and value pair are stored in a bucket, like 'Florida' and 'FL' for a state bucket.
#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("key-0", 'value-0')
my_cache.print_cache()
my_cache.put("key-1", 'value-0')
my_cache.print_cache()
my_cache.put("key-2", 'value-2')
my_cache.print_cache()
my_cache.put("key-3", 'value-3')
my_cache.print_cache()

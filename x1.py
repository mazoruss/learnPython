# -*- coding: utf-8 -*-

# ============================================

# # ===============lesson 4 ================

# cars = 5

# print 'there are', cars, 'cars.'

# # =============== lesson 5 =============

# tree = 'one'
# size = 10

# print 'there is %s trees.' % tree
# print 'it\'s %d stories tall and %s million dollars' % (size, tree)

# # ============= lesson 6 ===================

# x = 'there are %d types of people' % 10
# binary = 'binary'
# do_not = "don't"
# y = 'those who know %s and those who %s' % (binary, do_not)

# print x
# print y

# print 'i said %r' % x
# print "i also said '%s'" % y

# hilarious = False
# joke_evaluation = "isn't that joke so funny? %r"

# print joke_evaluation % hilarious

# w = 'left side'
# e = 'a string'

# print w + e

# # =============== lesson 7 ================

# print 'cheese',
# print 'burger'

# print '.' * 10

# ================ lesson 8 ==================

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	'this thing',
	'next thing',
	'what thing',
	'that thing'
	)


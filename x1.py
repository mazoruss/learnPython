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

# # ================ lesson 8 ==================

# formatter = "%r %r %r %r"

# print formatter % (1, 2, 3, 4)
# print formatter % ('one', 'two', 'three', 'four')
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % (
# 	'this thing',
# 	'next thing',
# 	'what thing',
# 	'that thing'
# )

# # ================ lesson 9 ==================
# days = 'Mon Tue Wed'
# months = 'Jan\nFeb\nMar'

# print 'days: ', days
# print 'months: ', months 

# print '''
# things 
# more things
# '''

# # =================== lesson 10 =====================

# tab = '\t tabs'
# newline = '\n new lines'
# slashes = '\\ slashes \\'
# triples = '''
# list: 
# \t 1
# \t 2
# \t 3
# '''

# print(tab)
# print(newline)
# print(slashes)
# print(triples)

# # =============== lesson 11 ================
# print 'how old are you?',
# age = raw_input()

# print 'you are %r years old' % age

# # =============== lesson 12 =================
# name = raw_input('name? ')
# age = int(raw_input('age? '))

# print 'you are %s and you are %d years old' % ( name, age )

# # ============== lesson 13 =================
# from sys import argv

# script, first, second, third = argv

# print 'script is: ', script
# print 'first variable is: ', first
# print 'second is: ', second
# print 'third is: ', third

# ================= lesson 14 ===================
from sys import argv

script, user = argv

prompt = '> '

print "Hi %s, I'm the %s script" % (user, script)
print "how are you, %s" % user
answer1 = raw_input(prompt)
print "what kind of computer do you have?"
answer2 = raw_input(prompt)

print '''
Alright, so you are doing %r
and you have a %r, awesome!
''' % (answer1, answer2)




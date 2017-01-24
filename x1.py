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

# # ================= lesson 14 ===================
# from sys import argv

# script, user = argv

# prompt = '> '

# print "Hi %s, I'm the %s script" % (user, script)
# print "how are you, %s" % user
# answer1 = raw_input(prompt)
# print "what kind of computer do you have?"
# answer2 = raw_input(prompt)

# print '''
# Alright, so you are doing %r
# and you have a %r, awesome!
# ''' % (answer1, answer2)

# # ============== lesson 15 ==============

# from sys import argv

# script, file = argv

# txt = open(file)

# print "here's your file %r" % file
# print txt.read()

# print "new file" 
# file2 = raw_input('> ')

# txt2 = open(file2)
# print txt2.read()


# ============== lesson 16 ==============

from sys import argv

script, file = argv

print "we are going to erase %r"
print "if you don't want to do that, press CTRL+C"
print "otherwise hit ENTER"

raw_input('?')

print "opening the file"

target = open(file, 'w')

print "truncating the file"
target.truncate()

print "now I'm going to ask for three lines"
line1 = raw_input('line 1: ')
line2 = raw_input('line 2: ')
line3 = raw_input('line 3: ')

print "I'm going to write these to the file"
target.write(line1 + '\n')
target.write(line2 + '\n')
target.write(line3 + '\n')

print 'then we close it'
target.close()

# ============== lesson 17 ==============
# ============== lesson 18 ==============
# ============== lesson 19 ==============
# ============== lesson 20 ==============
# ============== lesson 21 ==============
# ============== lesson 22 ==============
# ============== lesson 23 ==============
# ============== lesson 24 ==============
# ============== lesson 25 ==============
# ============== lesson 26 ==============
# ============== lesson 27 ==============
# ============== lesson 28 ==============
# ============== lesson 29 ==============
# ============== lesson 30 ==============
# ============== lesson 31 ==============
# ============== lesson 32 ==============
# ============== lesson 33 ==============
# ============== lesson 34 ==============
# ============== lesson 35 ==============
# ============== lesson 36 ==============
# ============== lesson 37 ==============
# ============== lesson 38 ==============
# ============== lesson 39 ==============
# ============== lesson 40 ==============
# ============== lesson 41 ==============
# ============== lesson 42 ==============
# ============== lesson 43 ==============
# ============== lesson 44 ==============
# ============== lesson 45 ==============
# ============== lesson 46 ==============
# ============== lesson 47 ==============
# ============== lesson 48 ==============
# ============== lesson 49 ==============
# ============== lesson 50 ==============
# ============== lesson 51 ==============
# ============== lesson 52 ==============
# ============== lesson 53 ==============
# ============== lesson 54 ==============




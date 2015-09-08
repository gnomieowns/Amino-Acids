import random

aa = ["alanine",
	"arginine, pKa = ?",
	"asparagine",
	"aspartic acid, pKa = ?",
	"cysteine",
	"glutamic acid, pKa = ?",
	"glutamine",
	"glycine",
	"proline",
	"serine",
	"tyrosine, pKa = ?",
	"histidine, pKa = ?",
	"isoleucine",
	"leucine",
	"lysine, pKa = ?",
	"methionine",
	"phenylalanine",
	"threonine",
	"tryptophan",
	"valine"]
	
random.shuffle(aa)

print

ii = 1

while len(aa) != 0:
	print "{}. {}".format(ii,aa.pop())
	ii += 1
	raw_input("")
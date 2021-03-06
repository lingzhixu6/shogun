# This software is distributed under BSD 3-clause license (see LICENSE file).
#
# Authors: Soumyajit De

#!/usr/bin/env python

from tools.load import LoadMatrix

lm=LoadMatrix()
traindat = lm.load_dna('../data/fm_train_dna.dat')
testdat = lm.load_dna('../data/fm_test_dna.dat')

parameter_list = [[traindat,testdat,2,0.75],[traindat,testdat,3,0.75]]

def kernel_ssk_string (fm_train_dna=traindat, fm_test_dna=testdat, maxlen=1, decay=1):
	from shogun import SubsequenceStringKernel
	from shogun import StringCharFeatures, DNA

	feats_train=StringCharFeatures(fm_train_dna, DNA)
	feats_test=StringCharFeatures(fm_test_dna, DNA)

	kernel=SubsequenceStringKernel(feats_train, feats_train, maxlen, decay)

	km_train=kernel.get_kernel_matrix()
	# print(km_train)
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()
	# print(km_test)
	return km_train,km_test,kernel

if __name__=='__main__':
	print('SubsequenceStringKernel DNA')
	kernel_ssk_string(*parameter_list[0])
	kernel_ssk_string(*parameter_list[1])

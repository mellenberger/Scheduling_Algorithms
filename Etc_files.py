from ETC_deadlines import *

t = 5
m = 3
u = 1000

#low task low machine
CVB_ETC_1(t, m, 0.1, 0.1, u, 'new_matrices/LT_LM_Inconsistent.txt', 'inconsistent')
CVB_ETC_1(t, m, 0.1, 0.1, u, 'new_matrices/LT_LM_PartiallyConsistent.txt', 'partiallyconsistent')
CVB_ETC_1(t, m, 0.1, 0.1, u, 'new_matrices/LT_LM_Consistent.txt', 'consistent')

#low task high machine 
CVB_ETC_2(t, m, 0.1, 0.6, u, 'new_matrices/LT_HM_Inconsistent.txt', 'inconsistent')
CVB_ETC_2(t, m, 0.1, 0.6, u, 'new_matrices/LT_HM_PartiallyConsistent.txt', 'partiallyconsistent')
CVB_ETC_2(t, m, 0.1, 0.6, u, 'new_matrices/LT_HM_Consistent.txt', 'consistent')

#high task low machine
CVB_ETC_1(t, m, 0.5, 0.1, u, 'new_matrices/HT_LM_Inconsistent.txt', 'inconsistent')
CVB_ETC_1(t, m, 0.5, 0.1, u, 'new_matrices/HT_LM_PartiallyConsistent.txt', 'partiallyconsistent')
CVB_ETC_1(t, m, 0.5, 0.1, u, 'new_matrices/HT_LM_Consistent.txt', 'consistent')

#high task high machine
CVB_ETC_1(t, m, 0.6, 0.6, u, 'new_matrices/HT_HM_Inconsistent.txt', 'inconsistent')
CVB_ETC_1(t, m, 0.6, 0.6, u, 'new_matrices/HT_HM_PartiallyConsistent.txt', 'partiallyconsistent')
CVB_ETC_1(t, m, 0.6, 0.6, u, 'new_matrices/HT_HM_Consistent.txt', 'consistent')
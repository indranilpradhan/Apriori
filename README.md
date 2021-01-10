# Apriori

As per the standard technique, in order to find L k , the frequent itemsets of size
k from L k−1 , the frequent itemsets of size k − 1, a two-step process is followed,
consisting of join and prune actions for the candidate generation, i.e., to find
C k and hence starting from 1−frequent itemsets, we get to reach the k-frequent
itemsets . Now a brute force approach is somewhat expensive and call for certain
optimisations .
• Partitioning : Distributed and Parallel algorithms for apriori based
frequent itemset mining obey a rule : If the database D is divided into
n partitions and frequent itemset mining is performed in each of them
individually, any itemset that is potentially frequent with respect to D
must occur as a frequent itemset in at least one of those n partitions.
Now the run of F IM on each of those partitions can be done paralelly
and all the local frequent itemsets generated can be checked for being
globally frequent by a scan of the database again . Note : You do not
need to significantly parallelise the algorithm . Just try out what can be
a suitable partitioning, and perform sequentially the apriori generation in
each of them, look at what was the maximum time needed among the
individual runs to get an idea of how much parallelising this would have
helped .
• Transaction Reduction : A transaction that does not contain any fre-
quent k-itemsets cannot contain any frequent (k + 1)-itemsets. Therefore,
such a transaction can be marked or removed from further consideration .
This is an easy task and hence recommended as a to be tried optimisation.
• Hash based Technique : When scanning each transaction in the
database to generate the frequent 1-itemsets, L 1 , we can generate all
the 2-itemsets for each transaction, hash (i.e., map) them into the dif-
ferent buckets of a hash table structure, and increase the corresponding
bucket counts. A 2-itemset with a corresponding bucket count in the hash
table that is below the support threshold cannot be frequent and thus
should be removed from the candidate set. Refer to figure 6.5 of Han,Kimber , Pei for clear understanding . Note : This can be generalised to
other k’s than just 2, but for the sake of simplicity, let’s just stick to 2 for
this project .


Tasks :
• Implement the entire apriori algorithm in any of the allowed languages
using any 2 of the above strategies . Run the algorithm on few datasets
from the given dataset library .
• State your partitioning strategy or the hash mapping whichever of the 2
you choose respectively.
• Compare the performance of your new implementation with the standard
version. Do not worry the optimisation strategies are generally to be ap-
plied on very large databases, so it might not show sufficient improvement
on datasets we use, so try to optimise as far as possible and state the
improvements you have got .

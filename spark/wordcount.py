from pyspark import SparkContext,SparkConf

conf=SparkConf()
conf.setMaster("spark://spark:7077")
conf.setAppName("test application")


logFile="file:///mnt/demo2.txt"
sc=SparkContext(conf=conf)
logData=sc.textFile(logFile).cache()


numAs=logData.filter(lambda s: 'a' in s).count()
numBs=logData.filter(lambda s: 'b' in s).count()

print "Lines with a:%i,lines with b:%i" % (numAs,numBs)

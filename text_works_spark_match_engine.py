import os
import sys
import math
import re

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
from pyspark.sql.functions import lit
from datetime import datetime
from timeit import timeit

def validatefiles(path):
    val = os.system("hadoop fs -test -e %s" %path)
    if val != 0: return 0
    else: return 1
    
def programexit(errormessage):
	print "The program is exiting with the error message: " + errormessage
	exit(-1)
	
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Missing parameters - Usage: CFPB_Text_Matching <inputpath> <channel> <horton/stampy>")
		exit(-1)
	print "Parameters count matched"
	sourcefile = sys.argv[1]
	channel = sys.argv[2]
	environment = sys.argv[3]
	rundate = str(datetime.now().strftime("%Y%m%d"))
	print "The source file name is: "+sourcefile
	print "The channel name is: "+channel
	print "The cluster is: "+environment
	basepath = "hdfs://horton//apps/dt/gops/"
	
	inputpath = basepath+"dragnet/"+channel+"/"
	#inputfile = "text_works."+channel+".****."+"prepared_source.dat.gz"
	inputfile = "hdfs://"+environment+"/"+sourcefile
	##ginputpath = sc.broadcast(inputpath)
	##ginputfile = sc.broadcast(inputfile)
	print "Input file path is: "+inputfile
	print "Checking for input file"
	inputstatus = validatefiles(inputfile)
	
	if(inputstatus == 0):
		print "Input file not found in the path"
		exit(-1)
	else:
		print "Input file found"
		
		
	outputfolder = rundate + channel
	outputpath = basepath+"cfpb/output/"+outputfolder
	print "Output path is: "+outputpath
	print "Checking for output directory"
	
	outputstatus = validatefiles(outputpath)
	if(outputstatus == 0):
		print "Output file will be created in the path: "+ outputpath
	else:
		print "Output path already exists. Please move or rename it."
		exit(-1)
	
		
	print "Creating SparkConf"
	conf = (SparkConf()
		 .setAppName("CFPB_Text_matching")
		 .set("spark.dynamicAllocation.enabled", "false")
		 .set("spark.sql.parquet.compression.codec", "uncompressed")
		 .set("spark.shuffle.compress", "true")
		 .set("spark.io.compression.codec", "snappy")
		 .set("spark.driver.allowMultipleContexts", "true"))
		 
	print "Creating SparkContext"
	sc = SparkContext(conf = conf)

	print "Creating SQLContext"
	sqlContext = SQLContext(sc)
	sqlContext.setConf("spark.sql.shuffle.partitions", "1")
	print "Accessing input files"
	##Horton
	head, tail = os.path.split(inputfile)
	##text_works.venmo.1598.prepared_source.dat.gz
	runid = str(int(re.search(r'\d+', tail).group()))
	print "File name: "+tail
	print "RunId: "+runid
	txtsrcchnl = sc.textFile("hdfs:////user/hive/warehouse/pp_cs_tables.db/dim_cs_txt_src_chnl/*").cache()
	input = sc.textFile(inputfile).cache()
	txtpattern = sc.textFile("hdfs:////user/hive/warehouse/pp_cs_tables.db/dim_cs_txt_pattern/*").cache()
	txtchnl_map = sc.textFile("hdfs:////user/hive/warehouse/pp_cs_tables.db/dim_cs_txt_chnl_map/*").cache()
	
	patternfields = txtpattern.map(lambda l: l.split("\001"))
	patterns = patternfields.map(lambda p: Row(txt_key=p[0], txt_pattern=p[1],txt_ln=p[2]))
	schemapatrns = sqlContext.createDataFrame(patterns)
	PAT = schemapatrns.alias('PAT')
	PAT.count()

	chmapfields = txtchnl_map.map(lambda l: l.split("\001"))
	chnls = chmapfields.map(lambda p: Row(CHNL_TXT_MAP_KEY=p[0], TXT_KEY=p[1], TXT_CAT_KEY=p[2],
					CHNL_KEY=p[3], IS_ACTV_Y_N=p[6]))
	schemachnls = sqlContext.createDataFrame(chnls)
	CHN = schemachnls.where(schemachnls["IS_ACTV_Y_N"]=='Y')
	CHN.count()

	newCHN = CHN.join(PAT, CHN.TXT_KEY == PAT.txt_key,'inner').select \
		(CHN.CHNL_TXT_MAP_KEY, CHN.TXT_KEY, CHN.TXT_CAT_KEY, CHN.CHNL_KEY, PAT.txt_pattern, PAT.txt_ln)

	srcchnlfields = txtsrcchnl.map(lambda l: l.split("\001"))
	srcchnls = srcchnlfields.map(lambda p: Row(CHNL_KEY=p[0], CHNL_NM=p[1], SUB_CHNL_NM=p[2],
					CHNL_TYPE=p[3], ENTITY_KEY=p[4],IS_ACTV_Y_N=p[7]))
	schemasrcchnl = sqlContext.createDataFrame(srcchnls)
	SC = schemasrcchnl.where(schemasrcchnl["IS_ACTV_Y_N"]=='Y')

	prepfields = input.map(lambda l: l.split("|"))
	prep = prepfields.map(lambda p: Row(ID=p[0], INTERACTION_ID=p[1], INTERACTION_TS=p[2], EMPLOYEE_ID=p[3],
					CHANNEL_CUST_ID=p[4],PAYPAL_CUST_ID=p[5],LANGUAGE=p[6], 
					MESSAGE=p[8],SUBCHNL_NM=p[7]))

	schemaprep = sqlContext.createDataFrame(prep)
	PFB = schemaprep.alias('PFB').cache()
	print "Number of input records: "+str(PFB.count())

	newPFB = PFB.join(SC, PFB.SUBCHNL_NM == SC.SUB_CHNL_NM,'inner').select \
		 (PFB.INTERACTION_ID,PFB.INTERACTION_TS,PFB.EMPLOYEE_ID,PFB.CHANNEL_CUST_ID,PFB.PAYPAL_CUST_ID, \
		 PFB.MESSAGE,SC.CHNL_KEY)
	newPFB.count()
	##newPFB.registerTempTable("newPFB")

	SCMnew = newCHN.where(newCHN["CHNL_KEY"].isin(newPFB.map(lambda l:l.CHNL_KEY).collect()))
	##SCMnew.registerTempTable("SCMnew")
	SCMnew.count()

	patterns = SCMnew.map(lambda l: (l.txt_pattern.lower(), l.CHNL_TXT_MAP_KEY, l.CHNL_KEY, l.TXT_KEY))
	
	#input list
	ilist=[]
	for (a,b,c,d,e,f,g) in newPFB.collect():
	    arr=[a,b,c,d,e,f,g]
	    ilist.append(arr)
	
	#base list
	blist =[]
	##runid = str(rundate + channel)
	cdate = str(datetime.now().strftime("%Y-%m-%d"))
	pc=[]
	pc = patterns.collect()
	
	print "Scanning for patterns"
	for (pattern,mapkey,chkey,txtkey) in pc:
		ctime = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		templist = [(a,b,c,d,e,f,g,mapkey,pattern,runid,cdate,ctime,txtkey) for a,b,c,d,e,f,g in ilist 
		if( (int(g)==int(chkey)) and (re.search("[^a-z0-9@_-]"+pattern+"[^a-z0-9@\'_]",f,re.I)
		or re.search("([ ])"+pattern+"$",f,re.I) or re.search("^"+pattern+"[ ]",f,re.I)) )]
		blist+=templist

	trdd=sc.parallelize(blist)
	qrdd=trdd.map(lambda l:(l[9],l[7],l[0],l[1],1 if (len(l[5])-len(l[5].lower().replace(l[8],"")))/len(l[8])==0 else 
	(len(l[5])-len(l[5].lower().replace(l[8],"")))/len(l[8]),l[10]
	,l[11],l[2],l[4],l[3].encode('utf-8'),l[12] ))

	finalRDD=qrdd.map(lambda l: str(l[0])+"\t"+str(l[1])+"\t"+str(l[10])+"\t"+str(l[2])+"\t"+str(l[3])+"\t"\
	+str(l[4])+"\t"+str(l[4])+"\t"+str(l[5])+"\t"+str(l[6])+"\t"+str(l[7])+"\t"+str(l[8])+"\t"+str(l[9]))
	
	print "Number of patterns matched: "+str(finalRDD.count())
	print "Scanning completed. Validating output directory"
	
	
	finalRDD.coalesce(1).saveAsTextFile(outputpath)
	print "Output file has been created successfully("+outputpath+")"
	sc.stop()
	print "Spark Job completed for the channel - "+ channel + " on "+rundate

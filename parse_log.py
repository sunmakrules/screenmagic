import csv

logfile = 'example.log' #Log File to be read
csvfile = 'parsedlog.csv' #CSV File
temp = [] #Temporary List of Dictionaries to write log data to csv

#Method to read the log file 
def read_logs():
	print ("Reading Logs...")
	with open(logfile,'r',encoding='utf-8') as logf: #Handles unicode
		reader = csv.reader(logf)
		for row in reader:
			if len(row) == 0:
				continue
			date = row[0]
			rows = row[1].split() #splitting the level and message data
			level = rows[0]
			message = ' '.join(rows[1:])
			temp.append({'Date':date,'Level':level,'Message':message}) #appends dictionary to temp list

#Method to write the data to csv file
def write_to_csv():
	print ("Writing to CSV.")
	fieldnames = ['Date','Level','Message']
	with open(csvfile,'w',encoding='utf-8') as writer: #Handles unicode
		csvwriter = csv.DictWriter(writer,delimiter=',',fieldnames=fieldnames)
		csvwriter.writerow(dict((fn,fn) for fn in fieldnames)) #Writes Header to csv file.
		for row in temp:
			csvwriter.writerow(row) #writes the row to csv file.
		pass

#Method to report the log data
def reporting():
	print("Creating Report.\n")
	date = []
#To get the date out of date and time (as written to log)
	for row in temp:
		d = [v for v in row['Date'].split(' ')] 
		date.append(d[0])
	date = list(set(date)) #To get the distinct dates from the list of dates
	print('\nDate\t','Errors\t','Warnings')
#counts the errors and warnings from distinct list of dates.
	pdate = [date[i] for i in range(0,len(date))]
	for i in range(0,len(pdate)):
		ecount = 0 #Error count
		wcount = 0 #Warnings count
		with open(csvfile,'r',encoding='utf-8') as repo:
			for word in repo.read().split(','):
				if pdate[i] in word:
					parts = word.split(' ') #Further splits the list to get every word as a single items
					if 'ERROR' in parts:
						ecount += 1
					elif 'WARNING' in parts:
						wcount += 1

#Prints the report for as per the date
		print(pdate[i],ecount,wcount)


if __name__ == "__main__":
    read_logs()
    write_to_csv()
    reporting()

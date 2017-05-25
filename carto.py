import requests as r

data = r.get('https://s3.amazonaws.com/carto-1000x/data/yellow_tripdata_2016-01.csv', stream=True);

lines  = 0;
column = 0;

# tip_amount -> column 16.
count  = 0.0;
charBuffer = str("0");

for chunk in data.iter_content(chunk_size=2048):
	if(chunk):
		for c in chunk:
			
			if(column==15 and c!=44):
			# tip_amount column, any char except ','
				charBuffer += chr(c);
			
			elif(c==44):
			# ',' = 44 (ascii)
				column += 1;
				if(charBuffer != "0"):
					if(lines != 0):
						# we skip csv headers
						# can be changed for a try-catch block
						# for CSVs with/without headers.
						try:
							count += float(charBuffer);
						except:
							count += float(charBuffer.split('-')[1])/2;	

					charBuffer = "0";

			# '\n' = 10 (ascii)
			elif(c==10):
				lines  += 1;
				column  = 0;
				# print(lines, count, "\n");
				
print('Lines: ', lines, '\n', 'Avg value for tip_amount: ', float(count/lines), '\n');

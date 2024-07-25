import csv #import to use the csv module


with open('MachineLearningCVE/output_file.csv', mode='a') as f:
        writer = csv.writer(f)
        with open('Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv', mode="r") as csv_file: #"r" represents the read mode
            reader = csv.reader(csv_file) #this is the reader object
            count = 0
     #this is the writer object
   # writer.writerow(column_name) # this will list out the names of the columns which are always the first entrries
            for item in reader:
                print(count)
                print(item[-1])
                if(item[-1] == "DDoS"):
                    count = count + 1
                    writer.writerow(item)
                    # print(item)
                if(count == 5000):
                    break
        
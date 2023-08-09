# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"104611.0","system":"med"},{"code":"10691.0","system":"med"},{"code":"11106.0","system":"med"},{"code":"11107.0","system":"med"},{"code":"11670.0","system":"med"},{"code":"11740.0","system":"med"},{"code":"12353.0","system":"med"},{"code":"12442.0","system":"med"},{"code":"1399.0","system":"med"},{"code":"1476.0","system":"med"},{"code":"16225.0","system":"med"},{"code":"16237.0","system":"med"},{"code":"16587.0","system":"med"},{"code":"17259.0","system":"med"},{"code":"17330.0","system":"med"},{"code":"17607.0","system":"med"},{"code":"18156.0","system":"med"},{"code":"18636.0","system":"med"},{"code":"19494.0","system":"med"},{"code":"20514.0","system":"med"},{"code":"20762.0","system":"med"},{"code":"2081.0","system":"med"},{"code":"2082.0","system":"med"},{"code":"2083.0","system":"med"},{"code":"2084.0","system":"med"},{"code":"21624.0","system":"med"},{"code":"21650.0","system":"med"},{"code":"21713.0","system":"med"},{"code":"21879.0","system":"med"},{"code":"22277.0","system":"med"},{"code":"24064.0","system":"med"},{"code":"24485.0","system":"med"},{"code":"24984.0","system":"med"},{"code":"25110.0","system":"med"},{"code":"26106.0","system":"med"},{"code":"26323.0","system":"med"},{"code":"27342.0","system":"med"},{"code":"28780.0","system":"med"},{"code":"2925.0","system":"med"},{"code":"29691.0","system":"med"},{"code":"30162.0","system":"med"},{"code":"30404.0","system":"med"},{"code":"30460.0","system":"med"},{"code":"30604.0","system":"med"},{"code":"30695.0","system":"med"},{"code":"31443.0","system":"med"},{"code":"31742.0","system":"med"},{"code":"3216.0","system":"med"},{"code":"32927.0","system":"med"},{"code":"32964.0","system":"med"},{"code":"33635.0","system":"med"},{"code":"33670.0","system":"med"},{"code":"33839.0","system":"med"},{"code":"36296.0","system":"med"},{"code":"36748.0","system":"med"},{"code":"37605.0","system":"med"},{"code":"37691.0","system":"med"},{"code":"37946.0","system":"med"},{"code":"38061.0","system":"med"},{"code":"39327.0","system":"med"},{"code":"39799.0","system":"med"},{"code":"40530.0","system":"med"},{"code":"41920.0","system":"med"},{"code":"41983.0","system":"med"},{"code":"43193.0","system":"med"},{"code":"4500.0","system":"med"},{"code":"4501.0","system":"med"},{"code":"4506.0","system":"med"},{"code":"45169.0","system":"med"},{"code":"46677.0","system":"med"},{"code":"4743.0","system":"med"},{"code":"47555.0","system":"med"},{"code":"4915.0","system":"med"},{"code":"54505.0","system":"med"},{"code":"5611.0","system":"med"},{"code":"56410.0","system":"med"},{"code":"56947.0","system":"med"},{"code":"5740.0","system":"med"},{"code":"5758.0","system":"med"},{"code":"57714.0","system":"med"},{"code":"59574.0","system":"med"},{"code":"61383.0","system":"med"},{"code":"6169.0","system":"med"},{"code":"62000.0","system":"med"},{"code":"63529.0","system":"med"},{"code":"64101.0","system":"med"},{"code":"64389.0","system":"med"},{"code":"6467.0","system":"med"},{"code":"65754.0","system":"med"},{"code":"65932.0","system":"med"},{"code":"67651.0","system":"med"},{"code":"68111.0","system":"med"},{"code":"69691.0","system":"med"},{"code":"7602.0","system":"med"},{"code":"7885.0","system":"med"},{"code":"7943.0","system":"med"},{"code":"8030.0","system":"med"},{"code":"8363.0","system":"med"},{"code":"8388.0","system":"med"},{"code":"94553.0","system":"med"},{"code":"94670.0","system":"med"},{"code":"9489.0","system":"med"},{"code":"95181.0","system":"med"},{"code":"96053.0","system":"med"},{"code":"96054.0","system":"med"},{"code":"96993.0","system":"med"},{"code":"97309.0","system":"med"},{"code":"9849.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcohol-problems-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcohol---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcohol---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcohol---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

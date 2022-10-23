import csv

if __name__ == '__main__':
    # ファイルopen
    with open('./test_in.csv') as f1:
        with open('./test_out.csv', 'w') as f2:

            reader = csv.reader(f1)
            writer = csv.writer(f2)

            for row in reader:
                writer.writerow(row)

    with open('./test_in.csv') as f:
        reader = csv.reader(f)

        for row in reader:
            print(row[1])
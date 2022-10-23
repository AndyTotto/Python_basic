import csv

if __name__ == '__main__':
   # ファイルopen(読み込み用)
    with open('./test_in.csv') as f1:
        # ファイルのopen(書き込み用)
        with open('./test_out.csv', 'w') as f2:
            # 読み込み操作用readerの設定
            reader = csv.reader(f1)
            # 書き込み操作用writerの設定
            writer = csv.writer(object)

            # 一行目のヘッダは処理しないので、区別のための変数
            header_flag = 0
            # 一行ずつ読み込み→処理→書き込み
            for row in reader:
                # 1行目(ヘッダー)の時は新しいヘッダーを追記
                if(header_flag == 0):
                    # ヘッダーフラグを1にして2行目行こうはこの処理に飛ばないようにする
                    header_flag = 1
                    # ヘッダーを追記
                    row.append("include tax")
                    # 書き込み
                    writer.writerow(row)
                    continue

                # 2行目行こうは税込価格の計算をして追記
                # priceを取得して、税率8%を計算
                tax = float(row[1]) * 1.08
                # 小数点以下を四捨五入して追記
                row.append(round(tax))
                # 書き込み
                writer.writerow(row)

            print(object)
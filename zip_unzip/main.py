import shutil

# 圧縮 (【圧縮先】, 【圧縮拡張子】, 【圧縮するディレクトリ】
shutil.make_archive("./test_zip/test", "zip", "./test_in/")

# 解凍(【解凍したいファイル】, 【解凍したファイルの配置先】)
shutil.unpack_archive("./test_zip/test.zip", "./test_unzip/")

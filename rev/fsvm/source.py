r0 = "0" # 0
r0 += "1" # 1
r0 = str(int(r0) + int(r0)) # 3
r1 = "0" # 7
r1 = str(int(r0) + int(r1)) # 8
r0 = str(int(r0) + int(r0)) # 12
r0 = str(int(r0) + int(r0)) # 16
r0 = str(int(r0) + int(r1)) # 20
r2 = "0" # 24
r2 += "1" # 25
r2 = str(int(r2) + int(r2)) # 27
r4 = r0 + r2 # 31
r4 = chr(int(r4)) # 35
r2 = str(int(r2) + int(r2)) # 38
r2 = str(int(r2) + int(r2)) # 42
r2 = r0 + r2 # 46
r2 = chr(int(r2)) # 50
r4 = r4 + r2 # 53
r2 = "0" # 57
r2 += "1" # 58
r1 = "0" # 60
r1 = str(int(r2) + int(r1)) # 61
r2 = str(int(r1) + int(r2)) # 65
r2 = str(int(r2) + int(r2)) # 69
r2 = str(int(r1) + int(r2)) # 73
r2 = r2 + r2 # 77
r2 = chr(int(r2)) # 81
r1 = str(int(r1) + int(r1)) # 84
r1 = str(int(r2) + int(r1)) # 88
r2 = r1 + r2 # 92
r2 = chr(int(r2)) # 96
r4 = r4 + r2 # 99
r3 = "0" # 103
r3 += "1" # 104
r1 = "0" # 106
r1 = str(int(r3) + int(r1)) # 107
r3 = str(int(r3) + int(r3)) # 111
r3 = str(int(r3) + int(r1)) # 115
r0 = r0 + r3 # 119
r0 = chr(int(r0)) # 123
r4 = r4 + r0 # 126
r0 = "0" # 130
r0 += "1" # 131
r1 = "0" # 133
r1 = str(int(r0) + int(r1)) # 134
r1 = str(int(r0) + int(r1)) # 138
r0 = str(int(r0) + int(r1)) # 142
r1 = "0" # 146
r1 = str(int(r0) + int(r1)) # 147
r0 = str(int(r1) + int(r0)) # 151
r0 += "1" # 155
if r1[0] == '-':
	r1 = 0
else:
	r1 = "-" + r1 # 157
r0 = str(int(r0) + int(r1)) # 159
r0 = chr(int(r0)) # 163
r4 = r4 + r0 # 166
print(r4) # 170
r5 = "0" # 171
r6 = "" # 172
r7 = "" # 173
r0 = input() # 174
r1 = "0" # 175
r1 += "1" # 176
r2 = "0" # 178
r2 = str(int(r1) + int(r2)) # 179
r1 += "1" # 183
r1 = str(int(r1) + int(r2)) # 185
r2 = "0" # 189
r2 += "1" # 190
r3 = "0" # 192
r3 = str(int(r2) + int(r3)) # 193
r2 = str(int(r2) + int(r2)) # 197
r2 = str(int(r2) + int(r2)) # 201
r2 = str(int(r2) + int(r3)) # 205
r1 = r1 + r2 # 209
r2 = str(ord(r0[len(r0)-1])) # size # 213
if len(r0):
	r0 = r0[:-1] # 216
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 218
r2 = str(int(r2) + int(r1)) # 220
r6 = r2 + r6 # 224
r7 = r5 + r7 # 228
r1 = "0" # 232
r1 += "1" # 233
r2 = "0" # 235
r2 = str(int(r1) + int(r2)) # 236
r1 += "1" # 240
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 242
r1 = str(int(r2) + int(r1)) # 244
r1 += "1" # 248
r1 = str(int(r2) + int(r1)) # 250
r2 = str(int(r2) + int(r2)) # 254
r2 = str(ord(r0[len(r0)-1])) # size # 258
if len(r0):
	r0 = r0[:-1] # 261
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 263
r2 = str(int(r2) + int(r1)) # 265
r6 = r2 + r6 # 269
r7 = r5 + r7 # 273
r1 = "0" # 277
r1 += "1" # 278
r2 = "0" # 280
r2 = str(int(r1) + int(r2)) # 281
r1 = str(int(r2) + int(r1)) # 285
r1 = str(int(r1) + int(r1)) # 289
r1 = str(int(r2) + int(r1)) # 293
r1 += "1" # 297
r1 = str(int(r2) + int(r1)) # 299
r2 = str(ord(r0[len(r0)-1])) # size # 303
if len(r0):
	r0 = r0[:-1] # 306
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 308
r2 = str(int(r2) + int(r1)) # 310
r6 = r2 + r6 # 314
r7 = r5 + r7 # 318
r1 = "0" # 322
r1 += "1" # 323
r2 = "0" # 325
r2 = str(int(r1) + int(r2)) # 326
r2 = str(int(r2) + int(r2)) # 330
r1 = str(int(r1) + int(r2)) # 334
r2 = str(int(r1) + int(r1)) # 338
r1 = str(int(r1) + int(r2)) # 342
r1 = r1 + r1 # 346
r2 = str(ord(r0[len(r0)-1])) # size # 350
if len(r0):
	r0 = r0[:-1] # 353
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 355
r2 = str(int(r2) + int(r1)) # 357
r6 = r2 + r6 # 361
r7 = r5 + r7 # 365
r1 = "0" # 369
r1 += "1" # 370
r2 = "0" # 372
r2 = str(int(r1) + int(r2)) # 373
r1 = str(int(r2) + int(r1)) # 377
r1 = str(int(r1) + int(r1)) # 381
r1 = str(int(r2) + int(r1)) # 385
r1 = r1 + r1 # 389
r2 = str(ord(r0[len(r0)-1])) # size # 393
if len(r0):
	r0 = r0[:-1] # 396
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 398
r2 = str(int(r2) + int(r1)) # 400
r6 = r2 + r6 # 404
r7 = r5 + r7 # 408
r1 = "0" # 412
r1 += "1" # 413
r2 = "0" # 415
r2 = str(int(r1) + int(r2)) # 416
r1 = str(int(r2) + int(r1)) # 420
r1 = str(int(r1) + int(r1)) # 424
r1 = str(int(r2) + int(r1)) # 428
r1 = r1 + r1 # 432
r1 = str(int(r2) + int(r1)) # 436
r2 = str(ord(r0[len(r0)-1])) # size # 440
if len(r0):
	r0 = r0[:-1] # 443
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 445
r2 = str(int(r2) + int(r1)) # 447
r6 = r2 + r6 # 451
r7 = r5 + r7 # 455
r1 = "0" # 459
r1 += "1" # 460
r2 = "0" # 462
r2 += "1" # 463
r1 = r1 + r2 # 465
r2 = str(ord(r0[len(r0)-1])) # size # 469
if len(r0):
	r0 = r0[:-1] # 472
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 474
r2 = str(int(r2) + int(r1)) # 476
r6 = r2 + r6 # 480
r7 = r5 + r7 # 484
r1 = "0" # 488
r1 += "1" # 489
r2 = "0" # 491
r2 = str(int(r1) + int(r2)) # 492
r1 = str(int(r2) + int(r1)) # 496
r1 = str(int(r1) + int(r1)) # 500
r1 = str(int(r2) + int(r1)) # 504
r1 += "1" # 508
r1 = str(int(r2) + int(r1)) # 510
r2 = str(ord(r0[len(r0)-1])) # size # 514
if len(r0):
	r0 = r0[:-1] # 517
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 519
r2 = str(int(r2) + int(r1)) # 521
r6 = r2 + r6 # 525
r7 = r5 + r7 # 529
r1 = "0" # 533
r1 += "1" # 534
r2 = "0" # 536
r2 = str(int(r1) + int(r2)) # 537
r2 = str(int(r2) + int(r2)) # 541
r1 = str(int(r1) + int(r2)) # 545
r2 = str(int(r1) + int(r1)) # 549
r1 = str(int(r1) + int(r2)) # 553
r1 = r1 + r1 # 557
r2 = str(ord(r0[len(r0)-1])) # size # 561
if len(r0):
	r0 = r0[:-1] # 564
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 566
r2 = str(int(r2) + int(r1)) # 568
r6 = r2 + r6 # 572
r7 = r5 + r7 # 576
r1 = "0" # 580
r1 += "1" # 581
r1 = str(int(r1) + int(r1)) # 583
r2 = "0" # 587
r2 = str(int(r1) + int(r2)) # 588
r1 = str(int(r1) + int(r1)) # 592
r1 = str(int(r1) + int(r1)) # 596
r1 = str(int(r1) + int(r2)) # 600
r2 = "0" # 604
r2 += "1" # 605
r3 = "0" # 607
r3 = str(int(r2) + int(r3)) # 608
r2 = str(int(r2) + int(r2)) # 612
r2 = str(int(r2) + int(r2)) # 616
r2 = str(int(r2) + int(r2)) # 620
r2 = str(int(r2) + int(r3)) # 624
r1 = r1 + r2 # 628
r2 = str(ord(r0[len(r0)-1])) # size # 632
if len(r0):
	r0 = r0[:-1] # 635
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 637
r2 = str(int(r2) + int(r1)) # 639
r6 = r2 + r6 # 643
r7 = r5 + r7 # 647
r1 = "0" # 651
r1 += "1" # 652
r1 += "1" # 654
r2 = "0" # 656
r2 += "1" # 657
r2 = str(int(r2) + int(r2)) # 659
r2 = str(int(r2) + int(r2)) # 663
r2 = str(int(r2) + int(r2)) # 667
r1 = r1 + r2 # 671
r2 = str(ord(r0[len(r0)-1])) # size # 675
if len(r0):
	r0 = r0[:-1] # 678
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 680
r2 = str(int(r2) + int(r1)) # 682
r6 = r2 + r6 # 686
r7 = r5 + r7 # 690
r1 = "0" # 694
r1 += "1" # 695
r2 = "0" # 697
r2 += "1" # 698
r2 = str(int(r2) + int(r2)) # 700
r2 += "1" # 704
r1 = r1 + r2 # 706
r2 = str(ord(r0[len(r0)-1])) # size # 710
if len(r0):
	r0 = r0[:-1] # 713
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 715
r2 = str(int(r2) + int(r1)) # 717
r6 = r2 + r6 # 721
r7 = r5 + r7 # 725
r1 = "0" # 729
r1 += "1" # 730
r1 += "1" # 732
r2 = "0" # 734
r2 += "1" # 735
r3 = "0" # 737
r3 = str(int(r2) + int(r3)) # 738
r2 = str(int(r2) + int(r2)) # 742
r2 = str(int(r2) + int(r2)) # 746
r2 = str(int(r2) + int(r3)) # 750
r1 = r1 + r2 # 754
r2 = str(ord(r0[len(r0)-1])) # size # 758
if len(r0):
	r0 = r0[:-1] # 761
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 763
r2 = str(int(r2) + int(r1)) # 765
r6 = r2 + r6 # 769
r7 = r5 + r7 # 773
r1 = "0" # 777
r1 += "1" # 778
r2 = "0" # 780
r2 = str(int(r1) + int(r2)) # 781
r1 = str(int(r2) + int(r1)) # 785
r1 = str(int(r1) + int(r1)) # 789
r1 = str(int(r2) + int(r1)) # 793
r1 = r1 + r1 # 797
r1 = chr(int(r1)) # 801
r2 = str(int(r2) + int(r2)) # 804
r2 = str(int(r1) + int(r2)) # 808
r1 = r2 + r1 # 812
r2 = str(ord(r0[len(r0)-1])) # size # 816
if len(r0):
	r0 = r0[:-1] # 819
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 821
r2 = str(int(r2) + int(r1)) # 823
r6 = r2 + r6 # 827
r7 = r5 + r7 # 831
r1 = "0" # 835
r1 += "1" # 836
r2 = "0" # 838
r2 += "1" # 839
r1 = r1 + r2 # 841
r2 = str(ord(r0[len(r0)-1])) # size # 845
if len(r0):
	r0 = r0[:-1] # 848
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 850
r2 = str(int(r2) + int(r1)) # 852
r6 = r2 + r6 # 856
r7 = r5 + r7 # 860
r1 = "0" # 864
r1 += "1" # 865
r1 += "1" # 867
r2 = "0" # 869
r2 += "1" # 870
r2 = str(int(r2) + int(r2)) # 872
r2 = str(int(r2) + int(r2)) # 876
r1 = r1 + r2 # 880
r2 = str(ord(r0[len(r0)-1])) # size # 884
if len(r0):
	r0 = r0[:-1] # 887
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 889
r2 = str(int(r2) + int(r1)) # 891
r6 = r2 + r6 # 895
r7 = r5 + r7 # 899
r1 = "0" # 903
r1 += "1" # 904
r2 = "0" # 906
r2 += "1" # 907
r1 = r1 + r2 # 909
r2 = str(ord(r0[len(r0)-1])) # size # 913
if len(r0):
	r0 = r0[:-1] # 916
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 918
r2 = str(int(r2) + int(r1)) # 920
r6 = r2 + r6 # 924
r7 = r5 + r7 # 928
r1 = "0" # 932
r1 += "1" # 933
r2 = "0" # 935
r2 += "1" # 936
r3 = "0" # 938
r3 = str(int(r2) + int(r3)) # 939
r2 += "1" # 943
r2 = str(int(r2) + int(r3)) # 945
r1 = r1 + r2 # 949
r2 = str(ord(r0[len(r0)-1])) # size # 953
if len(r0):
	r0 = r0[:-1] # 956
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 958
r2 = str(int(r2) + int(r1)) # 960
r6 = r2 + r6 # 964
r7 = r5 + r7 # 968
r1 = "0" # 972
r1 += "1" # 973
r2 = "0" # 975
r2 += "1" # 976
r3 = "0" # 978
r3 = str(int(r2) + int(r3)) # 979
r2 = str(int(r2) + int(r2)) # 983
r2 = str(int(r2) + int(r2)) # 987
r2 = str(int(r2) + int(r2)) # 991
r2 = str(int(r2) + int(r2)) # 995
r2 = str(int(r2) + int(r3)) # 999
r1 = r1 + r2 # 1003
r2 = str(ord(r0[len(r0)-1])) # size # 1007
if len(r0):
	r0 = r0[:-1] # 1010
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1012
r2 = str(int(r2) + int(r1)) # 1014
r6 = r2 + r6 # 1018
r7 = r5 + r7 # 1022
r1 = "0" # 1026
r1 += "1" # 1027
r1 += "1" # 1029
r2 = "0" # 1031
r2 += "1" # 1032
r3 = "0" # 1034
r3 = str(int(r2) + int(r3)) # 1035
r2 = str(int(r2) + int(r2)) # 1039
r2 = str(int(r2) + int(r2)) # 1043
r2 = str(int(r2) + int(r3)) # 1047
r1 = r1 + r2 # 1051
r2 = str(ord(r0[len(r0)-1])) # size # 1055
if len(r0):
	r0 = r0[:-1] # 1058
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1060
r2 = str(int(r2) + int(r1)) # 1062
r6 = r2 + r6 # 1066
r7 = r5 + r7 # 1070
r1 = "0" # 1074
r1 += "1" # 1075
r2 = "0" # 1077
r2 = str(int(r1) + int(r2)) # 1078
r1 += "1" # 1082
r1 = str(int(r1) + int(r2)) # 1084
r2 = "0" # 1088
r2 += "1" # 1089
r3 = "0" # 1091
r3 = str(int(r2) + int(r3)) # 1092
r2 = str(int(r2) + int(r2)) # 1096
r2 = str(int(r2) + int(r3)) # 1100
r1 = r1 + r2 # 1104
r2 = str(ord(r0[len(r0)-1])) # size # 1108
if len(r0):
	r0 = r0[:-1] # 1111
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1113
r2 = str(int(r2) + int(r1)) # 1115
r6 = r2 + r6 # 1119
r7 = r5 + r7 # 1123
r1 = "0" # 1127
r1 += "1" # 1128
r2 = "0" # 1130
r2 = str(int(r1) + int(r2)) # 1131
r1 = str(int(r1) + int(r1)) # 1135
r1 = str(int(r1) + int(r2)) # 1139
r1 = str(int(r1) + int(r1)) # 1143
r1 = r1 + r1 # 1147
r1 = str(int(r2) + int(r1)) # 1151
r2 = str(ord(r0[len(r0)-1])) # size # 1155
if len(r0):
	r0 = r0[:-1] # 1158
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1160
r2 = str(int(r2) + int(r1)) # 1162
r6 = r2 + r6 # 1166
r7 = r5 + r7 # 1170
r1 = "0" # 1174
r1 += "1" # 1175
r2 = "0" # 1177
r2 = str(int(r1) + int(r2)) # 1178
r1 = str(int(r1) + int(r1)) # 1182
r1 = str(int(r1) + int(r1)) # 1186
r2 = str(int(r2) + int(r2)) # 1190
r1 = str(int(r1) + int(r1)) # 1194
r1 += "1" # 1198
r1 = str(int(r2) + int(r1)) # 1200
r2 = str(ord(r0[len(r0)-1])) # size # 1204
if len(r0):
	r0 = r0[:-1] # 1207
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1209
r2 = str(int(r2) + int(r1)) # 1211
r6 = r2 + r6 # 1215
r7 = r5 + r7 # 1219
r1 = "0" # 1223
r1 += "1" # 1224
r2 = "0" # 1226
r2 = str(int(r1) + int(r2)) # 1227
r1 = str(int(r1) + int(r1)) # 1231
r1 = str(int(r1) + int(r2)) # 1235
r1 = str(int(r1) + int(r1)) # 1239
r1 = r1 + r1 # 1243
r1 = str(int(r2) + int(r1)) # 1247
r2 = str(ord(r0[len(r0)-1])) # size # 1251
if len(r0):
	r0 = r0[:-1] # 1254
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1256
r2 = str(int(r2) + int(r1)) # 1258
r6 = r2 + r6 # 1262
r7 = r5 + r7 # 1266
r1 = "0" # 1270
r1 += "1" # 1271
r2 = "0" # 1273
r2 = str(int(r1) + int(r2)) # 1274
r1 = str(int(r1) + int(r2)) # 1278
r2 = str(int(r1) + int(r2)) # 1282
r1 = "0" # 1286
r1 = str(int(r2) + int(r1)) # 1287
r1 = str(int(r1) + int(r1)) # 1291
r2 = str(int(r1) + int(r2)) # 1295
r1 = r1 + r2 # 1299
r2 = str(ord(r0[len(r0)-1])) # size # 1303
if len(r0):
	r0 = r0[:-1] # 1306
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1308
r2 = str(int(r2) + int(r1)) # 1310
r6 = r2 + r6 # 1314
r7 = r5 + r7 # 1318
r1 = "0" # 1322
r1 += "1" # 1323
r1 += "1" # 1325
r2 = "0" # 1327
r1 = r1 + r2 # 1328
r2 = str(ord(r0[len(r0)-1])) # size # 1332
if len(r0):
	r0 = r0[:-1] # 1335
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1337
r2 = str(int(r2) + int(r1)) # 1339
r6 = r2 + r6 # 1343
r7 = r5 + r7 # 1347
r1 = "0" # 1351
r1 += "1" # 1352
r2 = "0" # 1354
r2 += "1" # 1355
r1 = r1 + r2 # 1357
r2 = str(ord(r0[len(r0)-1])) # size # 1361
if len(r0):
	r0 = r0[:-1] # 1364
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1366
r2 = str(int(r2) + int(r1)) # 1368
r6 = r2 + r6 # 1372
r7 = r5 + r7 # 1376
r1 = "0" # 1380
r1 += "1" # 1381
r1 += "1" # 1383
r2 = "0" # 1385
r2 += "1" # 1386
r2 = str(int(r2) + int(r2)) # 1388
r1 = r1 + r2 # 1392
r2 = str(ord(r0[len(r0)-1])) # size # 1396
if len(r0):
	r0 = r0[:-1] # 1399
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1401
r2 = str(int(r2) + int(r1)) # 1403
r6 = r2 + r6 # 1407
r7 = r5 + r7 # 1411
r1 = "0" # 1415
r1 += "1" # 1416
r2 = "0" # 1418
r2 = str(int(r1) + int(r2)) # 1419
r1 += "1" # 1423
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1425
r1 = str(int(r2) + int(r1)) # 1427
r1 += "1" # 1431
r1 = str(int(r2) + int(r1)) # 1433
r2 = str(int(r2) + int(r2)) # 1437
r2 = "0" # 1441
r2 += "1" # 1442
r2 += "1" # 1444
r1 = str(int(r1) + int(r2)) # 1446
r2 = str(ord(r0[len(r0)-1])) # size # 1450
if len(r0):
	r0 = r0[:-1] # 1453
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1455
r2 = str(int(r2) + int(r1)) # 1457
r6 = r2 + r6 # 1461
r7 = r5 + r7 # 1465
r5 = "0" # 1469
r5 += "1" # 1470
r3 = "0" # 1472
r3 = str(int(r5) + int(r3)) # 1473
r5 = str(int(r5) + int(r5)) # 1477
r5 = str(int(r5) + int(r5)) # 1481
if r3[0] == '-':
	r3 = 0
else:
	r3 = "-" + r3 # 1485
r5 = str(int(r5) + int(r5)) # 1487
r5 = str(int(r5) + int(r3)) # 1491
r5 += "1" # 1495
if r6 != r7: print(f"{r6} != {r7} jmp {r5}") # 1497
r4 = "" # 1498
r4 += "1" # 1499
r4 += "1" # 1501
r4 += "1" # 1503
r4 = chr(int(r4)) # 1505
r3 = "0" # 1508
r3 += "1" # 1509
r3 = str(int(r3) + int(r3)) # 1511
r2 = "0" # 1515
r2 = str(int(r3) + int(r2)) # 1516
r3 = str(int(r3) + int(r3)) # 1520
r3 = str(int(r3) + int(r3)) # 1524
r3 = str(int(r3) + int(r2)) # 1528
r2 = "0" # 1532
r2 += "1" # 1533
r1 = "0" # 1535
r1 = str(int(r2) + int(r1)) # 1536
r2 = str(int(r2) + int(r2)) # 1540
r1 = str(int(r2) + int(r1)) # 1544
r2 = str(int(r2) + int(r2)) # 1548
r2 = str(int(r2) + int(r1)) # 1552
r3 = r3 + r2 # 1556
r3 = chr(int(r3)) # 1560
r4 = r4 + r3 # 1563
print(r4) # 1567
exit() # 1568
r4 = "" # 1569
r4 += "1" # 1570
r4 += "1" # 1572
r4 += "1" # 1574
r3 = "0" # 1576
r3 = str(int(r4) + int(r3)) # 1577
r4 = chr(int(r4)) # 1581
r2 = "" # 1584
r2 += "1" # 1585
if r2[0] == '-':
	r2 = 0
else:
	r2 = "-" + r2 # 1587
r3 = str(int(r2) + int(r3)) # 1589
r3 = chr(int(r3)) # 1593
r4 = r3 + r4 # 1596
print(r4) # 1600
exit() # 1601

r0 = 0 # 0
r0 = 1 # 1
r0 = r0 + r0 # (long) # 3
r1 = 0 # 7
r1 = r0 + r1 # (long) # 8
r0 = r0 + r0 # (long) # 12
r0 = r0 + r0 # (long) # 16
r0 = r0 + r1 # (long) # 20
r2 = 0 # 24
r2 = 1 # 25
r2 = r2 + r2 # (long) # 27
r4 = r0 + r2 # (char) # 31
r4 = r4 # 35
r2 = r2 + r2 # (long) # 38
r2 = r2 + r2 # (long) # 42
r2 = r0 + r2 # (char) # 46
r2 = r2 # 50
r4 = r4 + r2 # (char) # 53
r2 = 0 # 57
r2 = 1 # 58
r1 = 0 # 60
r1 = r2 + r1 # (long) # 61
r2 = r1 + r2 # (long) # 65
r2 = r2 + r2 # (long) # 69
r2 = r1 + r2 # (long) # 73
r2 = r2 + r2 # (char) # 77
r2 = r2 # 81
r1 = r1 + r1 # (long) # 84
r1 = r2 + r1 # (long) # 88
r2 = r1 + r2 # (char) # 92
r2 = r2 # 96
r4 = r4 + r2 # (char) # 99
r3 = 0 # 103
r3 = 1 # 104
r1 = 0 # 106
r1 = r3 + r1 # (long) # 107
r3 = r3 + r3 # (long) # 111
r3 = r3 + r1 # (long) # 115
r0 = r0 + r3 # (char) # 119
r0 = r0 # 123
r4 = r4 + r0 # (char) # 126
r0 = 0 # 130
r0 = 1 # 131
r1 = 0 # 133
r1 = r0 + r1 # (long) # 134
r1 = r0 + r1 # (long) # 138
r0 = r0 + r1 # (long) # 142
r1 = 0 # 146
r1 = r0 + r1 # (long) # 147
r0 = r1 + r0 # (long) # 151
r0 = 1 # 155
if str(r1)[0] == '-':
	r1 = 0
else:
	r1 = -r1 # 157
r0 = r0 + r1 # (long) # 159
r0 = r0 # 163
r4 = r4 + r0 # (char) # 166
print(r4) # 170
r5 = 0 # 171
r6 = 0 # val # 172
r7 = 0 # val # 173
r0 = input() # 174
r1 = 0 # 175
r1 = 1 # 176
r2 = 0 # 178
r2 = r1 + r2 # (long) # 179
r1 = 1 # 183
r1 = r1 + r2 # (long) # 185
r2 = 0 # 189
r2 = 1 # 190
r3 = 0 # 192
r3 = r2 + r3 # (long) # 193
r2 = r2 + r2 # (long) # 197
r2 = r2 + r2 # (long) # 201
r2 = r2 + r3 # (long) # 205
r1 = r1 + r2 # (char) # 209
r0 = str(r0)[len(str(r2))-1] # size # 213
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 216
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 218
r2 = r2 + r1 # (long) # 220
r6 = r2 + r6 # (char) # 224
r7 = r5 + r7 # (char) # 228
r1 = 0 # 232
r1 = 1 # 233
r2 = 0 # 235
r2 = r1 + r2 # (long) # 236
r1 = 1 # 240
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 242
r1 = r2 + r1 # (long) # 244
r1 = 1 # 248
r1 = r2 + r1 # (long) # 250
r2 = r2 + r2 # (long) # 254
r0 = str(r0)[len(str(r2))-1] # size # 258
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 261
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 263
r2 = r2 + r1 # (long) # 265
r6 = r2 + r6 # (char) # 269
r7 = r5 + r7 # (char) # 273
r1 = 0 # 277
r1 = 1 # 278
r2 = 0 # 280
r2 = r1 + r2 # (long) # 281
r1 = r2 + r1 # (long) # 285
r1 = r1 + r1 # (long) # 289
r1 = r2 + r1 # (long) # 293
r1 = 1 # 297
r1 = r2 + r1 # (long) # 299
r0 = str(r0)[len(str(r2))-1] # size # 303
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 306
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 308
r2 = r2 + r1 # (long) # 310
r6 = r2 + r6 # (char) # 314
r7 = r5 + r7 # (char) # 318
r1 = 0 # 322
r1 = 1 # 323
r2 = 0 # 325
r2 = r1 + r2 # (long) # 326
r2 = r2 + r2 # (long) # 330
r1 = r1 + r2 # (long) # 334
r2 = r1 + r1 # (long) # 338
r1 = r1 + r2 # (long) # 342
r1 = r1 + r1 # (char) # 346
r0 = str(r0)[len(str(r2))-1] # size # 350
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 353
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 355
r2 = r2 + r1 # (long) # 357
r6 = r2 + r6 # (char) # 361
r7 = r5 + r7 # (char) # 365
r1 = 0 # 369
r1 = 1 # 370
r2 = 0 # 372
r2 = r1 + r2 # (long) # 373
r1 = r2 + r1 # (long) # 377
r1 = r1 + r1 # (long) # 381
r1 = r2 + r1 # (long) # 385
r1 = r1 + r1 # (char) # 389
r0 = str(r0)[len(str(r2))-1] # size # 393
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 396
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 398
r2 = r2 + r1 # (long) # 400
r6 = r2 + r6 # (char) # 404
r7 = r5 + r7 # (char) # 408
r1 = 0 # 412
r1 = 1 # 413
r2 = 0 # 415
r2 = r1 + r2 # (long) # 416
r1 = r2 + r1 # (long) # 420
r1 = r1 + r1 # (long) # 424
r1 = r2 + r1 # (long) # 428
r1 = r1 + r1 # (char) # 432
r1 = r2 + r1 # (long) # 436
r0 = str(r0)[len(str(r2))-1] # size # 440
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 443
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 445
r2 = r2 + r1 # (long) # 447
r6 = r2 + r6 # (char) # 451
r7 = r5 + r7 # (char) # 455
r1 = 0 # 459
r1 = 1 # 460
r2 = 0 # 462
r2 = 1 # 463
r1 = r1 + r2 # (char) # 465
r0 = str(r0)[len(str(r2))-1] # size # 469
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 472
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 474
r2 = r2 + r1 # (long) # 476
r6 = r2 + r6 # (char) # 480
r7 = r5 + r7 # (char) # 484
r1 = 0 # 488
r1 = 1 # 489
r2 = 0 # 491
r2 = r1 + r2 # (long) # 492
r1 = r2 + r1 # (long) # 496
r1 = r1 + r1 # (long) # 500
r1 = r2 + r1 # (long) # 504
r1 = 1 # 508
r1 = r2 + r1 # (long) # 510
r0 = str(r0)[len(str(r2))-1] # size # 514
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 517
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 519
r2 = r2 + r1 # (long) # 521
r6 = r2 + r6 # (char) # 525
r7 = r5 + r7 # (char) # 529
r1 = 0 # 533
r1 = 1 # 534
r2 = 0 # 536
r2 = r1 + r2 # (long) # 537
r2 = r2 + r2 # (long) # 541
r1 = r1 + r2 # (long) # 545
r2 = r1 + r1 # (long) # 549
r1 = r1 + r2 # (long) # 553
r1 = r1 + r1 # (char) # 557
r0 = str(r0)[len(str(r2))-1] # size # 561
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 564
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 566
r2 = r2 + r1 # (long) # 568
r6 = r2 + r6 # (char) # 572
r7 = r5 + r7 # (char) # 576
r1 = 0 # 580
r1 = 1 # 581
r1 = r1 + r1 # (long) # 583
r2 = 0 # 587
r2 = r1 + r2 # (long) # 588
r1 = r1 + r1 # (long) # 592
r1 = r1 + r1 # (long) # 596
r1 = r1 + r2 # (long) # 600
r2 = 0 # 604
r2 = 1 # 605
r3 = 0 # 607
r3 = r2 + r3 # (long) # 608
r2 = r2 + r2 # (long) # 612
r2 = r2 + r2 # (long) # 616
r2 = r2 + r2 # (long) # 620
r2 = r2 + r3 # (long) # 624
r1 = r1 + r2 # (char) # 628
r0 = str(r0)[len(str(r2))-1] # size # 632
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 635
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 637
r2 = r2 + r1 # (long) # 639
r6 = r2 + r6 # (char) # 643
r7 = r5 + r7 # (char) # 647
r1 = 0 # 651
r1 = 1 # 652
r1 = 1 # 654
r2 = 0 # 656
r2 = 1 # 657
r2 = r2 + r2 # (long) # 659
r2 = r2 + r2 # (long) # 663
r2 = r2 + r2 # (long) # 667
r1 = r1 + r2 # (char) # 671
r0 = str(r0)[len(str(r2))-1] # size # 675
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 678
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 680
r2 = r2 + r1 # (long) # 682
r6 = r2 + r6 # (char) # 686
r7 = r5 + r7 # (char) # 690
r1 = 0 # 694
r1 = 1 # 695
r2 = 0 # 697
r2 = 1 # 698
r2 = r2 + r2 # (long) # 700
r2 = 1 # 704
r1 = r1 + r2 # (char) # 706
r0 = str(r0)[len(str(r2))-1] # size # 710
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 713
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 715
r2 = r2 + r1 # (long) # 717
r6 = r2 + r6 # (char) # 721
r7 = r5 + r7 # (char) # 725
r1 = 0 # 729
r1 = 1 # 730
r1 = 1 # 732
r2 = 0 # 734
r2 = 1 # 735
r3 = 0 # 737
r3 = r2 + r3 # (long) # 738
r2 = r2 + r2 # (long) # 742
r2 = r2 + r2 # (long) # 746
r2 = r2 + r3 # (long) # 750
r1 = r1 + r2 # (char) # 754
r0 = str(r0)[len(str(r2))-1] # size # 758
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 761
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 763
r2 = r2 + r1 # (long) # 765
r6 = r2 + r6 # (char) # 769
r7 = r5 + r7 # (char) # 773
r1 = 0 # 777
r1 = 1 # 778
r2 = 0 # 780
r2 = r1 + r2 # (long) # 781
r1 = r2 + r1 # (long) # 785
r1 = r1 + r1 # (long) # 789
r1 = r2 + r1 # (long) # 793
r1 = r1 + r1 # (char) # 797
r1 = r1 # 801
r2 = r2 + r2 # (long) # 804
r2 = r1 + r2 # (long) # 808
r1 = r2 + r1 # (char) # 812
r0 = str(r0)[len(str(r2))-1] # size # 816
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 819
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 821
r2 = r2 + r1 # (long) # 823
r6 = r2 + r6 # (char) # 827
r7 = r5 + r7 # (char) # 831
r1 = 0 # 835
r1 = 1 # 836
r2 = 0 # 838
r2 = 1 # 839
r1 = r1 + r2 # (char) # 841
r0 = str(r0)[len(str(r2))-1] # size # 845
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 848
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 850
r2 = r2 + r1 # (long) # 852
r6 = r2 + r6 # (char) # 856
r7 = r5 + r7 # (char) # 860
r1 = 0 # 864
r1 = 1 # 865
r1 = 1 # 867
r2 = 0 # 869
r2 = 1 # 870
r2 = r2 + r2 # (long) # 872
r2 = r2 + r2 # (long) # 876
r1 = r1 + r2 # (char) # 880
r0 = str(r0)[len(str(r2))-1] # size # 884
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 887
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 889
r2 = r2 + r1 # (long) # 891
r6 = r2 + r6 # (char) # 895
r7 = r5 + r7 # (char) # 899
r1 = 0 # 903
r1 = 1 # 904
r2 = 0 # 906
r2 = 1 # 907
r1 = r1 + r2 # (char) # 909
r0 = str(r0)[len(str(r2))-1] # size # 913
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 916
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 918
r2 = r2 + r1 # (long) # 920
r6 = r2 + r6 # (char) # 924
r7 = r5 + r7 # (char) # 928
r1 = 0 # 932
r1 = 1 # 933
r2 = 0 # 935
r2 = 1 # 936
r3 = 0 # 938
r3 = r2 + r3 # (long) # 939
r2 = 1 # 943
r2 = r2 + r3 # (long) # 945
r1 = r1 + r2 # (char) # 949
r0 = str(r0)[len(str(r2))-1] # size # 953
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 956
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 958
r2 = r2 + r1 # (long) # 960
r6 = r2 + r6 # (char) # 964
r7 = r5 + r7 # (char) # 968
r1 = 0 # 972
r1 = 1 # 973
r2 = 0 # 975
r2 = 1 # 976
r3 = 0 # 978
r3 = r2 + r3 # (long) # 979
r2 = r2 + r2 # (long) # 983
r2 = r2 + r2 # (long) # 987
r2 = r2 + r2 # (long) # 991
r2 = r2 + r2 # (long) # 995
r2 = r2 + r3 # (long) # 999
r1 = r1 + r2 # (char) # 1003
r0 = str(r0)[len(str(r2))-1] # size # 1007
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1010
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1012
r2 = r2 + r1 # (long) # 1014
r6 = r2 + r6 # (char) # 1018
r7 = r5 + r7 # (char) # 1022
r1 = 0 # 1026
r1 = 1 # 1027
r1 = 1 # 1029
r2 = 0 # 1031
r2 = 1 # 1032
r3 = 0 # 1034
r3 = r2 + r3 # (long) # 1035
r2 = r2 + r2 # (long) # 1039
r2 = r2 + r2 # (long) # 1043
r2 = r2 + r3 # (long) # 1047
r1 = r1 + r2 # (char) # 1051
r0 = str(r0)[len(str(r2))-1] # size # 1055
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1058
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1060
r2 = r2 + r1 # (long) # 1062
r6 = r2 + r6 # (char) # 1066
r7 = r5 + r7 # (char) # 1070
r1 = 0 # 1074
r1 = 1 # 1075
r2 = 0 # 1077
r2 = r1 + r2 # (long) # 1078
r1 = 1 # 1082
r1 = r1 + r2 # (long) # 1084
r2 = 0 # 1088
r2 = 1 # 1089
r3 = 0 # 1091
r3 = r2 + r3 # (long) # 1092
r2 = r2 + r2 # (long) # 1096
r2 = r2 + r3 # (long) # 1100
r1 = r1 + r2 # (char) # 1104
r0 = str(r0)[len(str(r2))-1] # size # 1108
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1111
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1113
r2 = r2 + r1 # (long) # 1115
r6 = r2 + r6 # (char) # 1119
r7 = r5 + r7 # (char) # 1123
r1 = 0 # 1127
r1 = 1 # 1128
r2 = 0 # 1130
r2 = r1 + r2 # (long) # 1131
r1 = r1 + r1 # (long) # 1135
r1 = r1 + r2 # (long) # 1139
r1 = r1 + r1 # (long) # 1143
r1 = r1 + r1 # (char) # 1147
r1 = r2 + r1 # (long) # 1151
r0 = str(r0)[len(str(r2))-1] # size # 1155
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1158
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1160
r2 = r2 + r1 # (long) # 1162
r6 = r2 + r6 # (char) # 1166
r7 = r5 + r7 # (char) # 1170
r1 = 0 # 1174
r1 = 1 # 1175
r2 = 0 # 1177
r2 = r1 + r2 # (long) # 1178
r1 = r1 + r1 # (long) # 1182
r1 = r1 + r1 # (long) # 1186
r2 = r2 + r2 # (long) # 1190
r1 = r1 + r1 # (long) # 1194
r1 = 1 # 1198
r1 = r2 + r1 # (long) # 1200
r0 = str(r0)[len(str(r2))-1] # size # 1204
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1207
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1209
r2 = r2 + r1 # (long) # 1211
r6 = r2 + r6 # (char) # 1215
r7 = r5 + r7 # (char) # 1219
r1 = 0 # 1223
r1 = 1 # 1224
r2 = 0 # 1226
r2 = r1 + r2 # (long) # 1227
r1 = r1 + r1 # (long) # 1231
r1 = r1 + r2 # (long) # 1235
r1 = r1 + r1 # (long) # 1239
r1 = r1 + r1 # (char) # 1243
r1 = r2 + r1 # (long) # 1247
r0 = str(r0)[len(str(r2))-1] # size # 1251
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1254
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1256
r2 = r2 + r1 # (long) # 1258
r6 = r2 + r6 # (char) # 1262
r7 = r5 + r7 # (char) # 1266
r1 = 0 # 1270
r1 = 1 # 1271
r2 = 0 # 1273
r2 = r1 + r2 # (long) # 1274
r1 = r1 + r2 # (long) # 1278
r2 = r1 + r2 # (long) # 1282
r1 = 0 # 1286
r1 = r2 + r1 # (long) # 1287
r1 = r1 + r1 # (long) # 1291
r2 = r1 + r2 # (long) # 1295
r1 = r1 + r2 # (char) # 1299
r0 = str(r0)[len(str(r2))-1] # size # 1303
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1306
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1308
r2 = r2 + r1 # (long) # 1310
r6 = r2 + r6 # (char) # 1314
r7 = r5 + r7 # (char) # 1318
r1 = 0 # 1322
r1 = 1 # 1323
r1 = 1 # 1325
r2 = 0 # 1327
r1 = r1 + r2 # (char) # 1328
r0 = str(r0)[len(str(r2))-1] # size # 1332
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1335
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1337
r2 = r2 + r1 # (long) # 1339
r6 = r2 + r6 # (char) # 1343
r7 = r5 + r7 # (char) # 1347
r1 = 0 # 1351
r1 = 1 # 1352
r2 = 0 # 1354
r2 = 1 # 1355
r1 = r1 + r2 # (char) # 1357
r0 = str(r0)[len(str(r2))-1] # size # 1361
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1364
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1366
r2 = r2 + r1 # (long) # 1368
r6 = r2 + r6 # (char) # 1372
r7 = r5 + r7 # (char) # 1376
r1 = 0 # 1380
r1 = 1 # 1381
r1 = 1 # 1383
r2 = 0 # 1385
r2 = 1 # 1386
r2 = r2 + r2 # (long) # 1388
r1 = r1 + r2 # (char) # 1392
r0 = str(r0)[len(str(r2))-1] # size # 1396
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1399
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1401
r2 = r2 + r1 # (long) # 1403
r6 = r2 + r6 # (char) # 1407
r7 = r5 + r7 # (char) # 1411
r1 = 0 # 1415
r1 = 1 # 1416
r2 = 0 # 1418
r2 = r1 + r2 # (long) # 1419
r1 = 1 # 1423
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1425
r1 = r2 + r1 # (long) # 1427
r1 = 1 # 1431
r1 = r2 + r1 # (long) # 1433
r2 = r2 + r2 # (long) # 1437
r2 = 0 # 1441
r2 = 1 # 1442
r2 = 1 # 1444
r1 = r1 + r2 # (long) # 1446
r0 = str(r0)[len(str(r2))-1] # size # 1450
tmp = str(r0)
if len(tmp):
	r0 = tmp[-1] # 1453
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1455
r2 = r2 + r1 # (long) # 1457
r6 = r2 + r6 # (char) # 1461
r7 = r5 + r7 # (char) # 1465
r5 = 0 # 1469
r5 = 1 # 1470
r3 = 0 # 1472
r3 = r5 + r3 # (long) # 1473
r5 = r5 + r5 # (long) # 1477
r5 = r5 + r5 # (long) # 1481
if str(r3)[0] == '-':
	r3 = 0
else:
	r3 = -r3 # 1485
r5 = r5 + r5 # (long) # 1487
r5 = r5 + r3 # (long) # 1491
r5 = 1 # 1495
if r6 != r7: print(f"jmp {r5}") # 1497
r4 = 0 # val # 1498
r4 = 1 # 1499
r4 = 1 # 1501
r4 = 1 # 1503
r4 = r4 # 1505
r3 = 0 # 1508
r3 = 1 # 1509
r3 = r3 + r3 # (long) # 1511
r2 = 0 # 1515
r2 = r3 + r2 # (long) # 1516
r3 = r3 + r3 # (long) # 1520
r3 = r3 + r3 # (long) # 1524
r3 = r3 + r2 # (long) # 1528
r2 = 0 # 1532
r2 = 1 # 1533
r1 = 0 # 1535
r1 = r2 + r1 # (long) # 1536
r2 = r2 + r2 # (long) # 1540
r1 = r2 + r1 # (long) # 1544
r2 = r2 + r2 # (long) # 1548
r2 = r2 + r1 # (long) # 1552
r3 = r3 + r2 # (char) # 1556
r3 = r3 # 1560
r4 = r4 + r3 # (char) # 1563
print(r4) # 1567
exit() # 1568
r4 = 0 # val # 1569
r4 = 1 # 1570
r4 = 1 # 1572
r4 = 1 # 1574
r3 = 0 # 1576
r3 = r4 + r3 # (long) # 1577
r4 = r4 # 1581
r2 = 0 # val # 1584
r2 = 1 # 1585
if str(r2)[0] == '-':
	r2 = 0
else:
	r2 = -r2 # 1587
r3 = r2 + r3 # (long) # 1589
r3 = r3 # 1593
r4 = r3 + r4 # (char) # 1596
print(r4) # 1600
exit() # 1601

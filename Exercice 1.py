# Question 1 : #############################################################################################################################
# Code :
for i in range(1, 101):
    print(f"Le carres de nombre {i} est : {i ** 2}")
# Output :
Le carres de nombre 1 est : 1
Le carres de nombre 2 est : 4
Le carres de nombre 3 est : 9
Le carres de nombre 4 est : 16
Le carres de nombre 5 est : 25
Le carres de nombre 6 est : 36
Le carres de nombre 7 est : 49
Le carres de nombre 8 est : 64
Le carres de nombre 9 est : 81
Le carres de nombre 10 est : 100
Le carres de nombre 11 est : 121
Le carres de nombre 12 est : 144
Le carres de nombre 13 est : 169
Le carres de nombre 14 est : 196
Le carres de nombre 15 est : 225
Le carres de nombre 16 est : 256
Le carres de nombre 17 est : 289
Le carres de nombre 18 est : 324
Le carres de nombre 19 est : 361
Le carres de nombre 20 est : 400
Le carres de nombre 21 est : 441
Le carres de nombre 22 est : 484
Le carres de nombre 23 est : 529
Le carres de nombre 24 est : 576
Le carres de nombre 25 est : 625
Le carres de nombre 26 est : 676
Le carres de nombre 27 est : 729
Le carres de nombre 28 est : 784
Le carres de nombre 29 est : 841
Le carres de nombre 30 est : 900
Le carres de nombre 31 est : 961
Le carres de nombre 32 est : 1024
Le carres de nombre 33 est : 1089
Le carres de nombre 34 est : 1156
Le carres de nombre 35 est : 1225
Le carres de nombre 36 est : 1296
Le carres de nombre 37 est : 1369
Le carres de nombre 38 est : 1444
Le carres de nombre 39 est : 1521
Le carres de nombre 40 est : 1600
Le carres de nombre 41 est : 1681
Le carres de nombre 42 est : 1764
Le carres de nombre 43 est : 1849
Le carres de nombre 44 est : 1936
Le carres de nombre 45 est : 2025
Le carres de nombre 46 est : 2116
Le carres de nombre 47 est : 2209
Le carres de nombre 48 est : 2304
Le carres de nombre 49 est : 2401
Le carres de nombre 50 est : 2500
Le carres de nombre 51 est : 2601
Le carres de nombre 52 est : 2704
Le carres de nombre 53 est : 2809
Le carres de nombre 54 est : 2916
Le carres de nombre 55 est : 3025
Le carres de nombre 56 est : 3136
Le carres de nombre 57 est : 3249
Le carres de nombre 58 est : 3364
Le carres de nombre 59 est : 3481
Le carres de nombre 60 est : 3600
Le carres de nombre 61 est : 3721
Le carres de nombre 62 est : 3844
Le carres de nombre 63 est : 3969
Le carres de nombre 64 est : 4096
Le carres de nombre 65 est : 4225
Le carres de nombre 66 est : 4356
Le carres de nombre 67 est : 4489
Le carres de nombre 68 est : 4624
Le carres de nombre 69 est : 4761
Le carres de nombre 70 est : 4900
Le carres de nombre 71 est : 5041
Le carres de nombre 72 est : 5184
Le carres de nombre 73 est : 5329
Le carres de nombre 74 est : 5476
Le carres de nombre 75 est : 5625
Le carres de nombre 76 est : 5776
Le carres de nombre 77 est : 5929
Le carres de nombre 78 est : 6084
Le carres de nombre 79 est : 6241
Le carres de nombre 80 est : 6400
Le carres de nombre 81 est : 6561
Le carres de nombre 82 est : 6724
Le carres de nombre 83 est : 6889
Le carres de nombre 84 est : 7056
Le carres de nombre 85 est : 7225
Le carres de nombre 86 est : 7396
Le carres de nombre 87 est : 7569
Le carres de nombre 88 est : 7744
Le carres de nombre 89 est : 7921
Le carres de nombre 90 est : 8100
Le carres de nombre 91 est : 8281
Le carres de nombre 92 est : 8464
Le carres de nombre 93 est : 8649
Le carres de nombre 94 est : 8836
Le carres de nombre 95 est : 9025
Le carres de nombre 96 est : 9216
Le carres de nombre 97 est : 9409
Le carres de nombre 98 est : 9604
Le carres de nombre 99 est : 9801
Le carres de nombre 100 est : 10000

# Question 2 : #############################################################################################################################
# Code :
for i in range(1, 1001):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
# Output :
1
2
4
7
8
11
13
14
16
17
19
22
23
26
28
29
31
32
34
37
38
41
43
44
46
47
49
52
53
56
58
59
61
62
64
67
68
71
73
74
76
77
79
82
83
86
88
89
91
92
94
97
98
101
103
104
106
107
109
112
113
116
118
119
121
122
124
127
128
131
133
134
136
137
139
142
143
146
148
149
151
152
154
157
158
161
163
164
166
167
169
172
173
176
178
179
181
182
184
187
188
191
193
194
196
197
199
202
203
206
208
209
211
212
214
217
218
221
223
224
226
227
229
232
233
236
238
239
241
242
244
247
248
251
253
254
256
257
259
262
263
266
268
269
271
272
274
277
278
281
283
284
286
287
289
292
293
296
298
299
301
302
304
307
308
311
313
314
316
317
319
322
323
326
328
329
331
332
334
337
338
341
343
344
346
347
349
352
353
356
358
359
361
362
364
367
368
371
373
374
376
377
379
382
383
386
388
389
391
392
394
397
398
401
403
404
406
407
409
412
413
416
418
419
421
422
424
427
428
431
433
434
436
437
439
442
443
446
448
449
451
452
454
457
458
461
463
464
466
467
469
472
473
476
478
479
481
482
484
487
488
491
493
494
496
497
499
502
503
506
508
509
511
512
514
517
518
521
523
524
526
527
529
532
533
536
538
539
541
542
544
547
548
551
553
554
556
557
559
562
563
566
568
569
571
572
574
577
578
581
583
584
586
587
589
592
593
596
598
599
601
602
604
607
608
611
613
614
616
617
619
622
623
626
628
629
631
632
634
637
638
641
643
644
646
647
649
652
653
656
658
659
661
662
664
667
668
671
673
674
676
677
679
682
683
686
688
689
691
692
694
697
698
701
703
704
706
707
709
712
713
716
718
719
721
722
724
727
728
731
733
734
736
737
739
742
743
746
748
749
751
752
754
757
758
761
763
764
766
767
769
772
773
776
778
779
781
782
784
787
788
791
793
794
796
797
799
802
803
806
808
809
811
812
814
817
818
821
823
824
826
827
829
832
833
836
838
839
841
842
844
847
848
851
853
854
856
857
859
862
863
866
868
869
871
872
874
877
878
881
883
884
886
887
889
892
893
896
898
899
901
902
904
907
908
911
913
914
916
917
919
922
923
926
928
929
931
932
934
937
938
941
943
944
946
947
949
952
953
956
958
959
961
962
964
967
968
971
973
974
976
977
979
982
983
986
988
989
991
992
994
997
998


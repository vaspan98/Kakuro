# Kakuro
Modelisation of Kakuro as a CSP problem and solution of Kakuro puzzles.

## Description
https://en.wikipedia.org/wiki/Kakuro

## Examples
https://www.kakuroconquest.com

## Usage
`$ python3 kakuro.py`

## Runtime and Assignments

<p align="center">
<b>Table 1: FC with MRV and LCV (Test 3 times)</b>
</p>

| Puzzle	| Rows | Columns	| Blank Squares	|Test 1 (run time / assignments)	| Test 2 (run time / assignments)	| Test 3(run time / assignments)|
| --- | :---: | :---: | :---: | :---: | :---: | :---: | 
| 1(very easy) | 4 | 3 | 8 | 0.001000 / 8 | 0.001990 / 8 | 0.004990 / 23|
| 2(easy) | 8 | 8 | 46 | 0.104730 / 118 | 0.104720 / 105 | 0.107710 / 130 |
| 3(intermediate) | 8 |8 | 48 | 0.705120 / 1966 | 1.255670 / 1859 | 0.693140 / 1735 |
| 4(intermediate)| 9 | 11 | 73 | 4.470050 / 3140 | 11.642020 / 6275 | 7.156880 / 5455 |
| 5(hard) | 8 | 8 | 48 | 0.209440 / 1428 | 0.516620 / 2681 | 0.221410 / 1816 |
| 6(challenging) | 8 | 8 | 48 | 0.135630 / 871 | 0.358040 / 1532 | 0.237340 / 1108 |
| 7(expert) | 9 | 11 | 73 | 285.94 / 159306 | 479.03 / 189876 | 469.57 / 186554 |

<p align="center">
<b>Table 2: MAC with MRV and LCV (Test 3 times)</b>
</p>

| Puzzle	| Rows | Columns	| Blank Squares	|Test 1 (run time / assignments)	| Test 2 (run time / assignments)	| Test 3(run time / assignments)|
| --- | :---: | :---: | :---: | :---: | :---: | :---: | 
| 1(very easy) |	4	| 3	| 8	| 0.006980 / 8	| 0.004990 / 8	| 0.009970 / 8 |
| 2(easy)	| 8	| 8	| 46	| 0.327110 / 35	| 0.366010 / 35	| 0.506610 / 34 |
| 3(intermediate)	| 8	| 8	| 48	| 0.532570 / 43	| 0.551500 / 43	| 0.625300 / 40 |
| 4(intermediate)	| 9	| 11	| 73	| 2.540210 / 76	| 5.337740 / 79	| 1.816150 / 50 |
| 5(hard)	| 8	| 8	| 48	| 0.230380 / 46	| 0.570480 / 43	| 0.155580 / 41 |
| 6(challenging)	| 8	| 8	| 48	| 0.319110 / 55	| 0.510630 / 65	|0.437830 / 54 |
| 7(expert)	| 9	| 11	| 73	| 22.857870 / 66	| 11.677790 / 54	| 10.507930 / 58 |

<p align="center">
<b>Table 3: FC with MRV and LCV (Final Results)</b>
</p>

| Puzzle |	Rows |	Columns |	Blank Squares	| Min Run Time (seconds) |	Max Run Time (seconds) |	Average Run Time (seconds) |	Average Extra Assignments |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| 1(very easy)	| 4	| 3	| 8	| 0.001000	| 0.004990	| 0.00266‬	| 13 |
| 2(easy)	| 8	| 8	| 46	| 0.104720	| 0.107710	| 0.10572‬	| 118 | 
| 3(intermediate)	| 8	| 8	| 48 | 0.693140	| 1.255670	| 0.88464	| 1853 |
| 4(intermediate)	| 9	| 11	| 73	| 4.470050	| 11.642020	‭| 7.88666‬‬‬	| 4957 |
| 5(hard)	| 8	| 8	| 48	| 0.209440	| 0.516620	| 0.31581	| 1975 |
| 6(challenging)	| 8	| 8	| 48	| 0.135630 	| 0.358040	| 0.24363	| 1171 |
| 7(expert)	| 9	| 11	| 73 |	285.94	| 479.03 | 411.51 | 178578 |

<p align="center">
<b>Table 4: MAC with MRV and LCV (Final Results)</b>
</p>

| Puzzle |	Rows |	Columns |	Blank Squares	| Min Run Time (seconds) |	Max Run Time (seconds) |	Average Run Time (seconds) |	Average Extra Assignments |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| 1(very easy)	| 4 |	3 |	8 |	0.004990 |	0.009970 |	‭0.00733 |‬‬‬	8 |
| 2(easy) |	8 |	8 |	46 |	0.327110 |	0.506610 |	0.3999‬0 |	35 |
| 3(intermediate) |	8 |	8 |	48 |	 0.532570 |	0.625300 |	0.56979 | ‬	42 |
| 4(intermediate) |	9 |	11 |	73 |	1.816150 |	5.337740 |	3.37678 |	68 |
| 5(hard) |	8 |	8 |	48 |	0.155580 |	0.570480 |	0.31881 |	43 |
| 6(challenging) |	8 |	8 |	48 |	 0.319110 |	0.510630 |	0.42252‬ |	58 |
| 7(expert) |	9 |	11 |	73 |	10.507930 |	22.857870 |	15.01453 |	59 |

## Ownership
The code in kakuro.py is written by me.  

The rest of the files uploaded are modified by me and owned by the University of Berkeley.  
They can be found here: https://github.com/aimacode/aima-python

### Note
You will find all files needed to execute the project in the above link.

## Author
Vasilis Panagakis

## Date
December 2019

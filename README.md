# Security_identifier_types_recognition

Security identifier types recognition provides regex to recognize all the most common identifier typse i.e. CUSIP, SEDOL, ISIN. 
In some cases information about security id type is not provided in data and it need to be retrieve from id itself, by its construcion.
This code use regular expression matching proper id to it's types.

It have been tested on bilions of rows on Unix envirnoment. Works with 95-97% efficiency.

Steps:
1. Reads input file line by line, humble does not lock memory
2. split file by delimiter
3. defines column in which id is stored
4. match id type to id by id construcion pattern with regex
5. once id is matched to particulat id type
  5.1 adding proper id type name to first field of row
  5.2 adding rest of row
  5.3 creating file with id name as file name. Each matching row will be added to this file 'a'.
  5.4 closing write funcion
6. closing input
7. closing outputs

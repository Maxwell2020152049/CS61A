These files contain a few examples of Schemish Prolog programs.

* (fact (PREDICATE-SYMBOL OPERANDS))   or
  (! (PREDICATE-SYMBOL OPERANDS))

      The predicate (logical true/false function) named PREDICATE-SYMBOL
      holds for the given OPERANDS.

* (fact (PREDICATE-SYMBOL0 OPERANDS0)
        (PREDICATE-SYMBOL1 OPERANDS1)
        ...
        (PREDICATE-SYMBOLn OPERANDSn))  or

  (!    (PREDICATE-SYMBOL0 OPERANDS0)
        (PREDICATE-SYMBOL1 OPERANDS1)
        ...
        (PREDICATE-SYMBOLn OPERANDSn))

       Assuming n >= 0 this means that (PREDICATE0 OPERANDS0) holds 
       if each of (PREDICATE-SYMBOLi OPERANDSi) holds.

* (query (PREDICATE-SYMBOL0 OPERANDS0) ... (PREDICATE-SYMBOLn OPERANDSn))

       True if all the (PREDICATEi OPERANDSi) are true.  Reports the
       bindings for all the logical variables for each possible
       substitution that makes then all true.

* (load FILENAME)

       Loads facts, queries, and other commands from FILENAME.

* (clear)

       Delete all facts from the database.

* (max-depth N)

       Set N as the maximum depth of search.


* In operands, symbols starting with ? are logical variables, which match
  expressions.

* An expression of the form (ITEM1 ITEM2...ITEMn . ?VAR) matches a list
  that starts with matches for ITEM1...ITEMn and then continues with additional
  items, which are matched (as a list) by ?VAR.  In other words, ?VAR matches
  a tail of a list.  For example, (?x ?y . ?z) would match any list containing
  at least two elements.  ?x would match the first item, ?y the second, and
  ?z the list of remaining items.






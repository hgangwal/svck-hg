// Test for package encapsulation: a class needs to be encapsulated in a package
// This file should pass.

class c;
     protected int state_i1;
     rand int rand_i1;
     local int lvar_i1;
   endclass : c

class c3;
  protected int state_i1;
  rand int rand_i1;
  protected int lvar_i1;
  protected int prot_i1;
endclass : c3
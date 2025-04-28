// Test for package encapsulation: a class needs to be encapsulated in a package.
// This file should pass.

package my_pkg;  
  class Transaction;  
    // Class definition  
  endclass  

  class Driver;  
    // Class definition  
  endclass  
endpackage : my_pkg  // Proper encapsulation


package myc2pkg;
class c2;
  protected int state_i1;
  protected rand int rand_i1;
  protected int lvar_i1;
  protected int prot_i1;
endclass : c2
endpackage : myc2pkg

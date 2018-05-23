
import plex


# ... συμπληρώστε τον κώδικά σας για τον συντακτικό αναλυτή - αναγνωριστή της γλώσσας ...



"""
Stmt_list       ->      Stmt Stmt_list | ε
Stmt            ->      id = Expr | print Expr
Expr		->	not Andterm Andterm_tail | Andterm Andterm_tail
Andterm_tail	->	and Andterm Andterm_tail | ε
Andterm		->	Orterm Orterm_tail
Orterm_tail	->	or Orterm Orterm_tail | ε
Orterm		->	( Expr ) | id | Bin 
Bin		->	1 | 0 | true | false | t | f

FIRST
Stmt_list:      id,print,ε
Stmt:           id,print
Expr:		not,(,id,bin,and
Andterm_tail:	and,ε
Andterm:	(,id,bin
Orterm_tail:	or,ε
Orterm:		(,id,bin
Bin:		1,0,true,false,t,f

FOLLOW
Stmt_list:      $
Stmt:           
Expr:		)
Andterm_tail:	)
Andterm:	and,)
Orterm_tail:	and,)
Orterm:		or,fl 
Bin:
  
"""



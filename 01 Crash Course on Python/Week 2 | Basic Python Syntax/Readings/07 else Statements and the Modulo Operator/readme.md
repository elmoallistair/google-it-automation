## else Statements and the Modulo Operator

<hr>

We just covered the *if* statement, which executes code if an evaluation is true and skips the code if it’s false. But what *if* we wanted the code to do something different if the evaluation is false? We can do this using the **else** statement. The **else** statement follows an *if* block, and is composed of the keyword **else** followed by a colon. The body of the **else** statement is indented to the right, and will be expected if the above *if* statement doesn’t execute.

We also touched on the modulo operator, which is represented by the percent sign: **%**. This operator performs integer division, but only returns the remainder of this division operation. If we’re dividing 5 by 2, the quotient is 2, and the remainder is 1. Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over. In this case, 10%2 would return 0, as there is no remainder.
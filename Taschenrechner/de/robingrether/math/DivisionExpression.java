package de.robingrether.math;

public class DivisionExpression extends Expression {
	
	private final Expression dividend, divisor;
	
	public DivisionExpression(Expression dividend, Expression divisor) {
		this.dividend = dividend;
		this.divisor = divisor;
	}
	
	public double evaluate() {
		double divisor = this.divisor.evaluate();
		if(divisor == 0) throw new ArithmeticException("Divide by zero");
		return dividend.evaluate() / divisor;
	}
	
}
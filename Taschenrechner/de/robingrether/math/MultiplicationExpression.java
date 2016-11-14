package de.robingrether.math;

public class MultiplicationExpression extends Expression {
	
	private final Expression factor1, factor2;
	
	public MultiplicationExpression(Expression factor1, Expression factor2) {
		this.factor1 = factor1;
		this.factor2 = factor2;
	}
	
	public double evaluate() {
		return factor1.evaluate() * factor2.evaluate();
	}
	
}
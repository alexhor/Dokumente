package de.robingrether.math;

public class SubtractionExpression extends Expression {
	
	private final Expression minuend, subtrahend;
	
	public SubtractionExpression(Expression minuend, Expression subtrahend) {
		this.minuend = minuend;
		this.subtrahend = subtrahend;
	}
	
	public double evaluate() {
		return minuend.evaluate() - subtrahend.evaluate();
	}
	
}
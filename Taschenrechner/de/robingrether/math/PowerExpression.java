package de.robingrether.math;

public class PowerExpression extends Expression {
	
	private final Expression basis, exponent;
	
	public PowerExpression(Expression basis, Expression exponent) {
		this.basis = basis;
		this.exponent = exponent;
	}
	
	public double evaluate() {
		return Math.pow(basis.evaluate(), exponent.evaluate());
	}
	
}
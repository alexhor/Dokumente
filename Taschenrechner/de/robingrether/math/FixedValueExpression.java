package de.robingrether.math;

public class FixedValueExpression extends Expression {
	
	private final double value;
	
	public FixedValueExpression(double value) {
		this.value = value;
	}
	
	public double evaluate() {
		return value;
	}
	
}
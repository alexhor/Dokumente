package de.robingrether.math;

public class AdditionExpression extends Expression {
	
	private final Expression summand1, summand2;
	
	public AdditionExpression(Expression summand1, Expression summand2) {
		this.summand1 = summand1;
		this.summand2 = summand2;
	}
	
	public double evaluate() {
		return summand1.evaluate() + summand2.evaluate();
	}
	
}